def sentence(positive, negative, neutral, unanalyzed=0):
    return {
        'positive': positive,
        'negative': negative,
        'neutral': neutral,
        'unanalyzed': unanalyzed,
    }


def stats(total, positive=0, negative=0, neutral=0):
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
