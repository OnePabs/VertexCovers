import numpy as np
import pandas as pd
import random
import time
from ..limit_resources import kill_if_max_memory_exceeded
from ..limit_resources import get_mem_left_gb
import os



#################################
#### Gurobipy Implementation ####
#################################

# import gurobipy as gp
# from gurobipy import GRB


# ###
# # relaxed_lp_search(graph)
# # Returns a 2-approximation minimum cover using constraint generation
# # Uses the Gurobi linear programming relaxation method.
# # returns a tuple where the first element is the size of the cover
# # and the second element is a list of nodes that cover the graph
# ###
# def relaxed_lp_search_gurobi(graph, batch_size):
#     n = graph.num_nodes
    
#     model = gp.Model()
#     model.setParam("OutputFlag", 0)

#     # Variables
#     x = model.addVars(graph.node_names_df["nodes"], lb=0, ub=1, name="")

#     # Objective
#     model.setObjective(gp.quicksum(x[row[0]] for row in graph.get_node_names_iterator()), GRB.MINIMIZE)

#     #### constraint generation ####
#     #### (otherwise too slow)  ####

#     # Get a maximal matching
#     matched = np.zeros(graph.num_nodes, dtype=bool)
#     truth_edges_in_maximal_matching = np.zeros(graph.num_edges, dtype=bool)
#     idx = 0
#     # Go through each edge. If it is not already covered add both edge nodes to the cover and add edge to maximal matching
#     for edge in graph.get_edges_iterator():
#         node1_id = graph.nodes_ids[edge[0]]
#         node2_id = graph.nodes_ids[edge[1]]
#         if not matched[node1_id] and not matched[node2_id]:
#             matched[node1_id] = True
#             matched[node2_id] = True
#             truth_edges_in_maximal_matching[idx] = True 
#         idx = idx + 1
#     # Get the indices of the edges in the maximal matching as the active edges indices
#     active_edges_idx = np.where(truth_edges_in_maximal_matching)[0]
#     initial_size = active_edges_idx.size

#     # Add constraints from edges in maximal matching
#     for idx in active_edges_idx:
#         row = graph.edges_df.iloc[idx]
#         u = row['node1']
#         v = row['node2']
#         model.addConstr(x[u] + x[v] >= 1)

#     # Loop solving LP and then adding constraints
#     iteration = 0
#     violated_truths = np.zeros(graph.num_edges, dtype=bool)
#     while True:
#         iteration += 1
#         print(f"Iteration {iteration}, constraints: {active_edges_idx.size}")

#         model.optimize()

#         # Get solution
#         x_val = model.getAttr("x", x)

#         # Find violated constraints
#         violated_truths.fill(False)
#         idx = 0
#         for edge in graph.get_edges_iterator():
#             if idx not in active_edges_idx:
#                 u = edge[0]
#                 v = edge[1]
#                 if x_val[u] + x_val[v] < 1 - 1e-6:
#                     violated_truths[idx] = True
#             idx = idx + 1

#         num_violated_constraints = np.sum(violated_truths)
#         print(f"Violated constraints found: {num_violated_constraints}")

#         if num_violated_constraints == 0:
#             break

#         # Add a batch (avoid adding millions at once so that the solver can solve in adequate time)
#         violated_indices = np.where(violated_truths)[0]
#         for idx in violated_indices[:batch_size]:
#             row = graph.edges_df.iloc[idx]
#             u = row['node1']
#             v = row['node2']
#             model.addConstr(x[u] + x[v] >= 1)
#         active_edges_idx = np.concatenate((active_edges_idx,violated_indices))


#     # Get the list of nodes that lead to the optimized value
#     cover = [k for k,v in x.items() if v.X >= 0.5]
#     size = len(cover)

#     return (size,cover)



#############################
#### Pulp Implementation ####
#############################

import pulp

def relaxed_lp_search_pulp(graph, batch_size=500000,  max_mem_gb=4):
    print('Relaxed LP Search with PuLP')
    pid = os.getpid()

    # create new model
    model = pulp.LpProblem("MyModel", pulp.LpMinimize)
    
    # Variables
    print('Setting variables ...')
    var_name_prefix = "node_name"
    start_time = time.perf_counter()
    x = pulp.LpVariable.dicts(var_name_prefix, graph.node_names_df["nodes"], lowBound=0, upBound=1, cat='Continuous')
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('variables set in runtime ' + str(running_time) + ' seconds')

    # Objective
    print('Setting objective ...')
    start_time = time.perf_counter()
    model += pulp.lpSum(x.values()), "Total_Sum_Objective"
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('objective set in runtime '  + str(running_time) + ' seconds' )

    # Add constraints from edges in maximal matching
    print('Adding constraints...')
    batch_itr = 0
    for edge in graph.get_edges_iterator():
        batch_itr = batch_itr + 1
        if batch_itr >= batch_size:
            # Check amount of memory used
            # Kill current process if it exceeds max memory limits
            kill_if_max_memory_exceeded(pid,max_mem_gb)
            batch_itr = 0
        node1_name = edge[0]
        node2_name = edge[1]
        model += x[node1_name] + x[node2_name] >= 1
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Added constraints in runtime '  + str(running_time) + ' seconds' )

    # Check amount of memory left
    kill_if_max_memory_exceeded(pid,max_mem_gb)
    # mem_left = get_mem_left_gb(pid,max_mem_gb)

    # solve model
    # CBC DOES NOT have a memory check fla :(  
    print('solving model...')
    solver = pulp.PULP_CBC_CMD(msg=False)
    start_time = time.perf_counter()
    model.solve(solver)
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Model solved in '  + str(running_time) + ' seconds')

    # Get the list of nodes that lead to the optimized value
    cover = [v.name[len(var_name_prefix)+1:] for v in model.variables() if v.varValue >= 0.5]
    cover_df = pd.DataFrame(cover, columns=['nodes'])
    size = len(cover)

    print('Finished Relaxed LP Search with PuLP')
    return (size,cover_df)





###
# relaxed_lp_search(graph)
# Returns a 2-approximation minimum cover
# Uses the Pulp linear programming relaxation method. 
# Uses looped Constraint generation but Pulp Rebuilds the model each time
#   Builds the model once with the constraints from a maximal matching and solves.
#   Builds the model a second time with all constraints 
#   and sets inital variable values to the ones found 
#   in the first iteration for more efficient solving. Then solves a second time
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def relaxed_lp_search_pulp_batching(graph, batch_size=500000,  max_iter=100, max_mem_gb=4):
    model = pulp.LpProblem("MyModel", pulp.LpMinimize)
    
    # Variables
    print('Setting variables ...')
    var_name_prefix = "node_name"
    start_time = time.perf_counter()
    x = pulp.LpVariable.dicts(var_name_prefix, graph.node_names_df["nodes"], lowBound=0, upBound=1, cat='Continuous')
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('variables set in runtime ' + str(running_time) + ' seconds')

    # Objective
    print('Setting objective ...')
    start_time = time.perf_counter()
    model += pulp.lpSum(x.values()), "Total_Sum_Objective"
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('objective set in runtime '  + str(running_time) + ' seconds' )

    # Use Maximal Matching for warm start

    # Get a maximal matching
    print('Getting Maximal Matching ...')
    matched = np.zeros(graph.num_nodes, dtype=bool)
    truth_edges_in_maximal_matching = np.zeros(graph.num_edges, dtype=bool)
    idx = 0
    # Go through each edge. If it is not already covered add both edge nodes to the cover and add edge to maximal matching
    for edge in graph.get_edges_iterator():
        node1_id = graph.nodes_ids[edge[0]]
        node2_id = graph.nodes_ids[edge[1]]
        if not matched[node1_id] and not matched[node2_id]:
            matched[node1_id] = True
            matched[node2_id] = True
            truth_edges_in_maximal_matching[idx] = True 
        idx = idx + 1
    # Get the indices of the edges in the maximal matching as the active edges indices
    active_edges_idx = np.where(truth_edges_in_maximal_matching)[0]
    initial_size = active_edges_idx.size
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Got maximal matching of size ' + str(initial_size) + ' in runtime '  + str(running_time) + ' seconds' )

    # Add constraints from edges in maximal matching
    print('Adding Maximal Matching constraints...')
    for idx in active_edges_idx:
        row = graph.edges_df.iloc[idx]
        u = row['node1']
        v = row['node2']
        model += x[u] + x[v] >= 1
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print('Added maximal matching constraints in runtime '  + str(running_time) + ' seconds' )

    # Loop:
    #   Optimize the model
    #   Find violated Constraints and add a batch of them to the model
    # Stop either when there are no more violated Constraints or when 
    # max_iter iterations have been done
    # Process is killed if it reaches max memory usage
    violated_truths = np.zeros(graph.num_edges, dtype=bool)
    warmStart = False
    pid = os.getpid()
    for iteration in range(max_iter):
        print('Iteration: ' + str(iteration))

        # Kill current process if it exceeds max memory limits
        kill_if_max_memory_exceeded(pid,max_mem_gb)

        # Set initial variable values
        if warmStart:
            for var in model.variables():
                var.setInitialValue(var.varValue)

        # solve model
        print('solving model using maximal matching constraints...')
        solver = pulp.PULP_CBC_CMD(warmStart=warmStart,msg=False)
        start_time = time.perf_counter()
        model.solve(solver)
        end_time = time.perf_counter()
        running_time = end_time - start_time
        print('Model solved in '  + str(running_time) + ' seconds')

        # Set warmStart to True so that following iterations start with a 'good guess'
        warmStart = True

        # Find at most 'batch size' violated constraints
        print('Finding violated constraints...')
        start_time = time.perf_counter()
        violated_truths.fill(False)
        idx = 0
        num_violated_constraints = 0
        for edge in graph.get_edges_iterator():
            if idx not in active_edges_idx:
                u = edge[0]
                v = edge[1]
                if x[u].varValue + x[v].varValue < 1 - 1e-6:
                    violated_truths[idx] = True
                    num_violated_constraints = num_violated_constraints + 1
                    # break if max number of violated constraints found
                    if num_violated_constraints >= batch_size:
                        print('number of violated constraints found reached batch size threshold...')
                        break 
            idx = idx + 1
        end_time = time.perf_counter()
        running_time = end_time - start_time
        print(f"Violated constraints found: {num_violated_constraints} in {running_time} seconds")

        # Break if no constraints are violated
        if num_violated_constraints == 0:
            break
        else:
            # There are violated constraints
            # If this was the last iteration raise error
            if iteration == max_iter - 1:
                raise Exception("Pulp LP Relaxation Search FAIL")

            # Add a batch of violated constraints
            print('Adding batch of violated constraints...')
            start_time = time.perf_counter()
            violated_indices = np.where(violated_truths)[0]
            for idx in violated_indices:
                row = graph.edges_df.iloc[idx]
                u = row['node1']
                v = row['node2']
                model += x[u] + x[v] >= 1
            active_edges_idx = np.concatenate((active_edges_idx,violated_indices))
            end_time = time.perf_counter()
            running_time = end_time - start_time
            print(f"Added batch of violated constraints in {running_time} seconds")

    
    # Get the list of nodes that lead to the optimized value
    cover = [v.name[len(var_name_prefix)+1:] for v in model.variables() if v.varValue >= 0.5]
    cover_df = pd.DataFrame(cover, columns=['nodes'])
    size = len(cover)

    return (size,cover_df)


