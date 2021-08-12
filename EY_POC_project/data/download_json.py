import requests

r = requests.get('http://downloads.cs.stanford.edu/nlp/data/coqa/coqa-train-v1.0.json')

print(r.json())