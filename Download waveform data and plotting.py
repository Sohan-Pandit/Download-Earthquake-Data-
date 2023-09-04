import obspy
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt

# Replace the following values with your desired information
station_network = "II"  # Replace XX with the network code of your seismic station
station_code = "LVZ"  # Replace XXXX with the station code of your seismic station
station_location = "00"  # Replace 00 with the location code of your seismic station
station_channel = "BHZ"  # Replace HHZ with the channel code of your seismic station
start_date = "2023-02-06"  # Replace YYYY-MM-DD with your desired start date

# Create a client to access earthquake data from a FDSN web service2023-02-06
client = Client("IRIS")  # You can use other providers supported by ObsPy

# Convert the start_date to UTCDateTime format
start_time = UTCDateTime(start_date)

# Define the end_time as 10 AM on the start_date
end_time = start_time + 172000  # 36000 seconds = 10 hours

# Download the earthquake data for the specified station and time range
st = client.get_waveforms(network=station_network, station=station_code,
                          location=station_location, channel=station_channel,
                          starttime=start_time, endtime=end_time)

# Plot the downloaded waveform data
st.plot(size=(800, 600))
plt.show()
print(st)
