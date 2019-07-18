from itertools import permutations
from flask import request
from geopy import distance
from math import sin, cos, atan2, sqrt, radians, degrees
from google_apis import nearby_landmarks, directions, get_coordinates

MAX_LANDMARKS = 10


def find_lndmrk_by_coords(coords, landmarks_to_go_through):
    for lndmrk in landmarks_to_go_through:
        if landmark_coords(lndmrk) == coords:
            return lndmrk


def landmark_coords(lndmrk):
    return lndmrk['geometry']['location'].values()


def get_coords(origin, destination):
    return get_coordinates(origin, destination)


def scenic_route(origin, destination):
    landmarks_to_go_through = get_landmarks_in_area(origin, destination)
    coordinate_list = [landmark_coords(lndmrk) for lndmrk in landmarks_to_go_through]
    shortest_path = None
    lowest_weight = None
    for p in permutations(coordinate_list):
        weight = distance.great_circle(p).m
        if lowest_weight is None or weight < lowest_weight:
            lowest_weight = weight
            shortest_path = p
    #     I have shortest_path!
    ordered_landmarks = [find_lndmrk_by_coords(coords, landmarks_to_go_through) for coords in shortest_path]
    return ordered_landmarks


def get_landmarks_in_area(origin, destination, types, max_=MAX_LANDMARKS):
    middle = middle_point(origin, destination)
    radius = distance.great_circle(middle, destination)
    sorted_landmarks = nearby_landmarks(middle, radius, types)
    landmarks_to_go_through = sorted_landmarks[:max_]
    return landmarks_to_go_through


def middle_point(start, end):
    s_lat, s_lng = start
    e_lat, e_lng = end
    s_lat, s_lng, e_lat, e_lng = radians(s_lat), radians(s_lng), radians(e_lat), radians(e_lng)
    bx = cos(e_lat) * cos(e_lng - s_lng)
    by = cos(e_lat) * sin(e_lng - s_lng)
    mid_lat = atan2(sin(s_lat) + sin(e_lat), sqrt((cos(s_lat) + bx) * (cos(s_lat) + bx) + by * by))
    mid_lng = s_lng + atan2(by, cos(s_lat) + bx)
    return degrees(mid_lat), degrees(mid_lng)


def flask_scenic_route():
    start = request.args.get('start')
    end = request.args.get('end')
    max_ = request.args.get('max')
    types = None
    landmarks = get_landmarks_in_area(start, end, types, max_)
    trail = directions(start, end, *[landmark_coords(lndmrk) for lndmrk in landmarks])
    return trail
