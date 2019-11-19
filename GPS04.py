def find_all_paths(self, start_vertex, end_vertex, path=[]):
    graph = self.__graph_dict
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = self.find_all_paths(vertex,
                                                 end_vertex,
                                                 path)
            for p in extended_paths:
                paths.append(p)
    return paths