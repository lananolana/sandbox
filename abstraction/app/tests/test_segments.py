from src.points import make_point
from src.segments import *


def test_segments():
    begin_point = make_decart_point(4, 2)
    end_point = make_decart_point(0, 0)
    segment = make_segment(begin_point, end_point)
    assert get_begin_point(segment) == begin_point
    assert get_end_point(segment) == end_point
    assert make_decart_point(2, 1) == get_mid_point_of_segment(segment)

    segment2 = make_segment(make_decart_point(3, 2), make_decart_point(2, 3))
    assert make_decart_point(2.5, 2.5) == get_mid_point_of_segment(segment2)


def test_segment():
    point1 = make_point(3, 2)
    point2 = make_point(0, 0)
    point3 = make_point(3, -5)
    assert is_parallel_with_y(make_segment(point1, point2)) is False
    assert is_parallel_with_y(make_segment(point1, point3)) is True
    assert is_parallel_with_x(make_segment(point2, point3)) is False
