import codecs, json
from collections import defaultdict

path = 'dict.txt'
replace_chars = "”\"()[]\{}\u6969\u0647\u0648\u0627\u0644\u05b1\u05b9\u05e0\u05d5\u05d7\u05d6\u05c2\u05e8\u05b5\u05b4\u05d4\u05d0\u05b6\u05b8\u05d3\u05bc\u05dd\u062f\u05dc\u05d9\u062d\u0635\u0645\u0642\u05e9\u05b0\u05c1\u05de\u05b7\u05e2"

with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

    for c in replace_chars:
        text = text.replace(c, '')

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
