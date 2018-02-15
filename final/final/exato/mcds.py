# -*- coding: utf-8 -*-

# Autor: Mauricio de Oliveira (mauricioliveira_@hotmail.com)
# oliveiramauricio@ufmg.br
# Universidade Federal de Minas Gerais
# Departamento de Ciência da Computação

import sys
from timeit import default_timer as timer
from myfunctions import read_file, create_adj_list
from itertools import combinations  
from random import randint

DELIMITER_1 = "," 
DELIMITER_2 = " "

def dfs(g, start):

    visited = set()
    stack   = [start]
    
    while stack:

        v = stack.pop()

        if v not in visited:

            visited.add(v)
            stack.extend(g[v] - visited)
    
    return visited

def is_connected(g, cands, i):
 
    if i == 1: 

        return True

    else:

        induced_subg = {k: set([item for item in v if item in cands]) 
                        for k, v in g.items() if k in cands}

        k    = randint(0, i-1)
        v    = cands[k]
        seen = dfs(induced_subg, v)
 
    return True if seen == set(cands) else False                       

def is_dominating(g, cands, vertices):

    seen = set()
    seen.update(cands)
    seen.update([vv for v in cands for vv in g[v]])

    return True if seen == set(vertices) else False

def find_mcds(g, vertices, n):
     
    for k in xrange(1,n):

        for candidate in combinations(vertices, k):

            if is_connected(g, candidate, k):

                if is_dominating(g, candidate, vertices):
                            
                    return(candidate)
    
    return(vertices) 

if __name__ == "__main__":

    delimiter   = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    graph_data  = read_file(sys.argv[1], delimiter)
    g           = create_adj_list(graph_data)
    vertices    = g.keys()
    n           = len(vertices)

    start = timer()
    mcds  = find_mcds(g, vertices, n)
    print(mcds, len(mcds))

    end = timer()

    print(end - start)

