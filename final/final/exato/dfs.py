# -*- coding: utf-8 -*-

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

graph = {'A': set(['B', 'E']),
         'B': set(['A']),
         'C': set(['D', 'F']),
         'D': set(['C', 'F']),
         'E': set(['A']),
         'F': set(['C', 'F'])}

tp = set(['A','B','C','D'])
new_graph = {k: set([item for item in v if item in tp]) for k, v in graph.items() if k in tp}
print(new_graph)
print(tp)
print(dfs(new_graph, 'C'))
