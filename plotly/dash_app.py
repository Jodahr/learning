import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# load titanic
df_titanic = pd.read_csv('titanic.csv',sep='\t')
df_titanic.head()


##################
# # PLOTLY PLOTS #
##################

# boxplot
data_box = [go.Box(y=df_titanic[df_titanic['Pclass'] == pclass]['Age'], name=str(pclass))
for pclass in df_titanic.Pclass.unique()]

layout_box = go.Layout(title="Scatter Plot",
 xaxis=dict(title='Passenger Class'), yaxis=dict(title='Age in years'))

# histogram
data_hist = [go.Histogram(x=df_titanic['Age'], xbins=dict(size=2))]


# dash app
app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[html.H1("Hello Dash",
                                        style={'textAlign': 'center',
                                               'color': colors['text']}),
                                html.Div('Dash: Web Dashboard'),
                                dcc.Graph(id='boxplot',
                                          figure={'data': data_box,
                                                  'layout': layout_box})
                                ,
                                dcc.Graph(id='hist', figure={
                                    'data': data_hist
                                })

                                ])

if __name__ == "__main__":
    app.run_server()
