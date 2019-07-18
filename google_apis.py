import googlemaps



OPTIONS = {
    'green': ['amusement_park','bar', 'book_store', 'city_hall', 'embassy',  'insurance_agency', 'library','restaurant'],
    'water': ['liquor_store', 'mosque', 'local_government_office',  'museum',  'park',],
    'sea': ['aquarium','shopping_mall', 'stadium', 'synagogue', 'zoo'],
    'city-landscape': ['art_gallery', 'bowling_alley', 'cafe','church','hindu_temple','mosque','night_club',]
}


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


def directions(origin, destination, *waypoints):
    """
    Return directions by foot, through waypoints, optimized.
    :param origin:
    :param destination:
    """
    gm = googlemaps.Client(key=GAPI)
    # by_bus = gm.directions(source, dest, mode="transit")
    by_foot = gm.directions(origin, destination, waypoints=waypoints, mode="walking", optimize_waypoints=True)
    return by_foot
