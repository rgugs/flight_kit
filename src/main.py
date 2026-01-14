import datetime
import geopandas as gpd
from templates import mk_kml_main, mk_kml_placemark, mk_fpl_main, mk_fpl_waypoint, mk_fpl_route_point

date_time_zulu = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

def main():
    # Import file with geopands into geodataframe - If not kml, check EPSG and convert to 4326 if needed.
    # Format into table with Waypoint name, lat, lon
    # Loop through geodataframe to create filled out lists for each type and use ''.join(list)
    # Inject into FPL and KML templates
    # Write out files
    pass

if __name__ == "__main__":
    main()