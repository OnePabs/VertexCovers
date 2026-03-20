
###
# maximal_matching_search(graph)
# Returns a 2-approximation minimum cover
# Uses maximal matches theorem. Iterates through edges adding non covered ones. 
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def maximal_matching_search(graph):
    cover = set()
    # Go through each edge. If it not already covered add both edge nodes to the cover
    for edge in graph.get_edges():
        if not any(edge_node_name in cover for edge_node_name in edge.get_node_names()):
            cover.update(edge.get_node_names())
    size = len(cover)
    return (size, cover)



