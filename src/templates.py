# KML 
def mk_kml_main(output_kml_filename: str, kml_placemark_list: list[str]):
    """
    Returns string of final kml output to write to file.
    """
    return f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
        <name>{output_kml_filename}.kml</name>
        <Folder>
            <name>{output_kml_filename}</name>
            {kml_placemark_list}
        </Folder>
    </Document>
    """

def mk_kml_placemark(waypoint_id: str, longitude: float, latitude: float, altitude: int):
    """
    Returns string for each placemark. Append result to kml_placemark_list for use in mk_kml_main().
    """
    return f"""
    <Placemark>
        <name>{waypoint_id}</name>
        <Point>
            <coordinates>{longitude},{latitude},{altitude}</coordinates>
        </Point>
    </Placemark>
    """

# FPL
def mk_fpl_main(date_time_zulu: str, fpl_waypoint_list: list[str], waypoint_prefix: str, fpl_route_list: list[str]):
    """
    Returns string of final fpl output to write to file.
    """
    return f"""
    <?xml version="1.0" encoding="utf-8"?>
    <flight-plan xmlns="http://www8.garmin.com/xmlschemas/FlightPlan/v1">
    <created>{date_time_zulu}</created>
    <waypoint-table>
        {fpl_waypoint_list}
    </waypoint-table
    <route>
        <route-name>ROUTE-{waypoint_prefix}</route-name>
        {fpl_route_list} 
    </route>
    </flight-plan>
    """

def mk_fpl_waypoint(waypoint_id: str, latitude: float, longitude: float):
    """
    Returns string for each input waypoint. Append result to fpl_waypoint_list for use in mk_fpl_main().
    """
    return f"""
    <waypoint>
        <identifier>{waypoint_id}</identifier>
        <type>USER WAYPOINT</type>
        <country-code></country-code>
        <lat>{latitude}</lat>
        <lon>{longitude}</lon>
        <comment></comment>
    </waypoint>\n
    """

def mk_fpl_route_point(waypoint_id: str):
    """
    Returns string for each input route point. Append result to fpl_route_list for use in mk_fpl_main().
    """
    return f"""
    <route-point>
        <waypoint-identifier>{waypoint_id}</waypoint-identifier>
        <waypoint-type>USER WAYPOINT</waypoint-type>
        <waypoint-country-code></waypoint-country-code>
    </route-point>\n
    """