#!/usr/bin/env python3

# import modules
import pandas as pd
from sklearn import datasets
import plotly.offline as pyo
import plotly.graph_objs as go

# load data
iris = datasets.load_iris()
df = pd.DataFrame(data=iris['data'],
                  columns=iris['feature_names'])
df['species'] = iris['target']
df['species_name'] = df['species'].apply(lambda x: iris['target_names'][x])
df.head()

iris['target_names']

########################
# # FIRST SCATTER PLOT #
########################

# similar to list of axes (roughly)
data = [go.Scatter(x=df['sepal length (cm)'].values,
        y=df['petal width (cm)'].values, mode='markers',
        marker=dict(size=12, color='rgb(51,204,153)', symbol='pentagon',
        line={'width':2}))]

# layout
layout = go.Layout(title="Scatter Plot",
 xaxis=dict(title='sepal length (cm)'),
 yaxis= dict(title='petal width in (cm)'),
 hovermode='closest')

# combine data and layout to fig
fig = go.Figure(data=data, layout=layout)

# plot
pyo.plot(fig)

#########################
# # SECOND SCATTER PLOT #
#########################
marker = dict(size=12, symbol='pentagon',
        line={'width':2})

trace0 = go.Scatter(x=df[df.species == 0].iloc[:,0],
 y=df[df.species == 0].iloc[:,1],  mode='markers',
  name='setosa')

trace1 = go.Scatter(x=df[df.species == 1].iloc[:,0],
 y=df[df.species == 0].iloc[:,1],  mode='markers',
 name='versicolor')

trace2 = go.Scatter(x=df[df.species == 2].iloc[:,0],
 y=df[df.species == 0].iloc[:,1],  mode='markers',
 name='virginica')

# combine all three plots
data = [trace0, trace1, trace2]
fig = go.Figure(data=data)
# set figure layout
fig.layout.template = 'plotly_dark'
# interactive plot
pyo.iplot(fig)

#############
# # BARPLOT #
#############
df['species_name']
data = [go.Bar(x=df['species_name'].unique(), y=df['species_name'].value_counts())]
layout = go.Layout(barmode='stack')
fig = go.Figure(data=data, layout=layout)
fig.layout.template = 'plotly_dark'
pyo.iplot(fig)

# stacked barplot only for three items in data

# load titanic
df_titanic = pd.read_csv('titanic.csv',sep='\t')
df_titanic.head()

data = []
df_survived = df_titanic[df_titanic.Survived == 1]
df_died = df_titanic[df_titanic.Survived == 0]

df_died.Sex.value_counts()

trace1 = go.Bar(x=['male', 'female'],
 y=df_died.Sex.value_counts(), name='died', orientation='v')
trace2 = go.Bar(x=['male', 'female'],
 y=df_survived.Sex.value_counts(), name='survived', orientation='v')
data=[trace1, trace2]

layout = go.Layout(barmode='stack')
fig = go.Figure(data=data, layout=layout)
fig.layout.template = 'plotly_dark'
pyo.iplot(fig)

# another test
trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
pyo.iplot(fig, filename='box')

#############
# # BOXPLOT #
#############

data = [go.Box(y=df_titanic[df_titanic['Pclass'] == pclass]['Age'], name=str(pclass))
for pclass in df_titanic.Pclass.unique()]

fig = go.Figure(data)
pyo.iplot(fig, filename='box')

###############
# # HISTOGRAM #
###############

# data = [go.Histogram(x=df_titanic[df_titanic['Pclass'] == pclass]['Age'], name=str(pclass))
# for pclass in df_titanic.Pclass.unique()]
data = [go.Histogram(x=df_titanic['Age'], xbins=dict(size=2))]
fig = go.Figure(data)
pyo.iplot(fig, filename='hist')

