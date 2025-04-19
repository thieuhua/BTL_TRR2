import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0

def distance(n1, n2):
    return math.hypot(n1.x - n2.x, n1.y - n2.y)

def is_inside_obstacle(x, y, obstacles):
    for (ox, oy, w, h) in obstacles:
        if ox <= x <= ox + w and oy <= y <= oy + h:
            return True
    return False

def obstacle_free(a, b, obstacles, steps=10):
    for i in range(steps + 1):
        t = i / steps
        x = a.x + t * (b.x - a.x)
        y = a.y + t * (b.y - a.y)
        if is_inside_obstacle(x, y, obstacles):
            return False
    return True

def extract_path(node):
    path = [(node.x, node.y)]
    while node.parent:
        node = node.parent
        path.append((node.x, node.y))
    return path[::-1]
