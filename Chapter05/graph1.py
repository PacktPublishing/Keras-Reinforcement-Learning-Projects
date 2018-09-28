graph = { "a" : ["b", "c", "d", "e", "g"],
         "b" : ["c", "a"],
         "c" : ["a", "b", "d"],
         "d" : ["a", "c", "e"],
         "e" : ["a", "d"],
         "f" : ["g"],
         "g" : ["a", "f"]
        }

def EdgesList(graph):
    edges = []
    for vertex in graph:
        for neighbour in graph[vertex]:
            edges.append((vertex, neighbour))
    return edges

print(EdgesList (graph))
