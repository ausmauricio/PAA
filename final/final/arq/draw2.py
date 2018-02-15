# -*- coding: utf-8 -*-

# Autor: Mauricio de Oliveira (mauricioliveira_@hotmail.com)
# Universidade Federal de Minas Gerais
# Departamento de Ciência da Computação

import sys
import networkx as nx
from myfunctions import read_file
import matplotlib.pyplot as plt

FILE_END    = '0,0'
DELIMITER_1 = ","
DELIMITER_2 = " " 

# ['circular_layout', 'fruchterman_reingold_layout', 'random_layout', 'shell_layout', 'spectral_layout', 'spring_layout']

if __name__ == "__main__":

    delimiter   = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    input_graph = read_file(sys.argv[1], delimiter)

    g = nx.Graph()
    g.add_edges_from(input_graph)

    pos_list = [x for x in dir(nx) if x.endswith('_layout')]
    
    for pos_name in pos_list:
        
        plt.figure(figsize=(10,9))
        p = getattr(nx, pos_name)(g)
        mcds = set(['10', '14', '4', '5', '6', '7', '8'])
        nx.draw_networkx(g, pos = p, node_color =  [0.7 if v in mcds else 0.2 for v in g])
        #nx.draw_networkx(g, pos = p)
        #nx.draw_networkx_labels(g, pos = p, labels = {'Los Angeles, CA': 'LA', 'New York, NY': 'NYC'}, font_size=18, font_color='w')
        plt.savefig(sys.argv[1] + pos_name + ".png")
