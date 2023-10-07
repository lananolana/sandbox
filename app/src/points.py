import math


def calculate_distance(point1, point2):
    """
    Distance between two points on a plane
    """
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]

    return math.sqrt((delta_x ** 2) + (delta_y ** 2))


def get_mid_point(point1, point2):
    """
    Search a point midway between two specified points
    """
    middle_point = {
      "x": (point1["x"] + point2["x"]) / 2,
      "y": (point1["y"] + point2["y"]) / 2
    }

    return middle_point


def make_point(x, y):
    """
    Converting Cartesian system coordinates to polar
    """
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_angle(point):
    return point["angle"]


def get_radius(point):
    return point["radius"]


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def convert_x_to_decart(point):
    """
    Converting x coordinate from polar to decart system
    """
    return get_radius(point) * math.cos(get_angle(point))


def convert_y_to_decart(point):
    """
    Converting y coordinate from polar to decart system
    """
    return get_radius(point) * math.sin(get_angle(point))


def get_quadrant(point):
    """
    Determining the quadrant in which a point is located
    """
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None
