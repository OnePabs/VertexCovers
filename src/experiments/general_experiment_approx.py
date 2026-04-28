from algorithms.approximations.maximal_matching import maximal_matching_search
from algorithms.approximations.pitt_randomized import pitt_randomized_search
from algorithms.approximations.relaxed_lp import relaxed_lp_search_pulp
from algorithms.approximations.MMRRLPb import mmrrlpb_search
from graph_tools.approx_graph_loader import approx_load_graph
from pathlib import Path
import time


def general_experiment_approx(data_folder_path, results_folder_path, algorithm_name, batch_size, max_mem_gb):

    # Construct the path to the graph data files and result files (first done in case of errors)
    data_folder_path = Path(data_folder_path)
    nodes_csv_path = data_folder_path / "nodes.csv"
    edges_csv_path = data_folder_path / "edges.csv"

    results_folder_path = Path(results_folder_path)
    res_vc_size_filepath = results_folder_path / 'vc-size.csv'
    res_cover_filepath = results_folder_path / 'cover.csv'
    res_runtime_filepath = results_folder_path / 'runtime.csv'

    # Load the graph
    g = approx_load_graph(nodes_csv_path, edges_csv_path)

    # get algorithm function
    if algorithm_name == "maximal_matching":
        alg = maximal_matching_search
    elif algorithm_name == "pitt":
        alg = pitt_randomized_search
    elif algorithm_name == "relaxed_lp":
        alg = relaxed_lp_search_pulp
    elif algorithm_name == "mmrrlpb":
         alg = mmrrlpb_search
    else:
        raise Exception("Algorithm Name NOT FOUND")

    # Run algorithm on graph
    start_time = time.perf_counter()
    res = alg(g, batch_size=batch_size, max_mem_gb=max_mem_gb)
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print("Total Algorithm search runtime: " + str(running_time))

    # Store cover and cover size in internal variables
    cover_size = res[0]
    cover = res[1]
    print('Algorithm Cover Size: ' + str(cover_size))

    # Write results to files
    with open(res_vc_size_filepath, "w") as file:
        file.write("cover_size\n")
        file.write(str(cover_size))

    cover.to_csv(res_cover_filepath, index=False)

    with open(res_runtime_filepath, "w") as file:
        file.write("runtime\n")
        file.write(str(running_time))

    return

