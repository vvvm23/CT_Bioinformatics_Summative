import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import time
import sys

def WPGMA(path):
    file = open(path, 'r')
    contents = file.read().splitlines()
    column_headers = contents[0].split(' ')[1:]
    matrix = [[int(x) for x in contents[y].split(' ')[1:]] for y in range(1, len(contents))] # Quicker to maybe map int?
    print(column_headers)
    print(np.array(matrix))
    file.close()

WPGMA('matrix1.txt')