import copy

###
# neighbor_branching_search(graph)
# Returns an exact solution to the parameterized problem
# Branches on a node or on its neighbors
# returns whether there is a cover of size k
# and the second element is a list of nodes that cover the graph or None
###
def neighbor_branching_search(graph,k):
    print("k="  +str(k))
    print('edges: ' + str(graph.get_edges_names()))
    if k < 0:
        # More nodes have been removed than the allowable number k
        print('More nodes have been removed than the allowable number k...')
        return False, None
    elif len(graph.get_edges()) == 0:
        # G has no edges
        # Empty set (size 0 <= k) is a cover 
        cover = set()
        print('New cover started: ' + str(cover))
        return True, cover
    elif  k == 0:
        # G has at least one edge
        # G cannot have a cover of size 0
        print('No Cover Found...')
        return False, None
    else:
        # G has at least one edge so at least one node
        # pick a node in G
        node_names = list(graph.get_node_names())
        node_name = node_names[0]
        

        # Branch using the node
        g1 = copy.deepcopy(graph)
        g1.remove_node(node_name)
        print("Branching on node " + node_name)
        r1, c1 = neighbor_branching_search(g1,k-1)
        if r1:
            # Add branch node to the cover
            c1.add(node_name)
            print('added node to cover to get: ' + str(c1))
            return True, c1
        
        # Branch using the neighbors of the node1
        print("Branching on neighbors ")
        node = graph.get_node(node_name)
        neighbor_names = node.get_neighbour_names()
        g2 = copy.deepcopy(graph)
        for neighbor_name in neighbor_names:
            g2.remove_node(neighbor_name)
            print('Neighbor ' + neighbor_name + ' removed')
        num_neighbors = len(neighbor_names)
        r2,c2 = neighbor_branching_search(g2,k-num_neighbors)
        if r2:
            for neighbor_name in neighbor_names:
                c2.add(neighbor_name)
            print('added node to cover to get: ' + str(c2))
            return True, c2
        return False, None

