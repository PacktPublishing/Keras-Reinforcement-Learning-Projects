import networkx as nx
import matplotlib.pyplot as plt 

G = nx.Graph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('G')
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('A', 'D')
G.add_edge('A', 'E')
G.add_edge('A', 'G')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('F', 'G')

nx.draw(G,with_labels=True, font_weight='bold')
plt.show() 
