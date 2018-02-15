# -*- coding: utf-8 -*-

def read_file(file_name, delimiter):
    
    file_end = '0,0'

    input_file = open(file_name, "r").read().splitlines()
    
    graph_data = []

    for line in input_file: 

        if line == file_end: 

            break

        else:  

            graph_data.append(tuple(line.split(delimiter)))

    else:       
        
        import sys
        sys.exit("Arquivo de entrada inválido")
    
    return graph_data

def create_adj_list(graph_data):

    graph_dict = {}

    for data in graph_data:
        
        if data[0] not in graph_dict:  
      
            graph_dict[data[0]] = set()
            graph_dict[data[0]].add(data[1])            

            if data[1] not in graph_dict: 

                graph_dict[data[1]] = set()
                graph_dict[data[1]].add(data[0])

            else:

                graph_dict[data[1]].add(data[0])

        else:
        
            graph_dict[data[0]].add(data[1])

            if data[1] not in graph_dict:

                graph_dict[data[1]] = set() 
                graph_dict[data[1]].add(data[0])

            else:

                graph_dict[data[1]].add(data[0])
    
    return graph_dict  
