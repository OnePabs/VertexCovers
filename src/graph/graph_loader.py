import pandas as pd
from graph import Graph

def load_graph(nodes_filepath, edges_filepath):
    nodes_df = pd.read_csv(nodes_filepath)
    nodes = nodes_df['nodes'].tolist()

    edges_df = pd.read_csv(edges_filepath)
    num_edges = len(edges_df)
    nodes_1 = edges_df['node1'].tolist()
    nodes_2 = edges_df['node2'].tolist()

    edges = []
    for i in range(num_edges):
        new_edge = (nodes_1[i], nodes_2[i])
        edges.append(new_edge)
    
    g = Graph(nodes, edges)
    return g
