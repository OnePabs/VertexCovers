from algorithms.exact_solutions.chen_kanj_xia_2010 import struction
from graph_tools.graph import Graph


print("TEST STRUCTION")

# Test 1
test_num = 1
node_names = ["v0", "v1", "v2", "v3","t","w","x","y","z"]
edges = [("v0", "v1"), ("v0", "v2"), ("v0", "v3"), ("v1", "v2"), ("v1", "t"), ("v1", "w"), ("v2", "x"), ("v3", "y"), ("v3", "z")]
g = Graph(node_names = node_names, edges = edges)
struction(g,"v0")
# Expected Results:
expected_nodes = ["v1-v3", "v2-v3", "t", "w", "x", "y", "z"]
expected_edges = ["v1-v3_v2-v3", "t_v1-v3", "v1-v3_w", "v1-v3_y", "v1-v3_z", "v2-v3_x", "v2-v3_y", "v2-v3_z"]
# Check Results
if (all(expected_node in g.get_node_names() for expected_node in expected_nodes) 
    and all(actual_node in expected_nodes for actual_node in g.get_node_names())
    and all(expected_edge in g.get_edges_names() for expected_edge in expected_edges)
    and all(actual_edge in expected_edges for actual_edge in g.get_edges_names())
    ):
    print("TEST " + str(test_num) + " STRUCTION: Pass")
else:
    print("TEST " + str(test_num) + " STRUCTION: FAIL")


# Test 2
test_num = 2
node_names = ["v0", "v1", "v2", "v3", "v4", "r", "s", "t","w","x","y","z"]
edges = [("v0", "v1"), ("v0", "v2"), ("v0", "v3"), ("v0","v4"), ("v1", "v2"), ("v1","v3"), ("v3","v4"), ("v1", "r"), ("v2","s"), ("v2","t"), ("v3","w"), ("v4","x"), ("v4","y"),("v4","z")]
g = Graph(node_names = node_names, edges = edges)
struction(g,"v0")
# Expected Results:
expected_nodes = ["v1-v4", "v2-v3", "v2-v4", "r", "s", "t", "w", "x", "y", "z"]
expected_edges = [ "v1-v4_v2-v3", "v1-v4_v2-v4", "r_v1-v4", "v1-v4_x", "v1-v4_y", "v1-v4_z",
                   "v2-v3_v2-v4", "s_v2-v3", "t_v2-v3", "v2-v3_w",
                   "s_v2-v4", "t_v2-v4", "v2-v4_x", "v2-v4_y", "v2-v4_z"
                  
                  ]
# Check Results
if (all(expected_node in g.get_node_names() for expected_node in expected_nodes) 
    and all(actual_node in expected_nodes for actual_node in g.get_node_names())
    and all(expected_edge in g.get_edges_names() for expected_edge in expected_edges)
    and all(actual_edge in expected_edges for actual_edge in g.get_edges_names())
    ):
    print("TEST " + str(test_num) + " STRUCTION: Pass")
else:
    print("TEST " + str(test_num) + " STRUCTION: FAIL")


