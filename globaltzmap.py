import numpy as np
import matplotlib.pyplot as plt
import csv
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.offline.offline import _plot_html
from plotly.graph_objs import *
from tzwhere import tzwhere
from scipy.optimize import minimize_scalar
from scipy.optimize import fsolve
from scipy.integrate import odeint
init_notebook_mode()

csvdata = list(csv.reader(open("UTFData.csv",encoding="UTF-8")))
csvdata = np.array(csvdata)
dataset1=[[36.6,-121.89846],[52.1427,6.1961],[-37.8136,144.9631],[31.2304,121.4737],[22.39,114.1095],[55.7558,37.6173]]
dataset2=[[42.3601,-71.0589],[42.3601,-71.0589],[1.3521,103.8198],[39.91,160.3636],[22.3964,114.1095],[22.3964,114.1095],[55.7558,37.6173],[52.0907,5.1412],[52.2297,21.0122],[55.6761,12.5683],[-37.8136,144.9631]]
latlongarray=dataset2

longlist = []
latlist = []
tzlist = []

i=-80
j=-180

shitintheocean = 0

while(i<84):
    while (j<180):
        if (longToTzName(i,j) == None):
            shitintheocean+=1
        else:
            latlist.append(i)
            longlist.append(j)
            tzlist.append(longToTz(longToTzName(i,j)))
        j=j+2
    i=i+2
    j=-180
    print(i)
i=-80
#shitintheocean=0

def longToTzName(lat,long):
    return tz.tzNameAt(lat,long)

def longToTz(name):
    panic=False
    k=0
    if (name == None):
        panic = True
        return 0
    else:
        while(k<(csvdata.shape[0])):
            if(csvdata[k][2]==name):
                return csvdata[k][4]
            else:
                k+=1
        k=0

data = [ dict(
        type = 'scattergeo',
        locationmode = 'world',
        lon = longlist,
        lat = latlist,
        text = 'text',
        mode = 'markers',
        marker = dict(
            size = 4,
            opacity = 1,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            color = tzlist,
            colorscale = 'Rainbow',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorbar=dict(
                title="Timezones",
                thickness=15,
                tickmode="array",
                showticklabels=True,
            )
        ))]

layout = dict(
        title = 'Timezone Map',
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

plotly.offline.plot({"data": data, "layout": layout},validate=False,image='svg')