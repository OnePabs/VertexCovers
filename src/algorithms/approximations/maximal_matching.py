
###
# maximal_matching_search(graph)
# Returns a 2-approximation minimum cover
# Uses maximal matches theorem. Iterates through edges adding non covered ones. 
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def maximal_matching_search(graph):
    cover = set()
    for edge in graph.edges:
        node1 = edge[0]
        node2 = edge[1]
        if (not (node1 in cover)) and (not (node2 in cover)):
            cover.update([node1,node2])
    cover = list(cover)
    size = len(cover)
    return (size, cover)



