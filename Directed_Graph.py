import plotly.graph_objects as go
import networkx as nx


# inserire percorso
path = "C:/Users/ECappella/OneDrive - Bip/Desktop/prova_grafo_1.html"

# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edges.html
# https://networkx.org/documentation/stable/reference/classes/digraph.html

G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3)])
arcs = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))

# e ora le plotti
edge_traceP = go.Scatter(
    x=[1,1,2], y=[2,1,3],
    line=dict(width=1, color='black'),
    hoverinfo='none',
    mode='lines')