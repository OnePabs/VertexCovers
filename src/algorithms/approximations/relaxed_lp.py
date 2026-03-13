import pulp as lp

###
# relaxed_lp_search(graph)
# Returns a 2-approximation minimum cover
# Uses the linear programming relaxation method.
# returns a tuple where the first element is the size of the cover
# and the second element is a list of nodes that cover the graph
###
def relaxed_lp_search(graph, verbose=True):

    # Initialize PuLP Model
    prob = lp.LpProblem("MinVertexCoverLPRelaxation", lp.LpMinimize)


    # Define Decision Variables (continuous between 0.0 and 1.0)
    x = {name: lp.LpVariable(name, lowBound=0.0, upBound=1.0, cat=lp.LpContinuous) for name in graph.get_nodes()}
    
    #lp.LpVariable.dicts("x", graph.get_nodes(), lowBound=0.0, upBound=1.0, cat=lp.LpContinuous)

    # Define Objective Function:
    # Minimize the sum of selected vertices
    prob += lp.lpSum([x[v] for v in graph.get_nodes()]), "Total_Weight_of_Vertex_Cover"

    # Define Constraints:
    # For every edge (u, v), the sum of their variables must be >= 1
    for u, v in graph.get_edges():
        prob += x[u] + x[v] >= 1, f"Edge_Cover_{u}_{v}"

    # Solve Model
    lp.LpSolverDefault.msg = 0
    prob.solve()

    # Print Status to know if everything went well
    if verbose:
        print(f"relaxed_lp_search Solver Status: {lp.LpStatus[prob.status]}")

    # Get the list of nodes that lead to the optimized value
    cover = []
    for var in prob.variables():
        if var.value() >= 0.5:
            cover.append(var.name)
    
    #get size of cover
    size = len(cover)

    # Check if this agrees with solver's result 
    objective = int(lp.value(prob.objective))
    if size != objective:
        print("ERROR: RELAXED LP cover size does not match objective")

    return (size, cover)


    



