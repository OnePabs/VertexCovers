import numpy as np
import pandas as pd
import pulp
import random
import time
from ..limit_resources import kill_if_max_memory_exceeded
from ..limit_resources import get_mem_left_gb
import os




def mmrrlpb_search(graph, batch_size=500000,  max_mem_gb=4):
    print("MMRRLPb Search")
    pid = os.getpid()

    #--- Perform Maximal Matching ---#
    print("Finding Maximal Matching...")
    start_time = time.perf_counter()
    # Create numpy arrays
    edges_in_maximal_matching_truth =  np.zeros(graph.num_edges, dtype=bool)  # True means that the edge at the index is in the maximal matching
    nodes_in_maximal_matching_truth = np.zeros(graph.num_nodes, dtype=bool)   # True means the node at the index is an endpoint to an edge in the maximal matching
    # Go through each edge. If it is not already covered add edge to edges_in_maximal_matching 
    # and edge endpoints to nodes_in_maximal_matching
    edges_idx = 0
    for edge in graph.get_edges_iterator():
        node1_id = graph.nodes_ids[edge[0]]
        node2_id = graph.nodes_ids[edge[1]]
        if not nodes_in_maximal_matching_truth[node1_id] and not nodes_in_maximal_matching_truth[node2_id]:
            edges_in_maximal_matching_truth[edges_idx] = True 
            nodes_in_maximal_matching_truth[node1_id] = True
            nodes_in_maximal_matching_truth[node2_id] = True
        edges_idx += 1
    # Get the indices of the edges that are included in the matching
    indices_of_edges_in_maximal_matching = np.where(edges_in_maximal_matching_truth)[0]
    # Get edges in maximal matching
    maximal_matching_edges = graph.edges_df.iloc[indices_of_edges_in_maximal_matching]
    # Get the indices of the vertices that are included in the matching
    indices_of_nodes_in_maximal_matching = np.where(nodes_in_maximal_matching_truth)[0]
    # Get the nodes in the maximal matching
    maximal_matching_node_names_df = graph.node_names_df.iloc[indices_of_nodes_in_maximal_matching]
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Maximal Matching found in ' + str(running_time) + ' seconds')


    #--- Reduce using Relaxed Linear Programming ---#
    print("Starting Reduction by Linear Programing Relaxation...")
    # Apply linear programming relaxation to graph induced by maximal matching
    model = pulp.LpProblem("MyModel", pulp.LpMinimize)
    ### Variables
    # vertices in the maximal matching
    print('Setting variables ...')
    var_name_prefix = "node_name"
    start_time = time.perf_counter()
    x = pulp.LpVariable.dicts(var_name_prefix, maximal_matching_node_names_df['nodes'], lowBound=0, upBound=1, cat='Continuous')
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('variables set in runtime ' + str(running_time) + ' seconds')
    ### Objective
    print('Setting objective ...')
    start_time = time.perf_counter()
    model += pulp.lpSum(x.values()), "Total_Sum_Objective"
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('objective set in runtime '  + str(running_time) + ' seconds' )
    ### Add constraints from edges in maximal matching
    print('Adding constraints from maximal matching...')
    start_time = time.perf_counter()
    for edge in maximal_matching_edges.itertuples():
        # edge is in maximal matching
        node1_name = edge.node1
        node2_name = edge.node2
        model += x[node1_name] + x[node2_name] >= 1
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Added constraints in runtime '  + str(running_time) + ' seconds' )
    ### Relaxed LP Iterations
    print("Starting Relaxed LP Iterations...")
    itr = 0
    is_violated = True
    while is_violated:
        # There are still some edges being violated 
        print("Iteration: " + str(itr))
        itr += 1
        ### Solve model
        print('solving model...')
        solver = pulp.PULP_CBC_CMD(msg=False)
        start_time = time.perf_counter()
        model.solve(solver)
        end_time = time.perf_counter()
        running_time = end_time - start_time
        print('Model solved in '  + str(running_time) + ' seconds')
        ### Get potential cover 
        potential_cover_names = {v.name[len(var_name_prefix)+1:] for v in model.variables() if v.varValue >= 0.5}
        ### check for violated constraints
        print("Looking for violated constraints...")
        num_node_names_added_as_constraints = 0
        is_violated = False
        for edge in graph.edges_df.itertuples():
            node1_name = edge.node1
            node2_name = edge.node2
            if  node1_name not in potential_cover_names and node2_name not in potential_cover_names:
                # print("edge violation found: " + str(edge))
                # edge is not covered
                # Exactly one of the endpoints must be in the maximal matching (at least one because it is a maximal matching and at most one because all edges in maximal matching are covered)
                # Find the endpoint in the maximal matching
                # Find if node 1 is in the maximal matching
                node_1_idx = graph.nodes_ids[node1_name]
                if nodes_in_maximal_matching_truth[node_1_idx]:
                    # Add the constraint that the first node must be in the cover. 
                    model += x[node1_name] == 1
                    potential_cover_names.add(node1_name)   # add node name to potential cover so that further violated edges with the same node do not get processed and add the constraint again
                else:
                    # The second node must be in the maximal matching so add it as a constraint
                    model += x[node2_name] == 1
                    potential_cover_names.add(node2_name)   # add node name to potential cover so that further violated edges with the same node do not get processed and add the constraint again
                is_violated = True
                if num_node_names_added_as_constraints >= batch_size: # ensure only up to batch_size number of nodes are added as constraints. 
                    break
                num_node_names_added_as_constraints += 1
        if is_violated:
            print("Number of nodes added as constraints: " + str(num_node_names_added_as_constraints))
    print("All Constraints satisfied...")
    print("Creating return data structures...")
    # Get Cover
    cover = list(potential_cover_names)
    cover_df = pd.DataFrame(cover, columns=['nodes'])
    size = len(cover)
    print("End of MMRRLPb search")
    return (size, cover_df)
