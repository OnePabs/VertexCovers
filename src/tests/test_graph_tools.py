from graph_tools.graph import Graph

## Testing Constructor ##
print("Test Constructor")
# Create the graph with no constructor parameters
print("Constructor with No parameters")
g = Graph()
g.print_structure()
print()
# Create the graph from a list of node names and a list of edge tuples
print("Constructor valid parameters")
node_names = ["1", "2", "3", "4"]
edges = [("1", "2"), ("2", "3"), ("3", "4"), ("4", "1")]
g = Graph(node_names = node_names, edges = edges)
g.print_structure()
print()


## Test add_node ##
print("Test add_node")
# Valid input: add node 5
print("Valid input: add node 5")
g.add_node("5")
g.print_structure()
# Invalid Input: Node name already in the graph
print("Invalid Input: add_node 5 - Node name is already in the graph")
try:
    g.add_node("5")
except Exception as e:
    print(e)
# Invalid Input: Node name is not a string
print("Invalid Input: Node name is not a string")
try:
    g.add_node([])
except Exception as e:
    print(e)
print()


## Test add_edge ##
print("Test add_edge")
# Valid input: add (5,1)
print("Valid input:  add (5,1)")
g.add_edge("5","1")
g.print_structure()
print()


## Test remove_node ##
print("Test remove_node")
# Valid input: remove node 1
print("Valid input:  remove node 1")
g.remove_node("1")
g.print_structure()







