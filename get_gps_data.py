from gps import *

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

def get_coordinates(gpsd):
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        longitude = getattr(nx, 'lon', "Unknown")
        latitude = getattr(nx, 'lat', "Unknown")
        return (longitude, latitude)
    return None


coords = get_coordinates(gpsd)

print(f"Coordinates: {coords}")
