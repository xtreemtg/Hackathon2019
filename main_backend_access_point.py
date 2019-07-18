from flask import request
from geopy import distance
from math import sin, cos, atan2, sqrt

from google_apis import nearby_landmarks


def scenic_route(start, end):
    middle = middle_point(start, end)
    radius = distance.great_circle(middle, end)
    landmarks = nearby_landmarks(middle, radius=radius)



def middle_point(start, end):
    s_lat, s_lng = start
    e_lat, e_lng = end
    bx = cos(e_lat) * cos(e_lng - s_lng)
    by = cos(e_lat) * sin(e_lng - s_lng)
    mid_lat = atan2(sin(s_lat) + sin(e_lat), sqrt((cos(s_lat) + bx) * (cos(s_lat) + bx) + by * by))
    mid_lng = s_lng + atan2(by, cos(s_lat) + bx)
    return mid_lat, mid_lng


def flask_scenic_route():
    start = request.args.get('start')
    end = request.args.get('end')
    return scenic_route(start, end)
