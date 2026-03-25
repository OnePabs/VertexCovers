

###
# struction(graph, node_name)
# Graph operation Struction as described in Chen, Kanj, and Xia 's 2010 paper
# Parameters
#       graph: object of type src/graph_tools/graph Graph
#       node_name: String representing the node name the Struction operation is done to
#       name_separator: String. When a new node is created from 2 old nodes the new 
#                       node name is old_node_name1 + name_separator + old_node_name2 
#                       where the old node names are sorted in alphabetical order.
###
def struction(graph, node_name, name_separator = "-"):
    if not isinstance(node_name,str):
        raise Exception("Expecting node_name to be a string but it is not.")
    
    ## Step 1 ##
    # Create a list of all node names in N[node_name] = {v \in V: v is a neighbor of node_name or v is node_name}
    node = graph.get_node(node_name)
    neighbor_names = node.get_neighbour_names()
    node_and_neighbor_names = list(neighbor_names)
    node_and_neighbor_names.append(node_name)
    # For every anti-edge (vi,vj) add node vij
    new_nodes_names_and_origin_indeces = []
    p = len(node_and_neighbor_names)
    for i in range(p):
        for j in range(i+1,p):
            if not graph.is_edge_in_graph(node_and_neighbor_names[i],node_and_neighbor_names[j]):
                #(vi,vj) is an anti-edge
                new_node_name = struction_create_new_node_name(node_and_neighbor_names[i],node_and_neighbor_names[j],name_separator)
                new_nodes_names_and_origin_indeces.append({"name": new_node_name, "indeces":(i,j)})
                graph.add_node(new_node_name)

    ## Step 2 and 3 ##
    for idx in range(len(new_nodes_names_and_origin_indeces)):
        v_ir = new_nodes_names_and_origin_indeces[idx]["name"]
        v_ir_ideces = new_nodes_names_and_origin_indeces[idx]["indeces"]
        for idx2 in range(idx+1,len(new_nodes_names_and_origin_indeces)):
            v_js = new_nodes_names_and_origin_indeces[idx2]["name"]
            v_js_ideces = new_nodes_names_and_origin_indeces[idx2]["indeces"]
            if (
                v_ir_ideces[0] != v_js_ideces[0] # i != j
                or 
                (v_ir_ideces[0] == v_js_ideces[0]          # i=j
                and v_ir_ideces[1] != v_js_ideces[1]      # r != s
                and graph.is_edge_in_graph(node_and_neighbor_names[v_ir_ideces[1]], node_and_neighbor_names[v_js_ideces[1]])  # (v_r,v_s) is an edge
                )):
                # add edge (v_ir,v_js)
                graph.add_edge(v_ir,v_js)

    ## Step 4 ##
    for u in graph.get_node_names():
        if not u in node_and_neighbor_names:
            for idx in range(len(new_nodes_names_and_origin_indeces)):
                v_ij = new_nodes_names_and_origin_indeces[idx]["name"]
                v_ij_ideces = new_nodes_names_and_origin_indeces[idx]["indeces"]
                if (graph.is_edge_in_graph(node_and_neighbor_names[v_ij_ideces[0]],u)
                    or graph.is_edge_in_graph(node_and_neighbor_names[v_ij_ideces[1]],u)
                    ):
                    # add edge (vij,u)
                    graph.add_edge(v_ij,u)

    # Remove node_name and neighbor_names from the graph
    for v in node_and_neighbor_names:
        graph.remove_node(v)
    



def struction_create_new_node_name(node1_name, node2_name, name_separator):
    sorted_strings = sorted([node1_name, node2_name])
    return sorted_strings[0] + name_separator + sorted_strings[1]







