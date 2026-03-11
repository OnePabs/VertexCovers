class Graph:

    def __init__(self):
        self.nodes = []     # list of node names
        self.edges = []     # list of tuples (node1,node2) representing edges

    def __init__(self, nodes, edges):
        self.nodes = nodes  # list of node names
        self.edges = edges  # list of tuples (node1,node2) representing edges


    def get_nodes(self):
        return self.nodes
    

    def get_edges(self):
        return self.edges

    def add_node(self, node_name):
        self.nodes.append(node_name)
        return

    def add_edge(self, node1, node2):
        edge = (node1, node2)
        self.edges.append(edge)
        return 