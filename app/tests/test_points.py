from src.points import *
from src.segments import *


def test_points():
    assert calculate_distance([0, 0], [3, 4]) == 5
    assert calculate_distance([-1, -4], [-1, -10]) == 6
    assert calculate_distance([1, 10], [1, 3]) == 7


def test_mid_point():
    point1 = {'x': 0, 'y': 0}
    point2 = {'x': 4, 'y': 4}
    assert get_mid_point(point1, point2) == {'x': 2, 'y': 2}

    point3 = {'x': -1, 'y': 10}
    point4 = {'x': 0, 'y': -3}
    assert get_mid_point(point3, point4) == {'x': -0.5, 'y': 3.5}


def test_segments():
    begin_point = make_decart_point(4, 2)
    end_point = make_decart_point(0, 0)
    segment = make_segment(begin_point, end_point)
    assert get_begin_point(segment) == begin_point
    assert get_end_point(segment) == end_point
    assert make_decart_point(2, 1) == get_mid_point_of_segment(segment)

    segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
    assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)
