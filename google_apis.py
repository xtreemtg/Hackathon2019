import googlemaps

GAPI = 'AIzaSyB1SlyO9n2uirPXWqL9O6k0k0Gx74Sqs6s'
gm = googlemaps.Client(key=GAPI)


def directions(source, dest):
    """
    Return pair of directions: by_bus, by_foot
    :param source:
    :param dest:
    """
    by_bus = gm.directions(source, dest, mode="transit")
    by_foot = gm.directions(source, dest, mode="walking")
    return by_bus, by_foot

