
# coding: utf-8

# In[1]:

import plotly
plotly.tools.set_credentials_file(username='justsfam', api_key='owa58kclb0')
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import numpy as np

# In[2]:

#functions for plotting
def scat_3d(d1,d2,d3):
    #creates a 3d scatter plot
    trace1 = go.Scatter3d(
        x=d1,
        y=d2,
        z=d3,
        mode='markers',
        marker=dict(
            size=12,
            color=np.arange(200,400),                # set color to an array/list of desired values
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8
        )
    )
    data = [trace1]
    layout = go.Layout(
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        )
    )
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.iplot(fig)
    
def hist(x1,y1):
    #creates a histogram
    data = [
    go.Histogram(
            x=x1,
            nbinsx = y1
        )
    ]
    return plotly.offline.iplot(data)
    
def scat_plot(d1,d2,d3):
    #2d scatter plot
    trace = go.Scatter(
        x = d1,
        y = d2,
        text = d3,
        mode = 'markers'
    )

    data = [trace]
    
    # Plot and embed in ipython notebook!
    return plotly.offline.iplot(data)

def line_plot(d1,d2,d3):
    #2d scatter plot with line
    trace = go.Scatter(
        x = d1,
        y = d2,
        text = d3,
        mode = 'lines+markers'
    )

    data = [trace]
    
    # Plot and embed in ipython notebook!
    return plotly.offline.iplot(data)

def scat_mat(d):
    fig = FF.create_scatterplotmatrix(d, height=1000, width=1000)
    return plotly.offline.iplot(fig)

def cluster_plot_old(d):
    n = d.label.unique()
    trace = []
    for i in n:
        d_n = d[(d['label']==i)]
        trace0 = go.Scatter(
            x=d_n.x.values,
            y=d_n.y.values,
            text = d_n.fit.values,
            mode='markers',
        )
        trace.append(trace0)
    fig = {
        'data': trace,
        #'layout': layout,
    }
    return plotly.offline.iplot(fig)
# In[ ]:

def cluster_plot(d, x_feature, y_feature, point_markers, x_label, y_label, title):
    color = ['blue','orange','green','brown','red','black','yellow','pink','blue','orange','green','brown','red','black','yellow','pink','blue','orange','green','brown','red','black','yellow','pink','blue','orange','green','brown','red','black','yellow','pink']
    n = d.label.nunique()
    n_list = d.label.unique()
    trace = []
    lst = []
    layout = {}
    value = {}
    for i in range(n):
        d_n = d[(d['label']==n_list[i])]
        x1 = d_n[x_feature].values
        y1 = d_n[y_feature].values
        pm = d_n[point_markers].values
        trace0 = go.Scatter(
            x=x1,
            y=y1,
            text = pm,
            mode='markers',
        )
        trace.append(trace0)
        
        x ={}
        x['type'] = 'circle'
        x['xref'] = 'x'
        x['yref'] = 'y'
        x['x0']= min(x1)
        x['y0']= min(y1)
        x['x1']= max(x1)
        x['y1']= max(y1)
        x['opacity']= 0.1
        x['fillcolor']= color[i]
        y = {}
        y['color']=color[i]
        x['line']=y
        #print x
        lst.append(x)
    #print lst
    layout['shapes']=lst
    layout['title'] = title
    
    temp = {}
    temp['title']=x_label
    layout['xaxis'] = temp

    temp={}
    temp['title']=y_label
    layout['yaxis'] = temp

    layout['showlegend'] = False
    #return layout
    #json_data = json.dumps(layout)
    #layout = json.loads(json_data)
    
    fig = {
        'data': trace,
        'layout': layout,
    }
    
    return plotly.offline.iplot(fig)

def cluster_plot_induvidual(d,c,color):
    x0 = d.x.values
    y0 = d.y.values
    a = d[(d['style_id'].isin(c['article_center']))]
    x1 = a.x.values
    y1 = a.y.values
        
    
    trace0 = go.Scatter(
        x=x0,
        y=y0,
        mode='markers',
    )
    trace1 = go.Scatter(
        x=x1,
        y=y1,
        mode='markers'
    )
    layout = {
        'shapes': [
            {
                'type': 'circle',
                'xref': 'x',
                'yref': 'y',
                'x0': min(x0),
                'y0': min(y0),
                'x1': max(x0),
                'y1': max(y0),
                'opacity': 0.2,
                'fillcolor': color,
                'line': {
                    'color': color,
                },
            },
            {
                'type': 'circle',
                'xref': 'x',
                'yref': 'y',
                'x0': min(x1),
                'y0': min(y1),
                'x1': max(x1),
                'y1': max(y1),
                'opacity': 0.2,
                'fillcolor': color,
                'line': {
                    'color': color,
                },
            },
        ],
        'showlegend': False,
    }
    data = [trace0, trace1]
    fig = {
        'data': data,
        'layout': layout,
    }
    
    return plotly.offline.iplot(fig)

