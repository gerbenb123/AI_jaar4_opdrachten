# A) Tussen de 0 en 10 procent
# B) 1.733 seconden en een afstand van 19627.5
# C) Hoe je een intersectie tussen twee edges kan vinden staat uitgelegd in de functie "check_crossing".
# Bij het verwijderen van een kruizing moet er gelet worden op dat de dichstbijzijnde steden worden gekoppeld aan elkaar.
#
#
#


import matplotlib.pyplot as plt
import random
import time
import itertools
import math
from collections import namedtuple

# based on Peter Norvig's IPython Notebook on the TSP

City = namedtuple('City', 'x y')


def distance(A, B):
    return math.hypot(A.x - B.x, A.y - B.y)


def try_all_tours(cities):
    # generate and test all possible tours of the cities and choose the shortest tour
    tours = alltours(cities)
    return min(tours, key=tour_length)


def nearest_neighbour(cities):
    visited_cities = []
    initial_city = next(iter(cities))
    visited_cities.append(initial_city)
    current_city = initial_city

    while len(visited_cities) != len(cities):
        nearest_city = []
        lowest_distance = 10000
        for city in cities:
            if city not in visited_cities and distance(current_city, city) < lowest_distance:
                nearest_city = city
                lowest_distance = distance(current_city, city)
        visited_cities.append(nearest_city)
        current_city = nearest_city

    return visited_cities

def two_opt(cities):
    city_path = nearest_neighbour(cities)

    # checks all the edges on possible intersections (this makes it way slower when the amount of cities become higher)
    index = 0
    #TODO(final to the first node should also be taken in the equation)
    while index != len(city_path) -1:
        for city_index in range(0, len(city_path)-1):
            index += 1
            for other_city_index in range(0, len(city_path)-1):
                if abs(city_index - other_city_index) > 2 and check_crossing([city_path[city_index], city_path[city_index + 1], city_path[other_city_index], city_path[other_city_index + 1]]):
                    # replaces edges between cities
                    if distance(city_path[city_index], city_path[other_city_index]) + distance(city_path[city_index + 1], city_path[other_city_index + 1]) < distance(city_path[city_index + 1], city_path[other_city_index]) + distance(city_path[city_index], city_path[other_city_index + 1]):
                        new_city_value = city_path[city_index + 1]
                        new_other_city_value = city_path[other_city_index]
                        city_path[other_city_index] = new_city_value
                        city_path[city_index + 1] = new_other_city_value
                    else:
                        new_city_value = city_path[city_index]
                        new_other_city_value = city_path[other_city_index]
                        city_path[other_city_index] = new_city_value
                        city_path[city_index] = new_other_city_value
                    index = 0
                    break
            if index == 0:
                break

    return city_path


# Knowing that 3 cities are colinear, checks if city_c is on the route between city_a and city_b
def on_line(city_a, city_b, city_c):
    if max(city_a.x, city_b.x) >= city_c.x >= min(city_a.x, city_b.x) and \
            max(city_a.y, city_b.y) >= city_c.y >= min(city_a.y, city_b.y):
        return True
    return False


def check_crossing(cities):
    # city 1 and 2 share an edge and city 3 and 4 share an edge
    # There are 4 orientations needed to check if there is an intersection.
    # Checks the orientation that are needed for deciding if there is an intersection
    orientation_1 = orientation(cities[0], cities[1], cities[2])
    orientation_2 = orientation(cities[0], cities[1], cities[3])
    orientation_3 = orientation(cities[2], cities[3], cities[0])
    orientation_4 = orientation(cities[2], cities[3], cities[1])

    # the orientation of an edge and one city of the other edge can't be the same as the orientation of the edge and
    # other city of the other edge
    if (orientation_1 != orientation_2) and (orientation_3 != orientation_4):
        return True

    # these are the special cases in which one orientation is colinear.
    if (orientation_1 == 0 and on_line(cities[0], cities[1], cities[2])) or \
            (orientation_2 == 0 and on_line(cities[0], cities[1], cities[3])) or \
            (orientation_3 == 0 and on_line(cities[2], cities[3], cities[0])) or \
            (orientation_4 == 0 and on_line(cities[2], cities[3], cities[1])):
        return True

    # if no intersection has been found.
    return False


def orientation(city_a, city_b, city_c):
    # checks the orientation of three cities based on the difference in slopes of routes between cities a and b
    # and c and a. If the slope between cities A and B is steeper than the orientation is clockwise.
    orientation_value = (float(city_b.y - city_a.y) * (city_c.x - city_b.x)) - (
            float(city_b.x - city_a.x) * (city_c.y - city_b.y))
    if orientation_value > 0:
        return 1  # clockwise
    elif orientation_value < 1:
        return 2  # counter clockwise
    else:
        return 0  # colinear


def alltours(cities):
    # return a list of tours (a list of lists), each tour a permutation of cities,
    # and each one starting with the same city
    # cities is a set, sets don't support indexing
    start = next(iter(cities))
    return [[start] + list(rest)
            for rest in itertools.permutations(cities - {start})]


def tour_length(tour):
    # the total of distances between each pair of consecutive cities in the tour
    return sum(distance(tour[i], tour[i - 1])
               for i in range(len(tour)))


def make_cities(n, width=1000, height=1000):
    # make a set of n cities, each with random coordinates within a rectangle (width x height).

    random.seed()  # the current system time is used as a seed
    # note: if we use the same seed, we get the same set of cities

    return frozenset(City(random.randrange(width), random.randrange(height))
                     for c in range(n))


def plot_tour(tour):
    # plot the cities as circles and the tour as lines between them
    points = list(tour) + [tour[0]]
    plt.plot([p.x for p in points], [p.y for p in points], 'bo-')
    plt.axis('scaled')  # equal increments of x and y have the same length
    plt.axis('off')
    plt.show()


def plot_tsp(algorithm, cities):
    # apply a TSP algorithm to cities, print the time it took, and plot the resulting tour.
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    print("{} city tour with length {:.1f} in {:.3f} secs for {}"
          .format(len(tour), tour_length(tour), t1 - t0, algorithm.__name__))
    print("Start plotting ...")
    plot_tour(tour)


if __name__ == '__main__':
    seed = make_cities(20)
    # plot_tsp(try_all_tours, seed)

    plot_tsp(nearest_neighbour, seed)
    plot_tsp(two_opt, seed)
