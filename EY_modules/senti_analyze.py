import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer as si

nltk.download('vader_lexicon')

def advancedSentimentAnalyzer():
    sentences = [
        ':)',
        ':(',
        'She is so :(',
        'what is you name?',
        'I love the way cricket is played by the champions',
        'She neither likes coffee nor tea',
    ]
    senti = si()
    print(' -- built-in intensity analyser --')
    for sentence in sentences:
        print('[{}]'.format(sentence), end=' --> ')
        kvp = senti.polarity_scores(sentence)
        for k in kvp:
            print('{} = {}, '.format(k, kvp[k]), end='')
        print()


advancedSentimentAnalyzer()