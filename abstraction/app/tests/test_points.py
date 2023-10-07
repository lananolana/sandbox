from src.points import calculate_distance, get_mid_point


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
