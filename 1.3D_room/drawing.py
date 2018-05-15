import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
def  show():
    #--------------------------------------------分割线-----读取数据----------------------------------------------#
    frame = DataFrame(pd.read_csv('intergrate.csv'))
    x=np.array(frame['x'])
    y= np.array(frame['y'])
    z=np.array(frame['z'])
    col=np.array(frame['azimuth'])
    #--------------------------------------------分割线----设置画图数据----------------------------------------------#
    trace=go.Scatter3d(#（官方文档） https://plot.ly/python/reference/#scatter3d
        opacity=0.9,
        x=x,
        y=y,
        z=z,
        mode="markers",
        marker=dict(size=1,
                    # line=dict(width=1),
                    color=col,
                    colorscale="RdBu",#Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow, Portland,
                                          # Jet, Hot, Blackbody, Earth, Electric, Viridis, Cividis
                    colorbar = dict(
                        title = 'azimuth',x=0.8
                    ),
        ),

    )
    data=[trace]
    #--------------------------------------------分割线----设置布局(XYZ轴)----------------------------------------------#
    layout = go.Layout(
        # bgcolor = "rgba(255,0,0,0)"
        title='Test Plot',
        autosize=True,
        scene=dict(
            aspectratio=dict(#https://community.plot.ly/t/setting-x-y-z-axes-width-for-a-3d-scatter-plot-in-python/1276,设置xyz纵横比，matlab里的axis equal
                x=1,
                y=1,
                z=0.5,

            ),
            xaxis =dict(
                # title="fs",
                rangemode ="tozero",
            )
             ,
                yaxis =dict(
                rangemode ="tozero",
            ) ,
                zaxis =dict(
                rangemode ="tozero",
            ) ,

        )
    )

    #--------------------------------------------分割线----见证奇迹的时候-------------------------------------------------#
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)



