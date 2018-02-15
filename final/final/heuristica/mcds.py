# -*- coding: utf-8 -*-

# Autor: Mauricio de Oliveira (mauricioliveira_@hotmail.com)
# Universidade Federal de Minas Gerais
# Departamento de Ciência da Computação

import sys
from timeit import default_timer as timer
from myfunctions import read_file, create_adj_list
from itertools import combinations  
from random import randint, shuffle

FILE_END    = '0,0'
DELIMITER_1 = ","
DELIMITER_2 = " " 

def dfs(g, start):

    visited = set()
    stack   = [start]
    
    while stack:

        v = stack.pop() #O(1)

        if v not in visited: #O(1)

            visited.add(v) #0(1)
            stack.extend(g[v] - visited) # O(E)
    
    return visited

def is_connected(g, cds):

    if len(cds):

        induced_subg = {k: set([item for item in v if item in cds]) 
                        for k, v in g.items() if k in cds}
                        # O(V + E)

        k = randint(0, len(cds) - 1)
        v = list(cds)[k]
        seen = dfs(induced_subg, v) # O(V + E)
 
        return True if seen == set(cds) else False   

    else:

        return False

def is_dominating(g, cds, vertices):

    # O(E) O(V)
    if len(cds):

        seen = set()
        seen.update(cds)
        seen.update([vv for v in cds for vv in g[v]])

        return True if seen == set(vertices) else False  

    else:

        return False

def calculate_degree(g):

     deg_g = {v:len(g[v]) for v in g}
   
     #for key in deg_g: print(key +":"+ str(deg_g[key]))

     return deg_g           

def order_vertices(deg_g, vertices, mode):

    ordered_vertices = [(deg_g[v], v) for v in vertices]
    ordered_vertices = sorted(ordered_vertices, key=lambda tup: tup[0])
    ordered_vertices = [v[1] for v in ordered_vertices]

    if mode == 1:

        # ascending order

        return ordered_vertices

    elif mode == 2:

        # descending order

        return ordered_vertices[::-1]

    else:

        # randomized order

        shuffle(ordered_vertices)
        return ordered_vertices

def find_mcds(g, deg_g, vertices):
     
    mcds  = set(vertices) # O(V) O(V) 

    for v in vertices: # O(V) O(V)

        mcds_copy = mcds.copy() # O(V)
        mcds_copy.remove(v) # O(1)

        if is_connected(g, mcds_copy) and is_dominating(g, mcds_copy, vertices): 
            # O(V+E)                            # O(E)
            mcds.remove(v) #O(1)

    mcds = sorted(list(mcds))
    return mcds

if __name__ == "__main__":

    delimiter  = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    graph_data = read_file(sys.argv[1], delimiter)
    g          = create_adj_list(graph_data) 

    start    = timer()
    deg_g    = calculate_degree(g) # T O(V) E O(V)
    vertices = order_vertices(deg_g, g.keys(), int(sys.argv[3])) # T O(Vlog(V) E O(V)
    mcds     = find_mcds(g, deg_g, vertices) # 
    print(mcds, len(mcds))
    # complexity O(VE)
    end = timer() 
    print(end - start)

