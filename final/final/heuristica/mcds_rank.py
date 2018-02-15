# -*- coding: utf-8 -*-

# Autor: Mauricio de Oliveira (mauricioliveira_@hotmail.com)
# Universidade Federal de Minas Gerais
# Departamento de Ciência da Computação

import sys
import bisect
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

        v = stack.pop()

        if v not in visited:

            visited.add(v)
            stack.extend(g[v] - visited)
    
    return visited

def is_connected(g, cds):

    if len(cds):

        induced_subg = {k: set([item for item in v if item in cds]) 
                        for k, v in g.items() if k in cds}

        k = randint(0, len(cds) - 1)
        v = list(cds)[k]
        seen = dfs(induced_subg, v)
 
        return True if seen == set(cds) else False   

    else:

        return False

def is_dominating(g, cds, vertices):

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

def order_vertices(deg_g, g, mode):

    ordered_vertices = []

    for v in g.keys():
        
        uniq_coef = sum([deg_g[vv] for vv in g[v]])
        bisect.insort_left(ordered_vertices, ((float(deg_g[v])/uniq_coef), v))
        print(v, float(deg_g[v]), uniq_coef)
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
     
    mcds  = set(vertices)
    watch = list()

    for v in vertices:

        mcds_copy = mcds.copy()
        mcds_copy.remove(v)

        if is_connected(g, mcds_copy) and is_dominating(g, mcds_copy, vertices): 
                
            mcds.remove(v)
            watch.append(v)

    mcds = sorted(list(mcds))
    return mcds, watch

if __name__ == "__main__":

    delimiter  = DELIMITER_1 if sys.argv[2] == "1" else DELIMITER_2
    graph_data = read_file(sys.argv[1], delimiter)
    g          = create_adj_list(graph_data)

    start    = timer()
    deg_g    = calculate_degree(g)
    vertices = order_vertices(deg_g, g, int(sys.argv[3]))
    print(vertices, deg_g)
    mcds     = find_mcds(g, deg_g, vertices)
    print("mcds")
    print(mcds[0], len(mcds[0]))
    #print("vertices")
    #print(vertices)
    #print("ordem")
    #print(mcds[1], len(mcds[1]))        
    end = timer() 
    print(end - start)

