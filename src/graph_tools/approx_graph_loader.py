import pandas as pd
from graph_tools.approx_graph import ApproxGraph


def approx_load_graph(nodes_filepath, edges_filepath):
    node_names_df = pd.read_csv(nodes_filepath, dtype={'nodes': 'string'}, index_col=False)
    edges_df = pd.read_csv(edges_filepath, dtype=pd.StringDtype(), index_col=False)
    
    g = ApproxGraph(node_names_df, edges_df)
    return g