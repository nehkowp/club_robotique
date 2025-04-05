import math

# distance(client.robots['green'][1],client.ball)
def distance(robot1,ball):
    return math.sqrt(((ball[0]-robot1[0])**2) + ((ball[1]-robot1[1])**2))

print(distance([2,3,5],[5,4]))