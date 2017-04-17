from GeoBases import GeoBase
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.offline.offline import _plot_html
from plotly.graph_objs import *
init_notebook_mode()

flightdata = [[[39.0392,41.8781],[125.7625,-87.6298]],[[51.5074,19.8563],[-.1278,102.4955]]]

flightpaths = []
for i in range ( len (flightdata)):
    flightpaths.append(dict(
    type = 'scattergeo',
    lat = flightdata[i][0],
    lon = flightdata[i][1],
    mode = 'lines',
    line = dict(
        width = 1,
        color = 'purple',
    ),))

print(flightpaths)

layout = dict(
        title = 'MAPS',
        showlegend = False,         
        geo = dict(
            resolution = 100,
            showland = True,
            showlakes = True,
            landcolor = 'rgb(204, 204, 204)',
            countrycolor = 'rgb(204, 204, 204)',
            lakecolor = 'rgb(255, 255, 255)',
            projection = dict( type="equirectangular" ),
            coastlinewidth = 2,
            lataxis = dict(
                range = [ -100, 100 ],
                showgrid = False,
                tickmode = "linear",
                dtick = 20
            ),
            lonaxis = dict(
                range = [-100, 100],
                showgrid = False,
                tickmode = "linear",
                dtick = 20
            ),
        )
    )

#fig = dict(data=flightpaths, layout=layout )
#iplot(fig, validate=False)
plotly.offline.plot({"data": flightpaths, "layout": layout},validate=False)


point = (40,-75)
geo_a = GeoBase(data='airports',verbose=False)
#print(list(geo_a.findClosestFromPoint(point)))
#print()