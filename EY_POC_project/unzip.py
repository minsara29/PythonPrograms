import pandas as pd
import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('data/amazon_qa/qa_Video_Games.json.gz')

print(df)

df.to_csv('output\\amazon_qa\\qa_Video_Games.csv', index=False, encoding="utf-8")