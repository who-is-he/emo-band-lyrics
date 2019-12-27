import random, json
from chain import walk_graph

CHARLIMIT = 280

def compose():
    with open('chain.json', 'r') as f:
            markov_graph = json.load(f)
            tweet = ''
            new_line = ''
            lines = random.randint(3, 6)

            while len(tweet) + len(new_line) < CHARLIMIT and lines > 0:
                tweet += new_line
                word_list = tweet.split()
                last_word = word_list[-1] if len(word_list) > 0 else None
                new_line = ' '.join(walk_graph(
                    markov_graph, 
                    distance=random.randint(2, 6), 
                    start_node=last_word
                ))
                new_line += '\n'
                lines -= 1
            return tweet[0:len(tweet)-1]

    return 'error'
