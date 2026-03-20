class Node:
    # Represents a Node in a graph

    ### Constructor
    # node_name: String denoting the node name
    ###
    def __init__(self, node_name, neighbor_names = None):
        self.node_name = node_name
        self.neighbor_names = neighbor_names

    ###
    # get_name(self)
    # Retrives the name of the node instance.
    # returns: String node name
    ###
    def get_name(self):
        return self.node_name


    ###
    # set_neighbours(self, neighbor_names)
    # stores the neighbors of the node instance 
    # neighbor_names: a set of Strings, each string representing a neighbor name.
    ###
    def set_neighbours(self, neighbor_names):
        self.neighbor_names = neighbor_names


    ### 
    # get_neighbours(self)
    # gets the names of the neighbors of the node instance
    # 
    def get_neighbours(self):
        if self.neighbor_names is None:
            raise Exception("Node Neighbors have not been set.")
        return self.neighbor_names
    

    ###
    # __eq__(self, other)
    # Determines the equality of the instance of a node with another node based solely on node name
    # To know if two nodes are equal we can now do "node1 == node2" where node1 and 2 are instances of the class node
    # other: The second node being compared
    ###
    def __eq__(self, other):
        if isinstance(other,Node):
            return self.node_name == other.node_name
        return False
    
    ###
    # __ne__(self, other)
    # Returns the oposite truth value of __eq__(self, other)
    ###
    def __ne__(self, other):
        return not self.__eq__(other)
    

