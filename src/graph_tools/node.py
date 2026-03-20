class Node:
    # Represents a Node in a graph

    ### Constructor
    # node_name: String denoting the node name
    # neighbor_names: Iterable of Strings representing the node's neighbors names
    ###
    def __init__(self, node_name, neighbor_names = None):
        self._node_name = node_name 
        self._neighbor_names = set()
        if not neighbor_names is None:
            self.add_neighbors(neighbor_names)
        

    ###
    # get_name(self)
    # Retrives the name of the node instance.
    # returns: String node name
    ###
    def get_name(self):
        return self._node_name


    ### 
    # add_neighbor(neighbor_name, throw_exception_if_already_exists)
    # Adds a neighbor to the node. An exception is raised when neighbor_name is already a neighbor of this node
    # Parameters
    #       neighbor_name: String representing the name of the neighbor node to be added
    ###
    def add_neighbor(self, neighbor_name):
        if not isinstance(neighbor_name, str):
            raise Exception("Node add_neighbor(neighbor_name): neighbor name is not Strings.")
        if neighbor_name in self._neighbor_names:
            raise Exception("Node add_neighbor(neighbor_name): " + neighbor_name + " is already a neighbor of node" + self.get_name() + ".")
        self._neighbor_names.add(neighbor_name)

    ### 
    # add_neighbors(neighbor_name, throw_exception_if_already_exists)
    # Adds neighbors to the node. An exception is raised when neighbor_name is already a neighbor of this node
    # Parameters
    #       neighbor_names: Iterable of Strings representing the names of the neighbors of this node that are to be added
    ###
    def add_neighbors(self, neighbor_names):
        for neighbor_name in neighbor_names:
            self.add_neighbor(neighbor_name)

    ###
    # remove_neighbor(neighbor_name)
    # removes the neighbor neighbor_name from the node's neighbors
    ###
    def remove_neighbor(self, neighbor_name):
        # check if neighbor_name is one of the neighbors
        if not neighbor_name in self._neighbor_names:
            raise Exception("Node does not have a neighbor called " + neighbor_name)
        # remove neighbor
        self._neighbor_names.remove(neighbor_name)


    ### 
    # get_neighbours(self)
    # gets the names of the neighbors of the node instance
    # 
    def get_neighbour_names(self):
        if self._neighbor_names is None:
            raise Exception("Node Neighbors have not been set.")
        return self._neighbor_names
    
    ###
    # clear_neighbour_names()
    # Removes all neighbors of this node
    ###
    def clear_neighbour_names(self):
        self._neighbor_names.clear()

    ###
    # __eq__(self, other)
    # Determines the equality of the instance of a node with another node based solely on node name
    # To know if two nodes are equal we can now do "node1 == node2" where node1 and 2 are instances of the class node
    # other: The second node being compared
    ###
    def __eq__(self, other):
        if isinstance(other,Node):
            return self._node_name == other._node_name
        return False
    
    ###
    # __ne__(self, other)
    # Returns the oposite truth value of __eq__(self, other)
    ###
    def __ne__(self, other):
        return not self.__eq__(other)
    

