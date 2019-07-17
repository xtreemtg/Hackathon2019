import googlemaps

GAPI = 'AIzaSyB1SlyO9n2uirPXWqL9O6k0k0Gx74Sqs6s'
gm = googlemaps.Client(key=GAPI)

gm.di


def directions(source, dest):
    bus_directions = gm.directions(source,
                                   dest,
                                   mode="transit")
