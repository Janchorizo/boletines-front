'''About module

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

def about():
    content = html.Div(id='about', className='cell my-3 shrink header medium-cell-block-container text-primary', children=[
        dcc.Markdown(children=mkd),
        html.Iframe(
            src="https://ghbtns.com/github-btn.html?user=Janchorizo&repo=boletines-front&type=star&count=true&size=large",
            width=150,
            height=30,
            title="GitHub"
        ),
        html.Iframe(
            src="https://ghbtns.com/github-btn.html?user=Janchorizo&repo=boletines-front&type=sponsor",
            width=150,
            height=20,
            title="GitHub"
        ),
        html.A(
            href='https://www.buymeacoffee.com/janchorizo',
            target='_blank',
            children=[
                html.Img(
                    src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png",
                    alt="Buy Me A Coffee",
                    style={'height': '60px', 'width': '217px'}
                )
            ]
        )
    ])
    return content
