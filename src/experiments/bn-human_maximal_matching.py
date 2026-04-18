########################################################
# to run:
# 1. activate conda environment 
# 2. cd to the src folder
# 3. run "python3 -m experiments.bn-human_maximal_matching"
########################################################

from algorithms.approximations.maximal_matching import maximal_matching_search
from graph_tools.approx_graph_loader import approx_load_graph
from pathlib import Path
import time




# Construct the path to the graph data file
src_dir = Path(__file__).parent.parent.parent
current_script_dir = Path(__file__).parent

nodes_csv_path = src_dir / 'data' / 'bn-human' / 'nodes.csv'
edges_csv_path = src_dir / 'data' / 'bn-human' / 'edges.csv'


# Load the Graph
g = approx_load_graph(nodes_csv_path, edges_csv_path)

# Maximal Matching approximation
start_time = time.perf_counter()
res = maximal_matching_search(g)
end_time = time.perf_counter()
running_time = end_time - start_time
print("Running time: " + str(running_time))

cover_size = res[0]
cover = res[1]
print('Maximal Matching Vertex Cover Size: ' + str(cover_size))


results_size_path = current_script_dir / 'results' / 'bn-human_maximal_matching_result_size.csv'
with open(results_size_path, "w") as file:
    file.write("cover_size\n")
    file.write(str(cover_size))

results_cover_path = current_script_dir / 'results' / 'bn-human_maximal_matching_result_cover.csv'
cover.to_csv(results_cover_path, index=False)

time_path = current_script_dir / 'results' / 'bn-human_maximal_matching_runtime.txt'
with open(time_path, "w") as file:
    file.write("runtime\n")
    file.write(str(running_time))

