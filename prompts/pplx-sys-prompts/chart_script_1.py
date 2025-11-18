
import plotly.graph_objects as go

# Data
categories = ["Clients", "Locations", "Services", "Keywords", "RAG Content"]
values = [6, 100, 50, 40, 618]
labels = ["6 contractors", "100+ cities", "50+ service types", "40+ keyword clusters", "618K chars"]

# Colors from the theme
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C']

# Create horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=categories,
    x=values,
    orientation='h',
    marker=dict(color=colors),
    text=labels,
    textposition='auto',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title="System Data Overview",
    xaxis_title="Records/Items",
    yaxis_title="",
    xaxis=dict(range=[0, 650]),
    showlegend=False
)

# Save as PNG and SVG
fig.write_image("chart.png")
fig.write_image("chart.svg", format="svg")
