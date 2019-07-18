import googlemaps

INTERESTING_LANDMARK_TYPES = ['amusement_park', 'aquarium', 'art_gallery', 'bar', 'book_store', 'bowling_alley', 'cafe',
                              'casino', 'church', 'city_hall', 'embassy', 'hindu_temple', 'insurance_agency', 'library',
                              'local_government_office', 'mosque', 'museum', 'night_club', 'park', 'restaurant',
                              'shopping_mall', 'stadium', 'synagogue', 'zoo']
GAPI = 'AIzaSyB1SlyO9n2uirPXWqL9O6k0k0Gx74Sqs6s'


def nearby_landmarks(coordinates, radius, type_=INTERESTING_LANDMARK_TYPES):
    gm = googlemaps.Client(key=GAPI)
    return gm.places_nearby(coordinates, radius=radius, type=type_)['results']


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


def directions(source, dest):
    """
    Return pair of directions: by_bus, by_foot
    :param source:
    :param dest:
    """
    gm = googlemaps.Client(key=GAPI)
    by_bus = gm.directions(source, dest, mode="transit")
    by_foot = gm.directions(source, dest, mode="walking")
    return by_bus, by_foot
