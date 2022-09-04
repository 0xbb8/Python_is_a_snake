# calculate the value of Pi using random.uniform() function
import random

def calculate_pi(points):
    # initializing
    points_inside_circle = 0
    points_inside_square = 0

    for _ in range(points):
        # random points distributed randomly
        x = random.uniform(0,1)
        y = random.uniform(0,2)
        # calculate the distance from the center to the plotted points
        distance_to_points = (x**2 + y**2)**(1/2)
        if distance_to_points < 1:
            points_inside_circle += 1
        points_inside_square += 1
    return 4 * (points_inside_circle/points_inside_square)
