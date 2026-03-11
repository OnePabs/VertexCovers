import itertools

###
# exhaustive_search(graph)
# Returns a list of the minimum vertex covers of the graph. 
# Uses exhaustive search (checks every subset of vertices to see if they cover the graph)
###
def exhaustive_search(graph):
    
    # Get all subsets of graph nodes
    all_nodes_subsets = []
    for  r in range(len(graph.nodes) + 1):
        subset = itertools.combinations(graph.nodes, r)
        all_nodes_subsets.append(subset)
    all_nodes_subsets = list(itertools.chain.from_iterable(all_nodes_subsets))
    
    # Check each subset to see if it is a cover
    covers = []
    for nodes_subset in all_nodes_subsets:
        is_cover = True
        for edge in graph.edges:
            is_either_edge_node_in_subset = False
            for edge_node in edge:
                for node in nodes_subset:
                    if node == edge_node:
                        is_either_edge_node_in_subset = True
                        break
                if is_either_edge_node_in_subset:
                    break
            
            if not is_either_edge_node_in_subset:
                is_cover = False
                break
        if is_cover:
            size = len(nodes_subset)
            covers.append((size, nodes_subset))

    covers.sort()

    #get the minimum covers
    min_covers = []
    min_size = covers[0][0]
    for cover in covers:
        if cover[0] == min_size:
            min_covers.append(cover)
        else:
            break 

    return min_covers
