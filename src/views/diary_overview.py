'''Diary entry overview.'''
import locale
# External
import dash_html_components as html
import dash_core_components as dcc
# Internal
import data

def entry_type_list(entries):
    types = data.get_entry_types(entries)
    types_list = [f'{e[1]} entradas son {e[0]}' for e in types.items() if e[0] != '']
    
    content = html.Ul(className='list-group list-group-flush', children=[
        html.Li(className='list-group-item bg-transparent', children=t) for t in types_list
    ])
    return content


def diary_overview(entries, date):
    month_names = 'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'.split(' ')
    link = f'https://boe.es/boe/dias/{date:%Y}/{date:%m}/{date:%d}/'
    economic_impact = locale.currency(sum(x for *_, x, y, z in entries), grouping=True)

    
    overview_mkd = f'Se registraron un total de **{len(entries)} entradas**, de las cuales:'
    economic_overview_mkd = f'Las licitaciones y formalizaciones de contrato publicadas suman un monto de **{economic_impact}**.'

    content = html.Div(className='m-3', children=[
        html.H1(className='', children=f'Boletín del día {date:%d} de {month_names[date.month-1]}, {date.year}'),
        dcc.Markdown(children=f'#### _(Accesible en [{link}]({link}))_'),
        dcc.Markdown(className='mt-5', children=overview_mkd),
        entry_type_list(entries),
        dcc.Markdown(children=economic_overview_mkd)
    ])
    return content
