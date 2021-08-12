import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as si
import re

nltk.download('vader_lexicon')



def extract_sentimental(string):
    string = str(string)
    print('[{}]'.format(string), end=' --> ')
    kvp = senti.polarity_scores(string)
    for k in kvp:
        print('{} = {}, '.format(k, kvp[k]), end='')

    if kvp['neg'] > kvp['pos'] > kvp['neu']:
        return "Negative"
    elif kvp['pos'] > kvp['neu']:
        return "Positive"
    else:
        return "Neutral"

def label_by_word(string):
    actual = str(string).translate({ord(c): " " for c in "'!@#$%^&*()’[]{};:,./<>?\|`~-=_+"}).lower()
    words_in_string = set(actual.split(' '))
    if words_in_string.intersection(negative_words):
        list_words.append(words_in_string.intersection(negative_words))
        return 'Negative'
    elif words_in_string.intersection(positive_words):
        list_words.append(words_in_string.intersection(positive_words))
        return 'Positive'
    else:
        list_words.append(None)
        return "Neutral"


script = []
sentimental_label = []
word_label = []
list_words = []

df = pd.read_excel('ey_data/EY Foundry - Consolidated Pilot Transcripts Data.xlsx', sheet_name='Transcripts')
words = pd.read_csv('ey_data/positive_negative_word.csv')
negative_words = set(words["Negative"])
positive_words = set(words["Positive"])



senti = si()
for index, row in df.iterrows():
    results = extract_sentimental(row["Learner's transcript"])
    label = label_by_word(row["Learner's transcript"])
    script.append(row["Learner's transcript"])
    sentimental_label.append(results)
    word_label.append(label)

sentimental_df = pd.DataFrame(list(zip(script, sentimental_label, word_label, list_words)),
               columns =["Learner's transcript", "Sentimental Label", "Label By Word", "Words"])
sentimental_df.to_csv("output_ey_data/sentimental_extractions.csv")


#
txt = "gross. Thanks for taking the time to meet with me and for sharing your your interest in getting promoted. So can you share with me a little bit more about you know what you'd like to do."
txt = set(txt.split(' '))
print(txt)
print(txt.intersection(negative_words))
if txt.intersection(negative_words):
    print('empty')

