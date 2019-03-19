import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
import sys

def WPGMA(path):
    print('Reading from file..')
    file = open(path, 'r')
    contents = file.read().splitlines()
    file.close()
    column_headers = contents[0].split(' ')[1:]
    matrix = np.array([[int(x) if not x == '0' else np.nan for x in contents[y].split(' ')[1:]] for y in range(1, len(contents))]) # Quicker to maybe map int?
    print('Read complete. Displaying data:')
    print('Generating initial tree..')
    tree = nx.DiGraph()
    for node in column_headers:
        tree.add_node(node)

    print(tree.nodes())

    while matrix.shape[0] > 2:
        s_index = np.unravel_index(np.nanargmin(matrix), matrix.shape) # Is there a better way to find index of smallest element?
        matrix[s_index[1], s_index[0]] = np.nan
        print(matrix)
        print(s_index)

        new_row = [(len(column_headers[s_index[0]])*matrix[s_index[0], j] + len(column_headers[s_index[1]])*matrix[s_index[1], j])\
                    /(len(column_headers[s_index[0]] + column_headers[s_index[1]]))\
                    if not j == s_index[0] else np.nan for j in [_ for _ in range(matrix.shape[0]) if not _ == s_index[1]]]
        print(np.array(new_row))
        # Create a new node at min point
        new_node = column_headers[s_index[0]] + column_headers[s_index[1]]

        tree.add_node(new_node)
        # Create edge from new node to the nodes coinciding at the min points
        tree.add_edge(new_node, column_headers[s_index[0]])
        tree.add_edge(new_node, column_headers[s_index[1]])

        matrix = np.delete(matrix, (s_index[0]), axis=0)
        matrix = np.delete(matrix, (s_index[1]), axis=1)

        break
    print(matrix)
    print(tree.nodes())

start_time = time.time()
WPGMA('matrix3.txt')
end_time = time.time()
print('Time taken {0}'.format(end_time - start_time))