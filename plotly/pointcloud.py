import plotly.plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
#--------------------------------------------分割线-----读取数据----------------------------------------------#
frame = DataFrame(pd.read_csv('kk.csv'))
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


#
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import pandas as pd
# from pandas import DataFrame,Series
#
# frame = DataFrame(pd.read_csv('2.csv'))
# x=np.array(frame['Points_m_XYZ:0'])
# y= np.array(frame['Points_m_XYZ:1'])
# z=np.array(frame['Points_m_XYZ:2'])
#
# ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# #  将数据点分成三部分画，在颜色上有区分度
# ax.scatter(x[:], y[:], z[:], c='y',s=0.1)  # 绘制数据点
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

# import plotly.graph_objs as go
# import plotly.plotly
# import pandas as pd
#
# # Read data from a csv
# # z_data = pd.read_csv('face.csv')
#
# data = [
#     go.Surface(
#         z=[[2,2,2],[2,2,2],[2,2,2],[0,0,0],[0,0,0],[0,0,0]],
#         x=[0,1,2  ,0,1,2],
#         y=[0,1,2  ,0,1,2],
#     ),
# go.Surface(
#         z=[[2,2,2],[2,2,2],[1,1,1],[1,1,1],[2,2,2]],
#         x=[0,1,1,1,1],
#         y=[0,1,1,0,0],
#
#     )
# ]
# layout = go.Layout(
#     title='Mt Bruno Elevation',
#     autosize=True,
#     # width=500,
#     # height=500,
#     # margin=dict(
#     #     l=65,
#     #     r=50,
#     #     b=65,
#     #     t=90
#     # )
# )
#
# fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='elevations-3d-surface')

