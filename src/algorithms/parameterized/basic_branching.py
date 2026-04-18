import copy

###
# basic_branching_search(graph)
# Returns an exact solution to the parameterized problem
# Brnaches on the nodes of an edge (one branch for each of the two nodes)
# returns whether there is a cover of size k
# and the second element is a list of nodes that cover the graph or None
###
def basic_branching_search(graph,k):
    print("k="  +str(k))
    print('edges: ' + str(graph.get_edges_names()))
    if len(graph.get_edges()) == 0:
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
        # pick an edge (u,v) in G
        e = graph.get_first_edge()
        node_names = list(e.get_node_names())

        # Branch using the first Node
        n1 = node_names[0]
        g1 = copy.deepcopy(graph)
        g1.remove_node(n1)
        print("Branching on node " + n1)
        r1, c1 = basic_branching_search(g1,k-1)
        if r1:
            # Add branch node to the cover
            c1.add(n1)
            print('added node to cover to get: ' + str(c1))
            return True, c1
        
        # Branch using the second node
        n2 = node_names[1]
        g2 = copy.deepcopy(graph)
        g2.remove_node(n2)
        print("Branching on node " + n2)
        r2,c2 = basic_branching_search(g2,k-1)
        if r2:
            c2.add(n2)
            print('added node to cover to get: ' + str(c2))
            return True, c2
        return False, None

