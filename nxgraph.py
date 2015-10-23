import networkx as nx
import pandas as pd
from networkx.readwrite import json_graph
import json
import os


rootdir = '/Users/Raghav/Desktop/cf-viz/data/csv_data/'

for files in os.walk(rootdir):
	for f in files:
		matching1 = [s for s in f if 'ge.csv' in s]
		matching2 = [s for s in f if 'de.csv' in s]
		

for i,j in zip(matching1,matching2):
	G = nx.Graph()

	edges = pd.read_csv('data/csv_data/' + i)
	nodes = pd.read_csv('data/csv_data/' + j)

	nodes_list = nodes.values.tolist()
	edges_list = edges.values.tolist()

	for a in nodes_list:
		G.add_node(a[1], name=a[2])
	for b in edges_list:
		G.add_edge(b[1],b[2],value=b[3])

	js = json_graph.node_link_data(G)
	jso = json.dumps(js,indent=4)
	with open('data/json_data/'+i+'.json','w') as file:
		file.write(jso)
