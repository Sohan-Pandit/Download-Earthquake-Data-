"""
Created on Mon Jun 12 00:47:00 2023

@author: sohan
"""

import os
import obspy.clients.fdsn
import numpy as np
import pandas as pd
import obspy
import obspy.clients.fdsn
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.basemap import Basemap

os.environ['PROJ_LIB'] = r'E:/My Softwares/Anaconda/pkgs/proj4-4.9.3-hfa6e2cd_9'

folder_output = 'F:/Project AK sir/CODE/Code from git/events/'
os.makedirs(folder_output, exist_ok=True)

excel_filename = 'events.xlsx'
excel_tab = 'info'

starttime = obspy.UTCDateTime("2003-01-01")
endtime = obspy.UTCDateTime("2005-12-25")

client = "USGS"

minlatitude = 20.146
maxlatitude = 40.585
minlongitude = 65.871
maxlongitude = 105.978

minmagnitude = 2
maxmagnitude = 5

#%%
#
#

client = obspy.clients.fdsn.Client(client)

events = client.get_events(
    minlatitude=minlatitude,
    maxlatitude=maxlatitude,
    minlongitude=minlongitude,
    maxlongitude=maxlongitude,
    starttime=starttime,
    endtime=endtime,
    minmagnitude=minmagnitude,
    maxmagnitude=maxmagnitude
)

print("Found %s event(s):" % len(events))
print(events)

print(events.__str__(print_all=True))

#%%

feature_list = [
    'Origin Time (UTC)', 'Lat [°]', 'Lon [°]', 'depth [m]', 'event_type',
    'mag', 'magnitude_type', 'creation_info', 'info'
]
df = pd.DataFrame(columns=feature_list)

for ii in range(len(events)):
    origin = events[ii].origins[0]
    magnitude = events[ii].magnitudes[0]

    df = df.append({
        'Origin Time (UTC)': origin.time,
        'Lat [°]': origin.latitude,
        'Lon [°]': origin.longitude,
        'depth [m]': origin.depth,
        'event_type': events[ii].event_type,
        'mag': magnitude.mag,
        'magnitude_type': magnitude.magnitude_type,
        'creation_info': origin.creation_info,
        'info': events[ii].event_descriptions[0].text
    }, ignore_index=True)

#%%

excel_output = os.path.join(folder_output, excel_filename)
df.to_excel(excel_output, sheet_name=excel_tab)

#%%

plt.rcParams.update({'font.size': 14})
plt.rcParams['axes.labelweight'] = 'bold'


t1 = starttime.strftime('%Y-%m-%d') # Start time
t2 = endtime.strftime('%Y-%m-%d') # End time



x = df['Lon [°]'].values # Longitude

y = df['Lat [°]'].values # Latitude
z = df['mag'].values

plt_title = 'Earthquakes {} - {}'.format(t1, t2)
plt_fig = os.path.join(folder_output, plt_title + '.png')

figsize = (10, 10)
fig = plt.figure(figsize=figsize)

ax = fig.add_subplot(111, facecolor='w', frame_on=False)

norm = Normalize()

x_ticks = np.arange(
    minlongitude, maxlongitude + maxlongitude / 10000,
    float("{0:.3f}".format(maxlongitude - minlongitude)) / 5
)
y_ticks = np.arange(
    minlatitude, maxlatitude + maxlatitude / 10000,
    float("{0:.3f}".format(maxlatitude - minlatitude)) / 5
)

map = Basemap(
    llcrnrlon=minlongitude, llcrnrlat=minlatitude,
    urcrnrlon=maxlongitude, urcrnrlat=maxlatitude,
    projection='merc', resolution='h'
)

x_lon, y_lat = map(*(x, y))

map.drawcoastlines()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='grey', lake_color='aqua')
map.drawcountries(
    linewidth=.75, linestyle='solid', color='#000073',
    antialiased=True,
    ax=ax, zorder=3
)
map.drawparallels(
    y_ticks,
    color='black', linewidth=0.5,
    labels=[True, False, False, False]
)
map.drawmeridians(
    x_ticks,
    color='0.25', linewidth=0.5,
    labels=[False, False, False, True]
)


scatter = map.scatter(
    x_lon, y_lat,
    c=z, alpha=1, s=200 * norm(z),
    cmap='jet', ax=ax,
    vmin=z.min(), vmax=z.max(), zorder=4
)

cbar = map.colorbar(scatter)
cbar.set_label('Magnitude', size=14)

plt.title(plt_title, fontweight="bold")
plt.xlabel('Longitude', labelpad=40)
plt.ylabel('Latitude', labelpad=80)

plt.tight_layout()
plt.savefig(plt_fig, bbox_inches='tight', dpi=500)
