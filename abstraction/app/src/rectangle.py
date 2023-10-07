from points import get_quadrant, get_x, get_y, make_decart_point


def make_rectangle(point, width, height):
    """
    Creates a rectangle, taking the top-left point, width and height as inputs
    """
    return {
        "point": point,
        "width": width,
        "height": height,
    }


def get_start_point(rectangle):
    """
    Selector for the start point
    """
    return rectangle['point']


def get_width(rectangle):
    """
    Selector for the width
    """
    return rectangle['width']


def get_height(rectangle):
    """
    Selector for the height
    """
    return rectangle['height']


def contains_origin(rectangle):
    """
    Checks if the coordinate center belongs to the rectangle
    """
    point1 = get_start_point(rectangle)
    point2 = make_decart_point(
        get_x(point1) + get_width(rectangle),
        get_y(point1) - get_height(rectangle),
    )

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4
