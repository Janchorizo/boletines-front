'''Sankey diagram for the diary entry flow by section and department.'''
import collections
# External
import dash_core_components as dcc
import plotly.graph_objects as go
# Internal
import helpers


def diary_entry_sankey(data):
    fig = go.Figure( 
        data=[go.Sankey(
            arrangement='fixed',
            hoverinfo='skip',
            node = dict( 
                label = data['labels']
            ),
            link = dict(
                source=data['link_source'],
                target=data['link_target'],
                value=data['link_value'],
                color='#d7dfff'

            ))])
    fig.update_layout(
    margin=dict(l=10, r=10, t=25, b=10),
    paper_bgcolor='#f8f9fa',
    autosize=True,
    #width=850,
    #height=900,
    )

    return dcc.Graph(
        style={'height': '100%'},
        figure=fig
    )
