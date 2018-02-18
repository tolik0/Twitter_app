import folium
import geopy


def make_coordinates(users):
    """
    (dict) -> (dict)
    Return dict with coordinates as key and name as value
    """
    new_users = dict()
    geocoder = geopy.geocoders.ArcGIS()
    for user in users:
        try:
            user_loc = geocoder.geocode(user["location"])
            if user_loc:
                la = user_loc.latitude
                lo = user_loc.longitude
                if (la, lo) not in new_users:
                    new_users[(la, lo)] = "<li>{}</li>".format(user["screen_name"])
                else:
                    new_users[(la, lo)]+="<li>{}</li>".format(user["screen_name"])
        except:
            pass
    for user in new_users:
        new_users[user] = '<div style="max-height: 100px; overflow-y: ' \
                            'scroll;"><ul>' + new_users[user] + '</ul></div>'
    return new_users


def map_create(users):
    """
    (dict, int, int) -> None
    Create map with markers of names
    """
    # create map
    map = folium.Map()
    # add users to map
    fg = folium.FeatureGroup("Users")
    for user in users:
        try:
            fg.add_child(folium.Marker(location=user, popup=users[user]))
        except:
            pass
    map.add_child(fg)
    return map.get_root().render()
