import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
import sys

def WPGMA(path):
    file = open(path, 'r')
    contents = file.read().splitlines()
    file.close()
    column_headers = contents[0].split(' ')[1:]
    matrix = np.array([[int(x) if not x == '0' else np.nan for x in contents[y].split(' ')[1:]] for y in range(1, len(contents))]) # Quicker to maybe map int?
    tree = nx.DiGraph()
    for n in range(len(column_headers)):
        tree.add_node(column_headers[n], pos=(0,0))#, pos=(2*(n+1), 2))

    n = len(column_headers)
    print(tree.nodes())
    print(matrix)
    while matrix.shape[0] > 2:
        print()
        s_index = np.unravel_index(np.nanargmin(matrix), matrix.shape) # Is there a better way to find index of smallest element?
        s_label = [column_headers[s_index[0]], column_headers[s_index[1]]]

        new_row = np.array([(matrix[s_index[0], j] + matrix[s_index[1], j])/2\
                    if not j == s_index[0] else np.nan for j in [_ for _ in range(matrix.shape[0]) if not _ == s_index[1]]])
        # Create a new node at min point
        new_node = column_headers[s_index[0]] + column_headers[s_index[1]]
        tree.add_node(new_node, pos=(0,0))#, pos=((tree.node[s_label[0]]['pos'][0] + tree.node[s_label[1]]['pos'][0])/2 + 2, tree.node[s_label[0]]['pos'][1] + 2))

        # Create edge from new node to the nodes coinciding at the min points
        tree.add_edge(new_node, column_headers[s_index[0]])
        tree.add_edge(new_node, column_headers[s_index[1]])

        matrix = np.delete(matrix, (s_index[1]), axis=0)
        matrix = np.delete(matrix, (s_index[1]), axis=1)

        matrix[s_index[0], :] = new_row
        matrix[:, s_index[0]] = new_row
        column_headers = [_ for _ in column_headers if not _ in s_label and column_headers.index(_) < s_index[0]] + [column_headers[s_index[0]] + column_headers[s_index[1]]] + [_ for _ in column_headers if not _ in s_label and column_headers.index(_) > s_index[0]]

        print(column_headers)
        print(matrix)
    
    new_node = column_headers[0] + column_headers[1]
    tree.add_node(new_node, pos=(0,0))#, pos=((tree.node[column_headers[0]]['pos'][0] + tree.node[column_headers[1]]['pos'][0])/2 + 2, tree.node[column_headers[0]]['pos'][1] + 2))
    tree.add_edge(new_node, column_headers[0])
    tree.add_edge(new_node, column_headers[1])

    nodes = [_ for _ in tree.nodes()]
    nodes.reverse()
    root = nodes[0]

    for node in nodes:
        if node == root:
            tree.node[node]['pos'] = (n, n)

        node_pos = tree.node[node]['pos']
        children = [_ for _ in tree.neighbors(node)]

        factor = len(node)

        if len(children):
            tree.node[children[0]]['pos'] = (node_pos[0] - 1*factor, node_pos[1] - 1)
            tree.node[children[1]]['pos'] = (node_pos[0] + 1*factor, node_pos[1] - 1)

    nx.draw_networkx(tree, pos=nx.get_node_attributes(tree, 'pos'))
    plt.axis('off')
    plt.show()

start_time = time.time()
WPGMA('matrix1.txt')
WPGMA('matrix2.txt')
WPGMA('matrix.10.txt')
end_time = time.time()
print('Time taken {0}'.format(end_time - start_time))