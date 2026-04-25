import random
import numpy as np
from ..limit_resources import kill_if_max_memory_exceeded
import os

###
# pitt_randomized_search(graph)
# Returns a 2-approximation minimum cover
# Uses maximal matches theorem. Iterates through edges adding non covered ones. 
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def pitt_randomized_search(graph, seed = 0, batch_size=500000, max_mem_gb=4):
    random.seed(seed) 
    matched = np.array([False]*graph.num_nodes)

    # Go through each edge. If it not already covered add a random edge node to the cover
    pid = os.getpid()
    itr = 0
    for edge in graph.get_edges_iterator():
        itr = itr + 1
        if itr >= batch_size:
            # Check amount of memory used
            # Kill current process if it exceeds max memory limits
            kill_if_max_memory_exceeded(pid,max_mem_gb)
            itr = 0
        node1_id = graph.nodes_ids[edge[0]]
        node2_id = graph.nodes_ids[edge[1]]
        if not matched[node1_id] and not matched[node2_id]:
            choices = [node1_id,node2_id]
            choice = random.choice(choices)
            matched[choice] = True
    
    # Get the indices of the vertices that are included in the matching
    indices = np.where(matched)[0]
    #Get the size of the cover
    size = len(indices)
    # Get the cover
    cover = graph.get_nodes_from_indices(indices)
    return (size, cover)


