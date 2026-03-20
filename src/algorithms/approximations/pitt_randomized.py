import random

###
# pitt_randomized_search(graph)
# Returns a 2-approximation minimum cover
# Uses maximal matches theorem. Iterates through edges adding non covered ones. 
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def pitt_randomized_search(graph, seed = 0):
    random.seed(seed) 
    cover = set()
    for edge in graph.get_edges():
        if not any(edge_node_name in cover for edge_node_name in edge.get_node_names()):
            choices = list(edge.get_node_names())
            choice = random.choice(choices)
            cover.add(choice)
    size = len(cover)
    return (size, cover)

