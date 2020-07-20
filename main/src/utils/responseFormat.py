def sentence(positive, negative, neutral, unanalyzed=0):
    return {
        'positive': positive,
        'negative': negative,
        'neutral': neutral,
        'unanalyzed': unanalyzed,
    }


def ratio(total, positive=0, negative=0, neutral=0):
    if total == 0:
        return {
            'positive': 0,
            'negative': 0,
            'neutral': 0,
            'total': 0
        }
    return {
        'positive': (positive / total) * 100,
        'negative': (negative / total) * 100,
        'neutral': (neutral / total) * 100,
        'total': total
    }


def stats(total, positive, negative, neutral, created_time):
    return {
        'analyze_quantity': total,
        'average_feeling': positive - negative,
        'positive_comment': positive,
        'negative_comment': negative,
        'neutral_comment': neutral,
        'created_time': created_time
    }
