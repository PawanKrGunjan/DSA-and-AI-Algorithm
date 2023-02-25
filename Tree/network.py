import networkx as nx
import random
import matplotlib.pyplot as plt
import math

G = nx.complete_graph(5)
for (u,v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,10)

plt.figure(figsize=(7,7))
nx.draw(G, with_labels=True)
plt.show()