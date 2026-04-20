########################################################
# to run:
# 1. activate conda environment 
# 2. cd to the src folder
# 3. run "python3 -m experiments.bn-human_lp_relaxation"
########################################################

from algorithms.approximations.relaxed_lp import relaxed_lp_search
from graph_tools.approx_graph_loader import approx_load_graph
from pathlib import Path
import time

print('bn-human LP Relaxation Experiment')

# Construct the path to the graph data file
src_dir = Path(__file__).parent.parent.parent
current_script_dir = Path(__file__).parent

nodes_csv_path = src_dir / 'data' / 'bn-human' / 'nodes.csv'
edges_csv_path = src_dir / 'data' / 'bn-human' / 'edges.csv'

# Load the Graph
g = approx_load_graph(nodes_csv_path, edges_csv_path)

# LP Relaxation approximation (Use Pulp since no licence for Gurobi)
print('Starting LP Relaxation search...')
start_time = time.perf_counter()
res = relaxed_lp_search(g, batch_size=500000, solver = 'pulp_batching', max_iter=10,max_mem_gb=3.5)
end_time = time.perf_counter()
running_time = end_time - start_time
print("Total LP Relaxation search runtime: " + str(running_time))

cover_size = res[0]
cover = res[1]
print('LP Relaxation Vertex Cover Size: ' + str(cover_size))


results_size_path = current_script_dir / 'results' / 'bn-human_lp_relaxation_result_size.csv'
with open(results_size_path, "w") as file:
    file.write("cover_size\n")
    file.write(str(cover_size))

results_cover_path = current_script_dir / 'results' / 'bn-human_lp_relaxation_result_cover.csv'
cover.to_csv(results_cover_path, index=False)

time_path = current_script_dir / 'results' / 'bn-human_lp_relaxation_runtime.txt'
with open(time_path, "w") as file:
    file.write("runtime\n")
    file.write(str(running_time))

print('bn-human LP Relaxation experiment over')