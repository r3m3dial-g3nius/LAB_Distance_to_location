# distance to Point p
# user inputs (x,y) for point p, x increments and y increments for each interation starting at origin
# each 3rd iteration, reverse steps in x AND y from user input
# calculates shortest distance and iteration number


import math


# Point class
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


# Main program
# Read in x and y for Point P
p = Point()
p.x = int(input('Enter X value for point p: '))
p.y = int(input('Enter Y value for point p: '))

# Read in num of steps to be taken in X and Y directions
steps_in_x = int(input('Enter increment in x: '))
steps_in_y = int(input('Enter increment in y: '))

# Read in num of steps to be taken (backwards) every 3 steps
steps_backwards = int(input('Enter reverse increment in x and y for every 3rd iteration: '))

# Write dynamic programming algorithm
current = Point()
current.x = 0
current.y = 0
dist_to_current = 0

previous = Point()
previous.x = 0
previous.y = 0
dist_to_previous = 0

arrival = Point()
arrival.x = 0
arrival.y = 0

counter = 0
working = True

while working:
    counter += 1
    previous.x = current.x
    previous.y = current.y
    current.x += steps_in_x
    current.y += steps_in_y
    # on 3rd iteration, step backwards
    if counter % 3 == 0:
        current.x -= steps_backwards
        current.y -= steps_backwards
    dist_to_current = math.sqrt(math.pow((p.x - current.x), 2) + math.pow((p.y - current.y), 2))
    # print(f'Iteration: {counter}, Current x: {current.x}, Current y: {current.y}, Distance to current: {
    # dist_to_current}')
    dist_to_previous = math.sqrt(math.pow((p.x - previous.x), 2) + math.pow((p.y - previous.y), 2))
    if dist_to_current == 0:
        arrival.x = current.x
        arrival.y = current.y
        working = False
    elif dist_to_previous < dist_to_current:
        arrival.x = previous.x
        arrival.y = previous.y
        counter -= 1
        working = False
    else:
        arrival.x = current.x
        arrival.y = current.y


dist_to_arrival = math.sqrt(math.pow((p.x - arrival.x), 2) + math.pow((p.y - arrival.y), 2))
formatted_DTA = '{:.6f}'.format(dist_to_arrival)


# Output
print(f'Point P: ({p.x},{p.y})')
print(f'Arrival Point: ({arrival.x},{arrival.y})')
print(f'Distance between P and arrival: {formatted_DTA}')
print(f'Number of iterations: {counter}')
