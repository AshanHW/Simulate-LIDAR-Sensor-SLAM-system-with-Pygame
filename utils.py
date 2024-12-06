import math
import numpy as np
from fractions import Fraction

# Euclidean distance between two poins
def euclidean_distance(point1, point2):
    return math.sqrt( ((point1[0]-point2[0])**2 )+ ((point1[1]-point2[1])**2) )

# Add noise to sensor data with gaussian distribution
def add_noise(distance, angle, noise):
    mean = np.array([distance, angle])
    covariance = np.diag(noise**2)

    distance, angle = np.random.multivariate_normal(mean, covariance)

    distance = max(distance, 0)
    angle = angle % (2*math.pi)

    return [distance, angle]

# Returns a point's cartesian coordiantes from a given point, distance and, angle
def get_cartesian_coords(distance, angle, position):
    x = distance * math.cos(angle) + position[0]
    y = distance * math.sin(angle) + position[1]

    return (int(x), int(y))


# Orthogonal distance from a point to a line
def dist_point2line(params, point):
    a, b, c = params
    distance = abs( a*point[0] + b*point[1] + c) / math.sqrt(a**2 + b ** 2)

    return distance


# Returns two points from a given line's slope and intersection
def get_2points_line(m, c):
    # when x = 0, y = c intercept
    x1, y1 = 0, c

    x2 = 7 # random
    y2 = m * x2 + c

    return [(x1,y1), (x2,y2)]


# returns slop and intercept from the general line form
def general_to_slope(params):
    a, b, c = params
    return -a/b, -c/a


# returs generarl line form from slop and intersection
def slope_to_general(m, c):
    slope = Fraction(m).limit_denominator()
    numerator = slope.numerator
    denominator = slope.denominator

    return (denominator, -numerator, -c*denominator)


# return intersection coordinates of two lines !!!Make sure they aren't parallel
def general_lines_intersect(params1, params2):
    a1, b1, c1 = params1
    a2, b2, c2 = params2

    x = (b2*c1 - b1*c2) / (a2*b1 - a1*b2)
    y = (a1*c2 - a2*c1) / (a2*b1 - a1*b2)

    return (x,y)


# return line's slope and intersection going through two given points
def points_2line(point1, point2):
    if point1[0] == point2[0]: # vertical line. Slope is undefined
        pass # TODO: Compatibility
    else:
        m = point1[1] - point2[1] / (point1[0] - point2[0])
        c = point1[1] - m * point1[0]
        return m, c


# return coordinates of a orthogonal projection of a point onto a line
def projection_point(point, m, c):
    x = ( point[0] + point[1] * m - c * m) / (1+m**2)
    y = m * x + c

    return (x,y)


# return y value from a given slope intersection and x coord
def get_y(m, c, x):
    return m*x + c




