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

def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)

    # show graph
    plt.show()

if __name__ == "__main__":

    delimiter   = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    input_graph = read_file(sys.argv[1], delimiter)
    G=nx.random_geometric_graph(200,0.125)
    g = nx.Graph()
    #labels = map(chr, range(65, 65+len(input_graph)))
    #draw_graph(input_graph)
    g.add_edges_from(input_graph)
    #pos = nx.spring_layout(g,k=0.15,iterations=20)
    nx.draw_networkx(G)
    plt.show()
    #plt.savefig(sys.argv[1] + ".png")
