from GeoBases import GeoBase
import plotly.plotly as py
import pandas as pd

import plotly.plotly as py

nyc_london = [ dict(
    type = 'scattergeo',
    lat = [ 39.0392, 41.8781],
    lon = [ 125.7625, -87.6298],
    mode = 'lines',
    line = dict(
        width = 1,
        color = 'purple',
    ),
) ]
print(nyc_london)
layout = dict(
        title = 'Pyongyang to Chicago',
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

fig = dict( data=nyc_london, layout=layout )
py.iplot( fig, validate=False, filename='d3-great-circle' )


point = (40,-75)
geo_a = GeoBase(data='airports',verbose=False)
#print(list(geo_a.findClosestFromPoint(point)))
#print()