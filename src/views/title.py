'''App title module'''
import dash_html_components as html


def title():
    content = html.Div(className='cell my-3 shrink header medium-cell-block-container text-primary', children=[
        html.H1(children=[
            'Explorador del BOE',
        ]),
        html.H2(children='Un resumen gráfico del Boletín Oficial del Estado'),
    ])
    return content
