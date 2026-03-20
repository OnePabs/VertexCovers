class Edge:
    # Represents an edge in a graph
    
    ### Constructor
    # __init__(self, node1, node2)
    # Creates the edge theoretically represented by (node1,node2) which is the same as (node2,node1)
    # node1: Instance of class node 
    # node2: Instance of class node
    ###
    def __init__(self, node1, node2):
        self.nodes = {node1.get_name():node1, node2.get_name():node1}
        node_names = sorted([node1.get_name(), node2.get_name()])
        self.edge_name = "_".join(node_names)

    ###
    # get_name(self)
    # Returns the uniquely determined name (String) of the edge created by placing the name of the 
    # two nodes in alphabetical order and placing a "_" character in between node names
    ###
    def get_name(self):
        return self.edge_name
    
    ###
    # get_nodes()
    # Returns the edge nodes objects as a dictionary "node_name": Node Object
    ###
    def get_nodes(self):
        return self.nodes
    
    ###
    # get_node_names
    # Returns an iterable of the name of the nodes in the edge
    ###
    def get_node_names(self):
        return self.nodes.keys()

    ###
    # is_node_in_edge(self, node_name)
    # Determines if a node is part of the edge using the node name
    # Parameters:
    # node_name: String representing the node name
    # returns:
    # true if the node is part of the edge
    # false otherwise 
    ###
    def is_node_in_edge(self, node_name):
        return node_name in self.nodes
    
    ###
    # __eq__(self, other)
    # Determines the equality of the instance of an edge with another edge based solely on edge name
    # To know if two edges are equal we can now do "edge1 == edge2" where edge1 and edge2 are instances of the class edge
    # other: The second edge being compared
    ###
    def __eq__(self, other):
        if isinstance(other,Edge):
            return self.edge_name == other.edge_name
        return False
    
    ###
    # __ne__(self, other)
    # Returns the oposite truth value of __eq__(self, other)
    ###
    def __ne__(self, other):
        return not self.__eq__(other)



### TESTING ###

# from Node import Node

# node1 = Node("node1")
# node2 = Node("node2")
# edge_1_2 = Edge(node1, node2)
# print(edge_1_2.get_name())
# print(edge_1_2.is_node_in_edge(node1.get_name()))


# node3 = Node("node3")
# node4 = Node("node4")
# edge_3_4 = Edge(node3, node4)

# s = ""
# if edge_1_2 != edge_3_4:
#     s = "not "
# print("edge_1_2 and edge_3_4 are " + s + "equal")


# node5 = Node("node1")
# node6 = Node("node2")
# edge_5_6 = Edge(node5, node6)
# s = ""
# if edge_1_2 != edge_5_6:
#     s = "not "
# print("edge_1_2 and edge_5_6 are " + s + "equal")

