import logging
from main.src.logger.config import logger
import csv
import nltk
from main.src.utils.tweet import clearTweet

log = logging.getLogger(__name__)
logger()

def transform_instance(row):
    cur_row = []
    # Prefix the index-ed label with __label__
    label = "__label__" + row['sentiment'].upper()
    cur_row.append(label)
    # Clean tweet and tokenize it
    cur_row.extend(nltk.word_tokenize(clearTweet(row['tweet_text'])))
    return cur_row


def processDataset(file, out=''):
    log.info('Converting csv to dataset from ' + file)
    if out == '':
        out = file[:file.rindex('.')] + '.train'
    i = 0
    with open(out, 'w', newline='', encoding='utf-8') as csvout:
        spamwriter = csv.writer(csvout, delimiter=' ', lineterminator='\n')
        with open(file, newline='') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                if row['sentiment'].upper() in ['POSITIVE', 'NEGATIVE', 'NEUTRAL'] and row['tweet_text'] != '':
                    trow = transform_instance(row)
                    spamwriter.writerow(trow)
                    i += 1
                    if i % 1000 == 0:
                        log.info('row ' + str(i))
    log.info('Done. Total rows: ' + str(i))
    log.info('Dataset saved to ' + out)
    return out


def upsampling(file, out='', ratio=0.8):
    log.info('Upsampling the dataset from ' + file)
    if out == '':
        out = file[:file.rindex('.')] + '_upsampled.train'
    i = 0
    labels = {}
    datas_label = {}
    upsampled = []

    log.info('Reading data')
    with open(file, 'r', newline='', encoding='utf8', errors='ignore') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            data = row[0].split(' ', 1)
            labels[data[0]] = labels.get(data[0], 0) + 1
            if not data[0] in datas_label:
                datas_label[data[0]] = [row[0]]
            else:
                datas_label[data[0]].append(row[0])
            i += 1
            if i % 1000 == 0:
                log.info('row ' + str(i))

    max_label = max(datas_label, key=lambda k: len(datas_label[k]))

    log.info('Upsampling data')
    for label in datas_label:
        upsampled.extend(datas_label[label])
        if label == max_label:
            continue
        item_added = 0
        item_needed = (len(datas_label[max_label]) - len(datas_label[label]) / ratio)
        while item_added < item_needed:
            item_added = item_added + max(0, min(item_needed - item_added, len(datas_label[label])))
            upsampled.extend(datas_label[label][:int(item_added)])

    log.info('Writing new data')
    i = 0
    with open(out, 'w', newline='', encoding='utf-8') as fout:
        for row in upsampled:
            fout.write(row + '\n')
            i += 1
            if i % 1000 == 0:
                log.info('row ' + str(i))
    log.info('Done. Total rows: ' + str(i))
    log.info('Upsampled dataset saved to ' + out)


def generateModel(f):
    path = processDataset(f)
    upsampling(path)
