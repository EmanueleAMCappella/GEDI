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
                  (5, {'pos': [9.5, 8], 'text':'Upselling&Cross-selling'}),
                  (6, {'pos': [7, 9.5], 'text':'User Clustering'}),
                  (7, {'pos': [2, 10.5], 'text':'Dynamic Paywall'}),
                  (8, {'pos': [3, 15], 'text':'Ottimizzazione'}),
                  (9, {'pos': [6.5, 16], 'text':'Scenario Analysis'}),
                  (10, {'pos': [13, 10], 'text':'Customer Journey'}),
                  (11, {'pos': [9.5, 11.5], 'text':'NBA per Acquisition'}),
                  (12, {'pos': [11, 14], 'text':'NBA per CC'}),
                  (13, {'pos': [14, 15], 'text':'Cost Forecast'}),
                  (14, {'pos': [16, 17], 'text':'Smart Closing'}),
                  (15, {'pos': [17, 15], 'text':'Revenue Forecast'}),
                  (16, {'pos': [18, 12.5], 'text':'Churn'}),
                  (17, {'pos': [17, 10], 'text':'Personalizzazione Offerta'}),
                  (18, {'pos': [11, 3], 'text':'Social Curation'}),
                  (19, {'pos': [13, 5], 'text':'Social Alert'}),
                  (20, {'pos': [15.5, 7.5], 'text':'Smart Archive'}),
                  (21, {'pos': [19, 5], 'text':'Reality Bridge'}),
                  (22, {'pos': [16, 4], 'text':'Ticket AutoRouting'}),
                  (23, {'pos': [15, 2], 'text':'Content Tagging'})
                  ])

P.add_edges_from([(3, 6), (4, 6), (5, 6), (7, 6), (8, 6), (9, 6), (8, 9),
                  (10, 6), (10, 11), (10, 12), (10, 13), (10, 15), (10, 16), (10, 17), (13, 14), (14, 15)])

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
    text= labels,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='Greens',
        reversescale=True,
        color=[],
        size=20, #aumenta dimensioni del punto
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
                title='<br>Relationship between GEDI Use Cases',
                titlefont_size=20,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

# aggiungi etichetta
figP.add_trace(go.Scatter(
    x=P_node_x,
    y=P_node_y,
    mode="text",
    name="Markers and Text",
    text=["UA01", "UA02", "UA03", "UA04", "UA05", "UA06", "UA07", "UA08", "UA09", "UA10",
          "UA11", "UA012", "UA13", "UA14", "UA15", "UA16", "UA17", "UA18", "UA19", "UA20", "UA21", "UA22", "UA23"],
    textposition="top left",
    textfont_size=16
))



figP.write_html(path)

# figP.show()
P.clear()


