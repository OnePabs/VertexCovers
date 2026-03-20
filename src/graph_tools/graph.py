from .node import Node
from .edge import Edge

class Graph:

    ### Constructor
    # __init__(self, nodes = None, edges=None)
    # Parameters
    #   node_names: Iterable of Strings representing node names. Each node name needs to be a unique identifier
    #   edges: Iterable of Iterable (String node1_name, String node2_name) representing edges between nodes. 
    #               node1_name and node2_name need to be in node_names
    # Self Variables
    #   self._nodes: a dictionary of nodes with their node_name as the key representing the graph nodes
    #   self._edges: a list of edge objects representing the graph edges
    ###
    def __init__(self, node_names = None, edges=None):
        self._nodes = {}
        self.edges = []
        if not node_names is None and not edges is None:
            # Ensure node_names is an enumerable of Strings
            if not all(isinstance(item, str) for item in node_names):
                raise Exception("Graph Constructor: Not all node names are strings.")
            
            #Ensure edges is an Enumerable of Enumerables of Strings
            if not all(all(isinstance(node_name, str) for node_name in edge)  for edge in edges):
                raise Exception("Graph Constructor: Not all edge node names are strings.")
            
            # Ensure all edges have exactly 2 node names
            if not all(len(edge)==2 for edge in edges):
                raise Exception("Graph Constructor: Not all edge have exactly two node names.")

            # Build dictionary of Nodes
            for node_name in node_names:
                self._nodes[node_name] = Node(node_name)

            # Build list of Edges
            for edge in edges:
                my_iterator = iter(edge)
                self.add_edge(next(my_iterator), next(my_iterator))
            

    ###
    # get_node_names(self)
    # returns a set of all node names of this graph
    ###
    def get_node_names(self):
        return self._nodes.keys()


    ###
    # get_edges(self)
    # Retturns the graph edges dictionary "edge name": Edge(node1_name, node2_name)
    ###
    def get_edges(self):
        return self.edges


    ###
    # add_node(self, node)
    # adds a node to the graph
    # Parameters
    #   node: node object representing the node that is to be added to the graph
    ###
    def add_node(self, node_name):
        if not isinstance(node_name,str):
            raise Exception("Graph add_node(node_name): Expecting node_name to be a string but it is not.")
        if node_name in self._nodes:
            raise Exception("Graph add_node(node_name): node_name is already the name of a node in the graph.")
        
        new_node = Node(node_name)
        self._nodes[node_name] = new_node
    
    ###
    # get_num_nodes()
    # Returns the number of nodes in the graph
    def get_num_nodes(self):
        return len(self._nodes)

    ###
    # add_edge(self, node)
    # adds an edge to the graph
    # Parameters
    #   edge: edge object representing the edge that is to be added to the graph
    ###
    def add_edge(self, node1_name, node2_name):
        if not isinstance(node1_name,str):
            raise Exception("Graph add_edge(node1_name,node2_name): Expecting node1_name to be a string but it is not.")
        if not isinstance(node2_name,str):
            raise Exception("Graph add_edge(node1_name,node2_name): Expecting node2_name to be a string but it is not.")
        if not node1_name in self._nodes:
            raise Exception("Graph add_edge(node1_name,node2_name): node1_name not found in graph node names.")
        if not node2_name in self._nodes:
            raise Exception("Graph add_edge(node1_name,node2_name): node2_name not found in graph node names.")
        #create new edge
        new_edge = Edge(self._nodes[node1_name], self._nodes[node2_name])
        #check if edge already exists
        if new_edge in self.edges:
            raise Exception("Graph add_edge(" + node1_name + "," + node2_name + "): Edge already exists.")
        #add edge to graph edges
        self.edges.append(new_edge)
        return 
    

    ###
    # remove_node(self, node_name)
    # Removes the node node_name and any edge containing it form the graph
    # Parameters
    #   node_name: The name of the node to be removed. 
    ###
    def remove_node(self, node_name):
        if not node_name in self._nodes:
            raise Exception("Graph remove_node(node_name): node_name not in the graph.")
        # delete all edges with node node_name
        for i in range(len(self.edges) - 1, -1, -1):
            if self.edges[i].is_node_in_edge(node_name):
                del self.edges[i]
        # delete the node
        del self._nodes[node_name]


    ###
    # print_structure()
    # Prints the node names and the edge names of the graph
    ###
    def print_structure(self):
        print("Graph Structure")
        print("nodes: ")
        print(self.get_node_names())
        print("Edges: ")
        edges_names = []
        for edge in self.edges:
            edges_names.append(edge.get_name())
        print(edges_names)


