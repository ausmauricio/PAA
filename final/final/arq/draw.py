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

if __name__ == "__main__":

    delimiter   = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    input_graph = read_file(sys.argv[1], delimiter)

    g = nx.Graph()
    g.add_edges_from(input_graph)
    nx.draw_networkx(g)
    plt.savefig(sys.argv[1] + "1.png")
