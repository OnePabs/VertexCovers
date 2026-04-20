A selection of exact and approximation vertex cover algorithms implementated in python


# DATA 

The Data of a graph must be of the following format:
Each graph should be stored in its own folder with two files
1. A file called nodes.csv containing a header called nodes and each node as a row 
2. A file called edges.csv containing the headers node1, node2 and each edge as a row


### Example nodes file (3 nodes with edges between each node)

1. create a folder (example name 3_node_circular_graph)
2. In the folder "3_node_circular_graph" create a file called "nodes.csv". The content of the file must be

nodes
1
2
3

3. In the folder "3_node_circular_graph" create a file called "edges.csv". The content of the file must be

node1,node2
1,2
2,3
3,1



# Experiments

An experiment is the script to run a specific algorithm on a specific graph. The experiments are stored under:

VertexCovers/src/experiments

Each experiment has at the top of the file an explanation on how to run it. It usually is

Open a terminal at VertexCovers
cd to src folder
typethe command: python3 -m experiments.name_of_experiment_file_without_extension

Depending on the environment you are running the project on the above command might slightly change (like python instead of python3)


# Results

Results are stored under the folder

VertexCovers/src/experiments/results

Each experiment outputs 3 files 

name_of_experiment_vc-size.csv 
name_of_experiment_cover.csv
name_of_experiment_runtime.txt

The file ending with vc-size.csv contains the size of the vertex cover found by the algorithm on the dataset specified. 
The file ending with cover.csv contains a single column of nodes that make up the vertex cover
The file ending with runtime.txt contains the time in seconds taken for the algorithm to complete. 

### Parameterized Algorithms Results

If no cover of size at most k (parameter) was found then the vc-size.csv file will contain a single zero entry and the cover.csv file will be empty. 


