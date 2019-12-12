import random, json
from chain import walk_graph

CHARLIMIT = 280

def compose():
    with open('chain.json', 'r') as f:
            markov_graph = json.load(f)
            tweet = ''
            lines = random.randint(3, 6)
            while len(tweet) < CHARLIMIT and lines > 0:
                tweet += ' '.join(walk_graph(markov_graph, distance=random.randint(3, 12)))
                tweet += '\n'
                lines -= 1
            return tweet[0:len(tweet)-1]
    return 'error'

if __name__ == '__main__':
    print(compose())