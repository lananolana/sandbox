from points import get_x, get_y, make_decart_point


def make_segment(point1, point2):
    """
    Takes two points as input and returns a segment
    """
    return {'begin_point': point1, 'end_point': point2}


def get_begin_point(segment):
    """
    Takes a segment as input and returns the begin point of the segment
    """
    return segment["begin_point"]


def get_end_point(segment):
    """
    Takes a segment as input and returns the end point of the segment
    """
    return segment["end_point"]


def get_mid_point_of_segment(segment):
    """
    Takes a segment as input and returns the middle point of the segment
    """
    begin_point = get_begin_point(segment)
    end_point = get_end_point(segment)

    x = (get_x(begin_point) + get_x(end_point)) / 2
    y = (get_y(begin_point) + get_y(end_point)) / 2

    return make_decart_point(x, y)
