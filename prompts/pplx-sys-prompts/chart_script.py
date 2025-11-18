
import plotly.graph_objects as go
import networkx as nx

# Create a directed graph for the flowchart
G = nx.DiGraph()

# Define nodes with their positions (using manual layout for better control)
nodes = {
    'User Input': (0, 5),
    'Context Builder': (0, 4),
    'Load Client Data': (-3, 2.5),
    'Load Location Data': (-1, 2.5),
    'Load Service Data': (1, 2.5),
    'Extract RAG Content': (3, 2.5),
    'Merge Context': (0, 1),
    'Fill Prompt Template': (0, -0.5),
    'LLM Generation API': (0, -2),
    'Quality Control': (0, -3.5),
    'Output & Export': (0, -5)
}

# Add nodes with positions
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

# Define edges
edges = [
    ('User Input', 'Context Builder'),
    ('Context Builder', 'Load Client Data'),
    ('Context Builder', 'Load Location Data'),
    ('Context Builder', 'Load Service Data'),
    ('Context Builder', 'Extract RAG Content'),
    ('Load Client Data', 'Merge Context'),
    ('Load Location Data', 'Merge Context'),
    ('Load Service Data', 'Merge Context'),
    ('Extract RAG Content', 'Merge Context'),
    ('Merge Context', 'Fill Prompt Template'),
    ('Fill Prompt Template', 'LLM Generation API'),
    ('LLM Generation API', 'Quality Control'),
    ('Quality Control', 'Output & Export')
]

G.add_edges_from(edges)

# Get positions
pos = nx.get_node_attributes(G, 'pos')

# Create edge traces
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=2, color='#5D878F'),
    hoverinfo='none',
    mode='lines'
)

# Define node colors by category
node_colors = {
    'User Input': '#B3E5EC',
    'Context Builder': '#FFEB8A',
    'Load Client Data': '#A5D6A7',
    'Load Location Data': '#A5D6A7',
    'Load Service Data': '#A5D6A7',
    'Extract RAG Content': '#FFEB8A',
    'Merge Context': '#FFEB8A',
    'Fill Prompt Template': '#FFEB8A',
    'LLM Generation API': '#FFCDD2',
    'Quality Control': '#9FA8B0',
    'Output & Export': '#B3E5EC'
}

# Create node traces
node_x = []
node_y = []
node_text = []
node_color = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
    node_color.append(node_colors[node])

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=node_text,
    textposition="middle center",
    textfont=dict(size=10, color='#13343B', family='Arial Black'),
    hoverinfo='text',
    marker=dict(
        size=50,
        color=node_color,
        line=dict(width=2, color='#13343B')
    )
)

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace])

fig.update_layout(
    title='Content Generation Process',
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor='white',
    hovermode='closest'
)

# Save the figure
fig.write_image('content_generation_flow.png')
fig.write_image('content_generation_flow.svg', format='svg')

print("Flowchart created and saved successfully!")
