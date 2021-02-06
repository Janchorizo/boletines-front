'''Economic cost by department barchart.'''
import locale
# External
import dash_core_components as dcc
import plotly.express as px
# Internal
import helpers


def cost_by_department_barchart(entries):
    costs = {}
    for title, department, cost, *_ in entries:
        if cost > 0:
            costs[department] = costs.setdefault(department, 0) + cost

    barchart = px.bar(
        x = tuple(costs.values()),
        y = tuple(helpers.shorttened(x) for x in costs.keys()),
        text = tuple(locale.currency(x, grouping=True) for x in costs.values()),
        hover_name = tuple(costs.keys()),
        orientation = 'h',
        labels={'x':'Gasto económico', 'y':''},
        height=len(costs)*30
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
