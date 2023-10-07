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

def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]
