import itertools

###
# exhaustive_search(graph)
# Returns a list of the minimum vertex covers of the graph. 
# Uses exhaustive search (checks every subset of vertices to see if they cover the graph)
###
def exhaustive_search(graph):
    
    # Get all subsets of graph nodes
    all_nodes_subsets = []
    for r in range(graph.get_num_nodes() + 1):
        subset = itertools.combinations(graph.get_node_names(), r)
        all_nodes_subsets.append(subset)
    all_nodes_subsets = list(itertools.chain.from_iterable(all_nodes_subsets))
    
    # Check each subset to see if it is a cover
    covers = []
    for nodes_subset in all_nodes_subsets:
        is_cover = True
        # Check each edge to see if at least one node in the edge is in the nodes_subset
        for edge in graph.get_edges():
            if not any(edge_node_name in nodes_subset for edge_node_name in edge.get_node_names()):
                # Edge is not covered
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
