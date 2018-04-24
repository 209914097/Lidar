#------contours------#
# import plotly.plotly
# from plotly.graph_objs import *
# import pandas as pd
# z_data = pd.read_csv('df.csv').drop(['ID'],axis=1)
# trace1 = {
#     "z": z_data.as_matrix(),
#     # "z":[[10, 10.625, 12.5, 15.625, 20],
#     #        [5.625, 6.25, 8.125, 11.25, 15.625],
#     #        [2.5, 3.125, 5., 8.125, 12.5],
#     #        [0.625, 1.25, 3.125, 6.25, 10.625],
#     #        [0, 0.625, 2.5, 5.625, 10]],
#     #     "x":[-9, -6, -5, -3, -1],
#     #     "y":[0, 1, 4, 5, 7],
#       "type": "contour",
#     "contours":{
#             "coloring" :'heatmap',
#             "showlabels" : True,
#             "labelfont" : {
#                 "family" :'Raleway',
#                 "size" : 12,
#                 "color" : 'white',
#             }
#     },
#     # 'dx': 10,
#     # 'x0': 5,
#     # 'dy': 10,
#     # 'y0':10,
# }
# data = Data([trace1])
# fig = Figure(data=data)
# plot_url = plotly.offline.plot(fig)

#------Surface------#
import plotly.graph_objs as go
import plotly.plotly
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('df.csv').drop(['ID'],axis=1)

data = [
    go.Surface(
        z=z_data.as_matrix()
        # z=[[10, 10.625, 12.5, 15.625, 20],
        #    [5.625, 6.25, 8.125, 11.25, 15.625],
        #    [2.5, 3.125, 5., 8.125, 12.5],
        #    [0.625, 1.25, 3.125, 6.25, 10.625],
        #    [0, 0.625, 2.5, 5.625, 10]],
        # x=[-9, -6, -5, -3, -1],
        # y=[0, 1, 4, 5, 7]

),

]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=True,
    scene= {
    "aspectratio": {
        "x": 2,
        "y": 1,
        "z": 0.1,
    },
    }
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='elevations-3d-surface')
