import numpy as np
import random

def walk_graph(graph, distance=15, start_node=None):
    if distance <= 0:
        return []

    if not start_node:
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
