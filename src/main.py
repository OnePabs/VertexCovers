from graph import Graph, load_graph
from algorithms.exact_solutions.exhaustive import exhaustive_search
from algorithms.approximations.maximal_matching import maximal_matching_search
from algorithms.approximations.pitt_randomized import pitt_randomized_search
from algorithms.approximations.relaxed_lp import relaxed_lp_search
from pathlib import Path



# Construct the path to the graph data file
current_script_dir = Path(__file__).parent
nodes_csv_path = current_script_dir / '..' / 'data' / 'star' / '3_star' / 'nodes.csv'
edges_csv_path = current_script_dir / '..' / 'data' / 'star' / '3_star' / 'edges.csv'

# Load the Graph
g = load_graph(nodes_csv_path, edges_csv_path)

# Exhaustive search
all_res = exhaustive_search(g)
min_vc = all_res[0][0]
print('Result of the Exhaustive Search: ')
print('Minimum Vertex Cover Size: ' + str(min_vc))
print('Covers of that size: ')
print(all_res)
print()

# Maximal Matching approximation
res = maximal_matching_search(g)
cover_size = res[0]
cover = res[1]
print('Result of Maximal Matching: ')
print('Vertex Cover Size: ' + str(cover_size))
print('Cover: ')
print(cover)
print()

# Pitt's Randomized approximation
res = pitt_randomized_search(g)
cover_size = res[0]
cover = res[1]
print('Result of Pitt\'s Ranommized Search: ')
print('Vertex Cover Size: ' + str(cover_size))
print('Cover: ')
print(cover)
print()

#Relaxed LP approximation
res = relaxed_lp_search(g)
cover_size = res[0]
cover = res[1]
print('Result of Relaxed LP Search: ')
print('Vertex Cover Size: ' + str(cover_size))
print('Cover: ')
print(cover)
print()



