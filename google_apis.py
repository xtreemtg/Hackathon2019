from functools import reduce

import googlemaps

GAPI = 'AIzaSyB1SlyO9n2uirPXWqL9O6k0k0Gx74Sqs6s'

OPTIONS = {
    'green': ['amusement_park', 'bar', 'book_store', 'city_hall', 'embassy', 'insurance_agency', 'library',
              'restaurant'],
    'water': ['liquor_store', 'mosque', 'local_government_office', 'museum', 'park', ],
    'sea': ['aquarium', 'shopping_mall', 'stadium', 'synagogue', 'zoo'],
    'city-landscape': ['art_gallery', 'bowling_alley', 'cafe', 'church', 'hindu_temple', 'mosque', 'night_club', ]
}

types = ['accounting', 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'atm', 'bakery', 'bank', 'bar',
         'beauty_salon', 'bicycle_store', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground',
         'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetery', 'church', 'city_hall',
         'clothing_store', 'convenience_store', 'courthouse', 'dentist', 'department_store', 'doctor', 'electrician',
         'electronics_store', 'embassy', 'fire_station', 'florist', 'funeral_home', 'furniture_store', 'gas_station',
         'gym', 'hair_care', 'hardware_store', 'hindu_temple', 'home_goods_store', 'hospital', 'insurance_agency',
         'jewelry_store', 'laundry', 'lawyer', 'library', 'liquor_store', 'local_government_office', 'locksmith',
         'lodging', 'meal_delivery', 'meal_takeaway', 'mosque', 'movie_rental', 'movie_theater', 'moving_company',
         'museum', 'night_club', 'painter', 'park', 'parking', 'pet_store', 'pharmacy', 'physiotherapist', 'plumber',
         'police', 'post_office', 'real_estate_agency', 'restaurant', 'roofing_contractor', 'rv_park', 'school',
         'shoe_store', 'shopping_mall', 'spa', 'stadium', 'storage', 'store', 'subway_station', 'supermarket',
         'synagogue', 'train_station', 'taxi_stand', 'transit_station', 'travel_agency', 'veterinary_care', 'zoo']


def nearby_landmarks(coordinates, radius, type_= 'all'):
    gm = googlemaps.Client(key=GAPI)
    if type_ == 'all':
        typ = reduce(lambda x, y:x + y, OPTIONS.values())
    else: typ = OPTIONS[type_]

    return gm.places_nearby(coordinates, radius=radius.m, type=typ)['results']


def get_coordinates(origin, destination):
    gm = googlemaps.Client(key=GAPI)
    origin = gm.geocode(origin)[0]['geometry']['location'].values()
    destination = gm.geocode(destination)[0]['geometry']['location'].values()
    return origin, destination


def directions(origin, destination, *waypoints):
    """
    Return directions by foot, through waypoints, optimized.
    :param origin:
    :param destination:
    """
    gm = googlemaps.Client(key=GAPI)
    # by_bus = gm.directions(source, dest, mode="transit")
    waypoints = [list(w) for w in waypoints]
    by_foot = gm.directions(origin, destination, waypoints=waypoints, mode="walking", optimize_waypoints=True)
    legs = by_foot[0]['legs']
    sorted_by_foot = [list(leg['start_location'].values()) for leg in legs]
    return sorted_by_foot
