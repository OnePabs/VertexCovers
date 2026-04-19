import gurobipy as gp
from gurobipy import GRB
import numpy as np
import random

###
# relaxed_lp_search(graph)
# Returns a 2-approximation minimum cover using constraint generation
# Uses the Gurobi linear programming relaxation method.
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def relaxed_lp_search(graph, batch_size=500000):
    n = graph.num_nodes
    
    model = gp.Model()
    model.setParam("OutputFlag", 0)

    # Variables
    x = model.addVars(graph.node_names_df["nodes"], lb=0, ub=1, name="")

    # Objective
    model.setObjective(gp.quicksum(x[row[0]] for row in graph.get_node_names_iterator()), GRB.MINIMIZE)

    ###############################
    #### constraint generation ####
    #### (otherwise too slow)  ####
    ###############################

    # Get a maximal matching
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

    #m = len(edges)

    # Add constraints from edges in maximal matching
    for idx in active_edges_idx:
        row = graph.edges_df.iloc[idx]
        u = row['node1']
        v = row['node2']
        model.addConstr(x[u] + x[v] >= 1)

    # Loop solving LP and then adding constraints
    iteration = 0
    violated_truths = np.zeros(graph.num_edges, dtype=bool)
    while True:
        iteration += 1
        print(f"Iteration {iteration}, constraints: {active_edges_idx.size}")

        model.optimize()

        # Get solution
        x_val = model.getAttr("x", x)

        # Find violated constraints
        violated_truths.fill(False)
        idx = 0
        for edge in graph.get_edges_iterator():
            if idx not in active_edges_idx:
                u = edge[0]
                v = edge[1]
                if x_val[u] + x_val[v] < 1 - 1e-6:
                    violated_truths[idx] = True
            idx = idx + 1

        num_violated_constraints = np.sum(violated_truths)
        print(f"Violated constraints found: {num_violated_constraints}")

        if num_violated_constraints == 0:
            break

        # Add a batch (avoid adding millions at once so that the solver can solve in adequate time)
        violated_indices = np.where(violated_truths)[0]
        for idx in violated_indices[:batch_size]:
            row = graph.edges_df.iloc[idx]
            u = row['node1']
            v = row['node2']
            model.addConstr(x[u] + x[v] >= 1)
        active_edges_idx = np.concatenate((active_edges_idx,violated_indices))


    # Get the list of nodes that lead to the optimized value
    cover = [k for k,v in x.items() if v.X >= 0.5]
    size = len(cover)

    return (size,cover)


