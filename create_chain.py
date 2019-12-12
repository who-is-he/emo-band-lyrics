import codecs, json
from collections import defaultdict

path = 'corpus.txt'

with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    text = text.replace("”", '')
    text = text.replace('"', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    tokens = [
        word
        for word in text.split()
            if word != ''
    ]

markov_graph = defaultdict(lambda: defaultdict(int))
last_word = tokens[0].lower()

for word in tokens[1:]:
    word = word.lower()
    markov_graph[last_word][word] += 1
    last_word = word

with open('chain.json', 'w') as out:
    json.dump(markov_graph, out, indent=4, sort_keys=True)
