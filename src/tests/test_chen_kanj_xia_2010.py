from algorithms.exact_solutions.chen_kanj_xia_2010 import struction
from algorithms.exact_solutions.chen_kanj_xia_2010 import general_folding
from graph_tools.graph import Graph


print("TEST STRUCTION")
func_name = "struction"

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
    print(func_name + " TEST " + str(test_num) + ": Pass")
else:
    print("TEST " + str(test_num) + " STRUCTION: FAIL")
    #g.print_structure()


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
    print(func_name + " TEST " + str(test_num) + ": Pass")
else:
    print(func_name + " TEST " + str(test_num) + " FAIL")
    #g.print_structure()



print("TEST general_folding")
func_name = "general_folding"

# Test 1
test_num = 1
node_names = ["u", "v", "w", "v1", "v2", "w1", "w2"]
edges = [("u", "v"), ("u", "w"), ("v", "v1"), ("v","v2") ,("w","w1"), ("w","w2")]
g = Graph(node_names = node_names, edges = edges)
I = ["u"]
general_folding(g,I)
# Expected Results:
expected_nodes = ["gf.u", "v1", "v2", "w1", "w2"]
expected_edges = ["gf.u_v1", "gf.u_v2", "gf.u_w1", "gf.u_w2"]
# Check Results
if (all(expected_node in g.get_node_names() for expected_node in expected_nodes) 
    and all(actual_node in expected_nodes for actual_node in g.get_node_names())
    and all(expected_edge in g.get_edges_names() for expected_edge in expected_edges)
    and all(actual_edge in expected_edges for actual_edge in g.get_edges_names())
    ):
    print(func_name + " TEST " + str(test_num) + ": Pass")
else:
    print(func_name + " TEST " + str(test_num) + " FAIL")
    #g.print_structure()


# Test 2
test_num = 2
node_names = ["u", "v", "w", "r", "s", "t", "z", "r1", "r2", "r3", "s1", "t1", "t2", "z1", "z2"]
edges = [
        ("u","r"), ("u","s"), ("u","t"),
        ("v","r"), ("v","s"), ("v","z"),
        ("w","s"), ("w","t"), ("w","z"),
        ("r","r1"), ("r","r2"), ("r","r3"),
        ("s","s1"),
        ("t","t1"), ("t","t2"),
        ("z","z1"), ("z","z2")
        ]
g = Graph(node_names = node_names, edges = edges)
I = ["u","v","w"]
general_folding(g,I)
# Expected Results:
expected_nodes = ["gf.u.v.w", "r1", "r2", "r3", "s1", "t1", "t2", "z1", "z2"]
expected_edges = ["gf.u.v.w_r1", "gf.u.v.w_r2", "gf.u.v.w_r3", "gf.u.v.w_s1", "gf.u.v.w_t1", "gf.u.v.w_t2", "gf.u.v.w_z1", "gf.u.v.w_z2"]
# Check Results
if (all(expected_node in g.get_node_names() for expected_node in expected_nodes) 
    and all(actual_node in expected_nodes for actual_node in g.get_node_names())
    and all(expected_edge in g.get_edges_names() for expected_edge in expected_edges)
    and all(actual_edge in expected_edges for actual_edge in g.get_edges_names())
    ):
    print(func_name + " TEST " + str(test_num) + ": Pass")
else:
    print(func_name + " TEST " + str(test_num) + " FAIL")
    #g.print_structure()