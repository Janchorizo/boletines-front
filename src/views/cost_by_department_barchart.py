'''Economic cost by department barchart.'''
import locale
# External
import dash_core_components as dcc
import plotly.express as px


def cost_by_department_barchart(data):
    barchart = px.bar(
        x = data['x'],
        y = data['y'],
        text = data['text'],
        hover_name = data['hover_name'],
        orientation = 'h',
        labels={'x':'Gasto económico', 'y':''},
        height=data['non_null_count']*30
    )

    barchart.update_layout(
        margin=dict(l=0, r=10, t=25, b=10),
        paper_bgcolor='#f8f9fa',
    )

    content = dcc.Graph(
        id='economic-barchart',
        figure=barchart
    )

    return content
