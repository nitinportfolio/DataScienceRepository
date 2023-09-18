import numpy as np


import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(101)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# Adding titles & axes names 
data = [go.Scatter(x = random_x, y= random_y, mode = 'markers')]
layout = go.Layout(title = 'Scatter Plot',
                  xaxis = dict(title = 'My X Axis'),
                  yaxis = dict(title='My Y Axis'),
                  hovermode='closest')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig, filename='scatter.html')