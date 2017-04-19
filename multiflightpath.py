from GeoBases import GeoBase
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.offline.offline import _plot_html
from plotly.graph_objs import *
import numpy as np
import random
import plotly
init_notebook_mode()
conference=[55.96756757,35.89189189]
#conference=[47.0925,8.305]
#[[latitude,latitude2],[longitude,longitude2],]
flightdata1 = [[[36.5883,conference[0]],[-121.8491,conference[1]]],[[52.1427,conference[0]],[6.1961,conference[1]]],[[-37.6690,conference[0]],[144.8410,conference[1]]],[[31.2304,conference[0]],[121.4737,conference[1]]],[[22.39,conference[0]],[114.1095,conference[1]]],[[55.7558,conference[0]],[37.6173,conference[1]]]]
flightdata2 = [[[42.3601,conference[0]],[-71.0589,conference[1]]],[[42.3601,conference[0]],[-71.0589,conference[1]]],[[1.3521,conference[0]],[103.8198,conference[1]]],[[39.91,conference[0]],[116.4074,conference[1]]],[[22.3964,conference[0]],[114.1095,conference[1]]],[[22.3964,conference[0]],[114.1095,conference[1]]],[[55.7558,conference[0]],[37.6173,conference[1]]],[[52.0907,conference[0]],[5.1412,conference[1]]],[[52.2297,conference[0]],[21.0122,conference[1]]],[[55.6761,conference[0]],[12.5683,conference[1]]],[[-37.8136,conference[0]],[144.9631,conference[1]]]]
flightpaths = []

flightnames1 = ["Monterey CA, USA","Zutphen, Netherlands","Melbourne, Australia","Shanghai, China","Hong Kong (SAR), China","Moscow, Russia"]
flightnames2 = ["Boston MA, USA","Boston MA, USA","Singapore","Beijing, China","Hong Kong (SAR), China","Hong Kong (SAR), China", "Moscow, Russia","Utrecht, Netherlands","Warsaw, Poland","Copenhagen, Denmark","Melbourne, Australia"]

r = lambda: random.randint(0,255)

i=0



for i in range ( len (flightdata1)):
    flightpaths.append(dict(
    type = 'scattergeo',
    lat = flightdata1[i][0],
    lon = flightdata1[i][1],
    name = 'Flight -- ' + flightnames1[i],
    mode = 'lines',
    line = dict(
        width = 3,
        color = '#%02X%02X%02X' % (r(),r(),r()),
    ),))
i=0

print(flightpaths)

layout = dict(
        title = 'Scenario 1 Flight Results',
        showlegend = True,         
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
plotly.offline.plot({"data": flightpaths, "layout": layout},validate=False,image='svg')


point = (40,-75)
geo_a = GeoBase(data='airports',verbose=False)
#print(list(geo_a.findClosestFromPoint(point)))
#print()