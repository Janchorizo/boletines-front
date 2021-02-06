'''Sankey diagram for the diary entry flow by section and department.'''
import collections
# External
import dash_core_components as dcc
import plotly.graph_objects as go
# Internal
import helpers


def diary_entry_sankey(entries_):
    entries = sorted(entries_, key=lambda x: x[0])

    section_names = tuple(set(x for x, *_ in entries))
    section_count = {
        name: sum(map(lambda x: x[2], filter(lambda x: x[0] == name, entries)))
        for name
        in section_names
    }
    department_count = {y: count for x, y, count in entries}
    department_names = tuple(department_count.keys())

    labels = (
        *[f'{helpers.shorttened(name, length=50)} ({section_count[name]})' for name in section_names],
        *[f'{helpers.shorttened(name, length=50)} ({department_count[name]})' for name in department_names]
    )

    fig = go.Figure( 
        data=[go.Sankey(
            arrangement='fixed',
            hoverinfo='skip',
            node = dict( 
                label = labels
            ),
            link = dict(
                source=[section_names.index(x) for x, *_ in entries],
                target=[len(section_names) + department_names.index(y) for x, y, _ in entries],
                value=[count for *_, count in entries],
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
