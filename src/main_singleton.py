'''Simple BOE data exploration.'''
import collections
import locale
from typing import Callable
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import data


locale.setlocale(locale.LC_ALL,"")


def shorttened(s, length=40, filler='...'):
    if len(s) <= length:
        return s
    else:
        overfill = len(s) - length
        t_length = len(s)//2 - overfill//2
        return ''.join((
            s[:t_length],
            filler,
            s[t_length + overfill + len(filler):]
        ))


def title():
    content = html.Div(className='cell my-3 shrink header medium-cell-block-container text-primary', children=[
        html.H1(children=[
            'Explorador del BOE',
        ]),
        html.H2(children='Un resumen gráfico del Boletín Oficial del Estado'),
    ])
    return content


def side_bar(call_with_db):
    date_range = call_with_db(data.get_date_range)
    markdown_text='''
    Cada día se procesa el [Boletín Oficial del Estado](https://boe.es/) para que puedas verlo
    de forma resumida aquí.

    Cada diario del BOE tiene entradas organizadas en secciones y éstas a su vez en departamentos.
    A veces las entradas van asociadas con un gasto económico (en licitaciones por ejemplo), y verlo
    supone tener que abrir cada boletín.

    Esta página se creó para facilitar dicha información.
    **Selecciona el día en el campo que hay debajo para cambiar el día mostrado en el espacio de la
    derecha.**


    #### **Día**
    '''
    content = html.Div(className='col border-end mt-4 text-muted', children=[
        dcc.Markdown(children=markdown_text),
        dcc.DatePickerSingle(
            id='date-picker',
            min_date_allowed=date_range[0],
            max_date_allowed=date_range[1],
            date=date_range[1]
            )
    ])
    return content


def department_count_by_section_sankey(call_with_db, date):
    entries = call_with_db(data.get_entries_by_department_for_date, date=date)
    entries = sorted(entries, key=lambda x: x[0])

    
    section_names = tuple(set(x for x, *_ in entries))
    section_count = {
        name: sum(map(lambda x: x[2], filter(lambda x: x[0] == name, entries)))
        for name
        in section_names
    }
    department_count = {y: count for x, y, count in entries}
    department_names = tuple(department_count.keys())


    labels = (
        *[f'{name} ({section_count[name]})' for name in section_names],
        *[f'{name} ({department_count[name]})' for name in department_names]
    )

    fig = go.Figure( 
        data=[go.Sankey(
            node = dict( 
                label = labels
            ),
            link = dict(
                source = [section_names.index(x) for x, *_ in entries],
                target = [len(section_names) + department_names.index(y) for x, y, _ in entries],
                value = [count for *_, count in entries]
            ))])
    fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=10),
    paper_bgcolor='#f8f9fa',
    autosize=True,
    #width=850,
    #height=900,
    )

    return dcc.Graph(
        style={'height': '100%'},
        figure=fig
    )


def entry_header(entries, date):
    meses = 'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'.split(' ')
    link = f'https://boe.es/boe/dias/{date:%Y}/{date:%m}/{date:%d}/'
    types = data.get_entry_types(entries)
    economic_impact = locale.currency(sum(x for *_, x, y, z in entries), grouping=True)

    types_list = '\n'.join(
        f'- {e[1]} entradas son {e[0]}' for e in types.items() if e[0] != ''
    )

    content = html.Div(className='', children=[
        html.H1(children=[
            f'Boletín del día {date:%d} de {meses[date.month-1]}, {date.year}',
        ]),
        dcc.Markdown(children=f'### Puedes verlo en [{link}]({link})'),
        dcc.Markdown(children=f'''Se registraron un total de **{len(entries)} entradas**, de las cuales:

{types_list}

Las licitaciones y formalizaciones de contrato publicadas suman un monto de **{economic_impact}**.
        ''')
    ])
    return content


def economic_barchart(entries):
    costs = {}
    for title, department, cost, *_ in entries:
        if cost > 0:
            costs[department] = costs.setdefault(department, 0) + cost

    barchart = px.bar(
        x = tuple(costs.values()),
        y = tuple(shorttened(x) for x in costs.keys()),
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


def get_diary_entry_overview_content(call_with_db, date):
    entries = call_with_db(data.get_entries, date=date)
    return [
        entry_header(entries, date),
        economic_barchart(entries)
    ]


def main_view(call_with_db):
    content = html.Div(className='col-9 bg-light border-top', children=[
        html.Div(className='row h-100', children=[
            html.Div(
                id='diary-entry-overview',
                className='col', children=[]
            ),
            html.Div(
                id='department-count-by-section-sankey',
                className='col shadow', children=[]
            )
        ])
    ])
    return content


def get_layout(call_with_db):
    layout = html.Div(className='container-fluid flex-column d-flex', style={'height': '100vh'}, children=[
        html.Div(className='row', children=[
            title(),
        ]),
        html.Div(className='row fs-4 flex-grow-1', children=[
            side_bar(call_with_db),
            main_view(call_with_db)
        ])
    ])
    return layout


def main(call_with_db:Callable):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = get_layout(call_with_db)

    @app.callback(
        Output(component_id='department-count-by-section-sankey', component_property='children'),
        Input(component_id='date-picker', component_property='date'),
    )
    def update_department_sankey(input_value):
        date = datetime.date.fromisoformat(input_value)
        return department_count_by_section_sankey(call_with_db, date)

    @app.callback(
        Output(component_id='diary-entry-overview', component_property='children'),
        Input(component_id='date-picker', component_property='date'),
    )
    def update_entry_overview(input_value):
        date = datetime.date.fromisoformat(input_value)
        return get_diary_entry_overview_content(call_with_db, date)

    app.run_server(debug=True)


if __name__ == '__main__':
    db_host = 'localhost'
    db_database = 'boe'
    db_user = 'root'
    db_password = 'pass'

    call_with_db = data.create_db_wrapper(db_host, db_database, db_user, db_password)
    main(call_with_db)

