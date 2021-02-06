'''Entry table.'''
import collections
# External
import pandas as pd
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_table
# Internal
import helpers


code_to_section_name = {
    '1': 'disposiciones generales',
    '2': 'autoridades y personal',
    '2a': 'nombramientos situaciones e incidencias',
    '2b': 'oposiciones y concursos',
    '3': 'otras secciones',
    '4': 'administración de justicia',
    '5': 'anuncios',
    '5a': 'licitaciones públicas y adjudicaciones',
    '5b': 'otros anuncios particulares',
    '5c': 'anuncios particulares',
    't': 'tribunal constitucional'
}


def diary_entry_table(entries):
    data = (
        (
            title,
            helpers.shorttened(title, 30),
            department,
            helpers.shorttened(department, 30),
            cost,
            f"[{htm_url.split('=')[1]}]({'https://boe.es'+htm_url})"
        )
        for title, section, department, cost, htm_url, pdf_url
        in entries
    )
    df = pd.DataFrame(data, columns=('Título_', 'Título', 'Departamento_', 'Departamento', 'Coste', 'Ver en el BOE'))
    content = dash_table.DataTable(
        id='datatable-interactivity',
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        columns=[
            *[
                {"name": i, "id": i, "deletable": False, "selectable": False}
                for i
                in df.columns
                if i not in ['id', 'Ver en el BOE', 'Título_', 'Departamento_']],
            {"name": 'Ver en el BOE', "id": 'Ver en el BOE', "deletable": False, "selectable": True, 'presentation':'markdown'}
        ],
        tooltip_data=[
            {
                column: {'value': str(value) if not column+'_' in row else str(row[column+'_']), 'type': 'markdown'}
                for column, value in row.items()
            } for row in df.to_dict('records')
        ],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode="single",
        #page_action="native",
        #page_current= 0,
        page_size= 18,
    )
    return content
