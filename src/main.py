import datetime
import geopandas as gpd
from templates import mk_kml_main, mk_kml_placemark, mk_fpl_main, mk_fpl_waypoint, mk_fpl_route_point

date_time_zulu = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")


# Hard coded for now, eventually access with flag
waypoint_prefix = "A"

def import_file(input_file: str):
    gdf = gpd.read_file(input_file)




def main():
    # Use pathlib to get path from sys.argv
    # Import file with geopands into geodataframe - If not kml, check EPSG and convert to 4326 if needed.
    # Format into table with Waypoint name, lat, lon
    # Loop through geodataframe to create filled out lists for each type and use ''.join(list)
    # Inject into FPL and KML templates
    # Write out files
    output_kml = mk_kml_main(output_filename, kml_placemark_list)
    output_fpl = mk_fpl_main(date_time_zulu,waypoint_prefix, fpl_waypoint_list, fpl_route_list)

if __name__ == "__main__":
    main()