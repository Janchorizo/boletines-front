'''Simple BOE data exploration.'''
import locale
from typing import Callable
# External
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
# Internal
from views.title import title
import data


locale.setlocale(locale.LC_ALL,"")


def layout():
    layout = html.Div(className='container-fluid flex-column d-flex', style={'height': '100vh'}, children=[
        html.Div(className='row', children=[
            title(),
        ]),
        html.Div(className='row fs-4 flex-grow-1', children=[
            html.Div(id='sidebar', className='col p-0 border-end justify-content-end d-flex flex-column', children=[
                html.Div(id='sidebar-top', className='p-5 flex-fill', children=[]
                ),
                html.Div(id='sidebar-bottom', className='p-5 bg-light bg-gradient border-top', children=[]
                )
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
    pass


def main(call_with_db:Callable):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = layout()
    set_callbacks(app, call_with_db)
    app.run_server(debug=True)


if __name__ == '__main__':
    db_host = 'localhost'
    db_database = 'boe'
    db_user = 'root'
    db_password = 'pass'

    call_with_db = data.create_db_wrapper(db_host, db_database, db_user, db_password)
    main(call_with_db)

