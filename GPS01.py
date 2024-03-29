class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    g = {"Rahat": ["Rahat"],
         "b": ["Rahat"],
         "c": ["Rahat", "BeerSheva", "SegevShaloam", "Eilat"],
         "d": ["Rahat", "Rahat"],
         "e": ["Rahat"],
         "f": ["Rahat"]
         }

    graph = Graph(g)

    print("DISTINATIONS001:")
    print(graph.vertices())

    print("DISTINATIONS002:")
    print(graph.edges())
    #
    # print("Add vertex:")
    # graph.add_vertex("z")
    #
    # print("Vertices of graph:")
    # print(graph.vertices())
    #
    # print("Add an edge:")
    # graph.add_edge({"a", "z"})
    #
    # print("Vertices of graph:")
    # print(graph.vertices())
    #
    # print("Edges of graph:")
    # print(graph.edges())
    #
    # print('Adding an edge {"x","y"} with new vertices:')
    # graph.add_edge({"x", "y"})
    # print("Vertices of graph:")
    # print(graph.vertices())
    # print("Edges of graph:")
    # print(graph.edges())