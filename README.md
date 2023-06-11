# Download-Earthquake-Data-
For Southeast Tibet



# Explaination of For the Getting Event Data
1. The necessary libraries are imported, including os, obspy, numpy, pandas, matplotlib.pyplot, Normalize from matplotlib.colors, and Basemap from mpl_toolkits.basemap. These libraries are used for many different things, including processing files, manipulating data, charting, and visualizing maps. 
2. Folder_output specifies the folder path where the output files should be stored, and os.makedirs() creates the folder if it doesn't already exist.
3. The excel_filename and excel_tab variables each contain the name of the Excel file and tab.
4. Obspy.UTCDateTime is used to set the beginning and ending times for data retrieval. These show the time frame for which seismic events will be fetched.
5. The "USGS" value, which designates the data source, is used to define the FDSN client.
6. The minimum, and maximum latitude and longitude values (minlatitude, maxlatitude, minlongitude, and maxlongitude.) are set for the map's extent.
7. The terms "minmagnitude" and "maxmagnitude" describe the earthquake events' minimum and highest magnitudes.
8. Obspy.clients.fdsn.Client(client) is used to create the FDSN client.
9. The FDSN client's get_events() method is used to retrieve the seismic events. The latitude and longitude range, start and end times, and lowest and maximum magnitudes are among the method parameters.
10. The console prints information about the events that were fetched.
11. The events are kept in df, a Pandas DataFrame. The columns listed in feature_list and an empty structure are used to initialise the DataFrame.
12. Each event that is fetched is iterated over in a loop. The df.append() method is used inside the loop to extract pertinent data from each event, such as the origin time, latitude, longitude, depth, event type, magnitude, magnitude type, creation information, and event description, and add it as a new row to the DataFrame.
13. The DataFrame is then saved using df.to_excel() to an Excel file that is defined by excel_output. One sheet with the name excel_tab will be present in the Excel file.
14. The events are then plotted on a map using Basemap and Matplotlib in the code. The plot title, text size, tick intervals, and other settings and parameters are all defined.
15. Variables x, y, and z are each given values from the DataFrame for longitude, latitude, and magnitude.
16. The projection and map extent that are supplied when creating the Basemap instance.
17. The Basemap techniques are used to draw the map's details, including the coasts, boundaries, continents, countries, parallels, and meridian lines.
18. The scatter spots on the map represent the earthquake incidents. The magnitude values dictate the size and colour of the points, resulting in a color-coded representation of the earthquake magnitudes.
19. The magnitude scale is indicated on the plot by a colorbar.
20. Plot.savefig() is then used to save the plot as a PNG picture.




