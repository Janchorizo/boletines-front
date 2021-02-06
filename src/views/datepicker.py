'''Date picker.'''
import dash_html_components as html
import dash_core_components as dcc


def datepicker(date_range):
    content = html.Div(className='mt-5 border-top border-bottom border-primary d-flex p-4 align-items-center', children=[
        html.Span(className='fw-bold text-primary me-3', children='Cambia la fecha del boletín'),
        dcc.DatePickerSingle(
            id=output_id,
            min_date_allowed=date_range[0],
            max_date_allowed=date_range[1],
            date=date_range[1]
        )
    ])
    return content

output_id = 'date-picker'
