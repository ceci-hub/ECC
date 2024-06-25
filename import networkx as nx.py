import networkx as nx
import json

# Load your GEXF file
G = nx.read_gexf('C:\Users\cecir\Desktop\ecc\RED_INT_TEST.gexf')

# Convert to JSON
data = nx.node_link_data(G)
with open('graph.json', 'w') as f:
    json.dump(data, f)
