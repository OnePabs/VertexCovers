

class ApproxGraph:

    ####
    # __init__(self, node_names, edges)
    # Parameters
    # node_names_df: Pandas Dataframe with one column called nodes. Type is String
    # edges_df: Pandas dataframe with columns node1name, node2name
    #
    # Variables stored in Graph
    # node_names: a reference to the node_names pandas data
    # edges: a reference to the edges pandas data
    # nodes_ids: A dictionary mapping nodes to their numerical ids
    # 
    # 
    ####
    def __init__(self, node_names_df, edges_df):
        self.node_names_df = node_names_df
        self.num_nodes = len(node_names_df)
        self.edges_df = edges_df
        self.num_edges = len(edges_df)
        self.nodes_ids = {}
        node_id = 0
        for node_name_row in node_names_df.itertuples(index=False):
            self.nodes_ids[node_name_row[0]] = node_id
            node_id = node_id + 1

    ####
    #
    #
    ####
    def get_edges_iterator(self):
        return self.edges_df.itertuples(index=False)


    ####
    #
    #
    ####
    def get_nodes_from_indices(self, indices):
        return self.node_names_df.iloc[indices]
    
        
