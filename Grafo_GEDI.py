import plotly.graph_objects as go
import networkx as nx

# inserire percorso
path = "C:/Users/ECappella/OneDrive - Bip/Desktop/prova_grafo_1.html"

P = nx.Graph()
P.add_nodes_from([
                  (1, {'pos': [2, 4], 'text':'Chatbot'}),
                  (2, {'pos': [4, 3], 'text':'IVR'}),
                  (3, {'pos': [2, 7], 'text':'Upselling&Cross-selling'}),
                  (4, {'pos': [6.5, 7], 'text':'Dynamic Adv'}),
                  (5, {'pos': [9.5, 8], 'text':'Dynamic Paywall'}),
                  (6, {'pos': [7, 9.5], 'text':'User Clustering'}),
                  (7, {'pos': [2, 10.5], 'text':'Augmented Search'}),
                  (8, {'pos': [3, 15], 'text':'Ottimizzazione'}),
                  (9, {'pos': [5.5, 15], 'text':'Scenario Analysis'}),
                  (10, {'pos': [13, 10], 'text':'Customer Journey'}),
                  (11, {'pos': [9.5, 11.5], 'text':'NBA per Acquisition'}),
                  (12, {'pos': [11, 14], 'text':'NBA per CC'}),
                  (13, {'pos': [14, 15], 'text':'Cost Forecast'}),
                  (14, {'pos': [16, 17], 'text':'Smart Closing'}),
                  (15, {'pos': [17, 15], 'text':'Revenue Forecast'}),
                  (16, {'pos': [18, 12.5], 'text':'Churn'}),
                  (17, {'pos': [4.5, 17], 'text':'Personalizzazione Offerta'}),
                  (18, {'pos': [11, 3], 'text':'Social Curation'}),
                  (19, {'pos': [13, 5], 'text':'Social Alert'}),
                  (20, {'pos': [15.5, 7.5], 'text':'Smart Archive'}),
                  (21, {'pos': [19, 5], 'text':'Reality Bridge'}),
                  (22, {'pos': [16, 4], 'text':'Ticket AutoRouting'}),
                  (23, {'pos': [15, 2], 'text':'Content Tagging'})
                  ])

P.add_edges_from([(3, 6), (4, 6), (5, 6), (7, 6), (8, 6), (9, 6), (8, 9),
                  (10, 6), (10, 11), (10, 12), (10, 13), (10, 15), (10, 16), (10, 17), (13, 14), (14, 15),
                  (8, 17), (9, 17)])

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
    line=dict(width=1, color='black'),
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
    text=labels,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale= 'YlGnBu', #'Greens',
        reversescale=True,
        color=[],
        size=20,  # aumenta dimensioni del punto
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))

# valore di adiacenza per gestire il colore
node_adjacencies = []
for node, adjacencies in enumerate(P.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))

P_node_trace.marker.color = node_adjacencies

# metti insieme in figura plotly tutti gli elementi
figP = go.Figure(data=[edge_traceP, P_node_trace],
             layout=go.Layout(
                title='<br>Relationship between GEDI Use Cases',
                titlefont_size=24,
                showlegend=False,
                hovermode='closest',
                # margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=True, zeroline=False, showticklabels=False),  # showgrid=False se vuoi eliminarla...
                yaxis=dict(showgrid=True, zeroline=False, showticklabels=False))
                )

# aggiungi etichetta
# https://plotly.com/python/text-and-annotations/
figP.add_trace(go.Scatter(
    x=[x+0.35 for x in P_node_x],  # sposta un pò in alto le etichette
    y=[x+0.35 for x in P_node_y],
    mode="text",
    name="Text",
    text=["UA01-A", "UA01-B", "UA03", "UA05", "UA06", "UA09", "UA18", "UA07", "UA12", "UA10",
          "UA11", "UA022", "UA13", "UA21", "UA08", "UA04", "UA27", "UA19", "UA25", "UA15", "UA17", "UA29", "UA20"],
    textposition="top left",
    textfont={"color": "Black", "family": "Arial", "size": 16}
))


# aggiungi una singola freccia, questa è la funzione da utilizzare:
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edges.html

# scrivi file html
figP.write_html(path)

P.clear()


