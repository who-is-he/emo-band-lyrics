import numpy as np
import random

def walk_graph(graph, distance=10, start_node=None):
    if distance <= 0:
        return []

    if start_node == None:
        start_node = random.choice(list(graph.keys()))

    if start_node not in graph:
        possible = [
            key
            for key in graph
                if start_node in key
        ]
        start_node = random.choice(possible)

        # if start node isn't in any keys, which shouldn't happen *shrug*
        if start_node == None:
            start_node = random.choice(list(graph.keys()))

    weights = np.array(
        list(graph[start_node].values()),
        dtype=np.float64
    )

    weights /= weights.sum()

    choices = list(graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)

    return [chosen_word] + walk_graph(
        graph, distance=distance-1,
        start_node=chosen_word
    )
