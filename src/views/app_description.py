'''Description module

Github buttons taken from https://ghbtns.com/
'''
import dash_html_components as html
import dash_core_components as dcc


mkd = f'''### Acerca de
Hola! Me puedes llamar [Janchorizo](https://github.com/Janchorizo). Hice esta página con mucho ♥ como parte
de un proyecto más grande para facilitar el uso del BOE.

Mantener los servidores cuesta dinero y, aunque lo hago de forma desinteresada, agradezco
cualquier ayudita a través de Github o BuyMeACoffee.
'''

def app_description():
    markdown_text='''
    Cada día se procesa el [Boletín Oficial del Estado](https://boe.es/) para que puedas verlo
    de forma resumida aquí.

    Cada diario del BOE tiene entradas organizadas en secciones y éstas a su vez en departamentos.
    A veces las entradas van asociadas con un gasto económico (en licitaciones por ejemplo), y verlo
    supone tener que abrir cada boletín.

    Esta página se creó para facilitar dicha información.
    **Selecciona el día en el campo que hay debajo para cambiar el día mostrado en el espacio de la
    derecha.**

    '''
    content = html.Div(className='text-muted', children=[
        dcc.Markdown(children=markdown_text),
    ])
    return content
