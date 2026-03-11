from graph import Graph, load_graph
from algorithms.exhaustive import exhaustive_search
from pathlib import Path



# Construct the path to the graph data file
current_script_dir = Path(__file__).parent
nodes_csv_path = current_script_dir / '..' / 'data' / 'star' / '3_star' / 'nodes.csv'
edges_csv_path = current_script_dir / '..' / 'data' / 'star' / '3_star' / 'edges.csv'

# Load the Graph
g = load_graph(nodes_csv_path, edges_csv_path)

# Perform the vertex cover algorithm
res = exhaustive_search(g)
print(res)

