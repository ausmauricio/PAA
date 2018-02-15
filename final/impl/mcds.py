# -*- coding: utf-8 -*-

# Autor: Mauricio de Oliveira (mauricioliveira_@hotmail.com)
# Universidade Federal de Minas Gerais
# Departamento de Ciência da Computação

import sys
from itertools import combinations  

FILE_END    = '0,0'
DELIMITER_1 = ","
DELIMITER_2 = " "
 
def read_file():

    input_file = open(sys.argv[1], "r").read().splitlines()
    
    graph_data = []

    for line in input_file: 

        if line == FILE_END: 
            break
        else:  
            graph_data.append(tuple(line.split(DELIMITER_1)))

    else:       
        sys.exit("Arquivo de entrada inválido")
    
    return graph_data

def create_adj_list(graph_data):

    graph_dict = {}

    for data in graph_data:
        
        if data[0] not in graph_dict:  
      
            graph_dict[data[0]] = {data[1]: 1}

            if data[1] not in graph_dict: 
                graph_dict[data[1]] = {data[0]: 1}
            else:
                graph_dict[data[1]][data[0]] = 1

        else:
        
            graph_dict[data[0]][data[1]] = 1

            if data[1] not in graph_dict:
                graph_dict[data[1]] = {data[0]: 1}
            else:
                graph_dict[data[1]][data[0]] = 1
    
    return graph_dict    

def is_dominating(g, tp, vertices, num, n):

    if num == 1:

        return True if len(g[tp[0]]) == n-1 else False

    else:

        seen = set()

        for v in tp:

            for vv in g[v]:

                seen.add(vv)

    return True if seen == set(vertices) else False

def is_connected(g, tp, i):
 
    if i == 1: 

        return True

    else:

        seen = set()

        for v in tp:

            for vv in g[v]:

                if vv in tp:

                    seen.add(vv)

    return True if seen == set(tp) else False                       

def find_mcds(g, vertices, n):
     
    for k in xrange(1,n):

        for candidate in combinations(vertices, k):

            if is_connected(g, candidate, k):
        
                if is_dominating(g, candidate, vertices, k, n):

                    return(candidate)
    
    return(vertices) 

graph_data  = read_file()
g           = create_adj_list(graph_data)
vertices    = sorted(g.keys())
n           = len(vertices)

from timeit import default_timer as timer
start = timer()

print(find_mcds(g, vertices, n))

end = timer()

print(end - start)         
