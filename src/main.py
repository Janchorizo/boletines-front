'''Simple BOE data exploration.'''
import locale
import datetime
from typing import Callable
# External
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
# Internal
from views.title import title
from views.about import about
from views.app_description import app_description
from views.datepicker import datepicker
from views.datepicker import output_id as date_output_id
from views.diary_overview import diary_overview
from views.cost_by_department_barchart import cost_by_department_barchart
import data


locale.setlocale(locale.LC_ALL,"")


def layout(date_range):
    layout = html.Div(className='container-fluid flex-column d-flex', style={'height': '100vh'}, children=[
        html.Div(className='row', children=[
            title(),
        ]),
        html.Div(className='row fs-4 flex-grow-1', children=[
            html.Div(id='sidebar', className='col p-0 border-end justify-content-end d-flex flex-column', children=[
                html.Div(id='sidebar-top', className='p-5 flex-fill', children=[
                    app_description(),
                    datepicker(date_range)
                ]),
                html.Div(id='sidebar-bottom', className='p-5 bg-light bg-gradient border-top', children=[
                    about()
                ])
            ]),
            html.Div(className='col-9 bg-light border-top', children=[
                html.Div(className='row h-100', children=[
                    html.Div(id='main-left', className='col', children=[]
                    ),
                    html.Div(id='main-right', className='col shadow', children=[]
                    )
                ])
            ])
        ])
    ])
    return layout


def set_callbacks(app, call_with_db:Callable):
    '''Set the callbacks.'''
    
    @app.callback(
        Output(component_id='main-left', component_property='children'),
        Input(component_id=date_output_id, component_property='date'),
    )
    def update_entry_overview(input_value):
        date = datetime.date.fromisoformat(input_value)
        entries = call_with_db(data.get_entries, date=date)
        return [
            diary_overview(entries, date),
            cost_by_department_barchart(entries)
        ]


def main(call_with_db:Callable):
    date_range = call_with_db(data.get_date_range)

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = layout(date_range)
    set_callbacks(app, call_with_db)
    app.run_server(debug=True)


if __name__ == '__main__':
    db_host = 'localhost'
    db_database = 'boe'
    db_user = 'root'
    db_password = 'pass'

    call_with_db = data.create_db_wrapper(db_host, db_database, db_user, db_password)
    main(call_with_db)

