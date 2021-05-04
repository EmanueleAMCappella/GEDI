import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

# risorse
# https://towardsdatascience.com/tutorial-network-visualization-basics-with-networkx-and-plotly-and-a-little-nlp-57c9bbb55bb9
# https://plotly.com/python/network-graphs/
# https://dash.plotly.com/cytoscape

# 1. grafo di test con matplotlib
Q = nx.Graph()
Q.add_nodes_from([1, 2, 3, 4])
Q.add_edges_from([(1, 2), (1, 3), (2, 3), (1, 4)])
nx.draw(Q, pos={1: [0.556, 0.189], 2: [0.3, 0.43], 3: [0.70, 0.2], 4: [0.3, 0.5]}, with_labels=True, font_weight='bold')



# 2. grafo di prova con plotly

# inserire percorso
path = "C:/Users/ECappella/OneDrive - Bip/Desktop/prova_grafo_1.html"

P = nx.Graph()
P.add_nodes_from([(1, {'pos': [0.856, 0.6], 'text':'Daje'}), (2, {'pos': [0.3, 0.43], 'text':'tutta'}),
                  (3, {'pos': [0.70, 0.2], 'text':'Forza'}), (4, {'pos': [0.3, 0.5], 'text':'lupacchiotti'})])
P.add_edges_from([(1, 2), (1, 3), (2, 3), (1, 4)])

# parsing coordinate degli edge
P_edge_x = []
P_edge_y = []
for P_edge in P.edges():
    Px0, Py0 = P.nodes[P_edge[0]]['pos']
    Px1, Py1 = P.nodes[P_edge[1]]['pos']
    P_edge_x.append(Px0)
    P_edge_x.append(Px1)
    P_edge_x.append(None)
    P_edge_y.append(Py0)
    P_edge_y.append(Py1)
    P_edge_y.append(None)

# e ora le plotti
edge_traceP = go.Scatter(
    x=P_edge_x, y=P_edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')


# parsing coordinate dei nodes x e y
P_node_x = [P.nodes[node]['pos'][0] for node in P.nodes()]
P_node_y = [P.nodes[node]['pos'][1] for node in P.nodes()]

# parsing delle etichette
labels = [P.nodes[node]['text'] for node in P.nodes()]

# e ora plotti i nodi, con le etichette in hovering
P_node_trace = go.Scatter(
    x=P_node_x, y=P_node_y,
    text= labels,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale= 'Greens',#'YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))


# valore di adiacenza per gestire il colore
node_adjacencies = []
#node_text = []
for node, adjacencies in enumerate(P.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    #node_text.append('# of connections: '+str(len(adjacencies[1])))

P_node_trace.marker.color = node_adjacencies
#node_trace.text = node_text


# metti insieme in figura plotly tutti gli elementi
figP = go.Figure(data=[edge_traceP, P_node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

# aggiungi etichetta
# https://plotly.com/python/text-and-annotations/
figP.add_trace(go.Scatter(
    x=P_node_x,
    y=P_node_y,
    mode="text",
    name="Markers and Text",
    text=["Daje", "tutta", "forza", "Lupacchiotti"],
    textposition="bottom center"
))


figP.write_html(path)

# figP.show()
P.clear()


