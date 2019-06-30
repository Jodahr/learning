import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# dash app
app = dash.Dash()

# layout
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[
        dict(label='First Class', value=1),
        dict(label='Second Class', value=2),
        dict(label='Third Class', value=3)
    ],
                 value=3),
    html.Label('Slider'),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i:i for i in range(-10,10)}),

    html.P(dcc.Markdown(""" This is Markdown: Radio *Items*""")),
    dcc.RadioItems(options=[dict(label='male', value='male'),
                            dict(label='female', value='female')
                            ],value='female'),
    html.Label('Interaction'),
    dcc.Input(id='my-id', value='Initial Text', type='text'),
    html.Div(id='my_div', style={'border':'2px blue solid'})
])

@app.callback(Output(component_id='my_div', component_property='children'),
              [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value):
    return "You entered: {}".format(input_value)



if __name__ == "__main__":
    app.run_server()