import random
import math
from utils import Node, distance, obstacle_free, extract_path

def steer(from_node, to_node, step_size):
    # tìm khoảng cách và hướng đi từ from_node đến to_node
    # nếu khoảng cách nhỏ hơn step_size thì trả về to_node
    dist = distance(from_node, to_node)
    if dist <= step_size:
        return Node(to_node.x, to_node.y)
    angle = math.atan2(to_node.y - from_node.y, to_node.x - from_node.x)

    # tính toán tọa độ mới của node mới
    # sử dụng step_size để di chuyển từ from_node đến to_node
    return Node(from_node.x + step_size * math.cos(angle),
                from_node.y + step_size * math.sin(angle))

# hàm tìm những node gần nhất trong cây
def get_nearby_nodes(tree, node, radius):
    return [n for n in tree if distance(n, node) <= radius]

def rrt_star(start_coords, goal_coords, obstacles, iterations=1500, step_size=5, radius=15):
    # cơ bản là giống như hàm rrt nhưng có thêm bước tối ưu hóa
    start = Node(*start_coords)
    goal = Node(*goal_coords)
    tree = [start]

    for _ in range(iterations):
        # tạo một node ngẫu nhiên trong không gian
        rand = Node(random.uniform(0, 100), random.uniform(0, 100))
        nearest = min(tree, key=lambda n: distance(n, rand))
        new_node = steer(nearest, rand, step_size)

        if not obstacle_free(nearest, new_node, obstacles):
            continue

        # thêm new_node vào cây, cập nhật cost và parent
        new_node.cost = nearest.cost + distance(nearest, new_node)
        new_node.parent = nearest

        # duyệt qua các node lân cận để tìm node tối ưu hơn
        # nếu có node nào gần hơn và có đường đi đến new_node thì cập nhật parent và cost
        near_nodes = get_nearby_nodes(tree, new_node, radius)
        for near in near_nodes:
            if obstacle_free(near, new_node, obstacles):
                new_cost = near.cost + distance(near, new_node)
                if new_cost < new_node.cost:
                    new_node.parent = near
                    new_node.cost = new_cost

        tree.append(new_node) # thêm new_node vào cây

        for near in near_nodes:
            if obstacle_free(new_node, near, obstacles):
                new_cost = new_node.cost + distance(new_node, near)
                if new_cost < near.cost:
                    near.parent = new_node
                    near.cost = new_cost

        if distance(new_node, goal) < step_size and obstacle_free(new_node, goal, obstacles):
            goal.parent = new_node
            tree.append(goal)
            return tree, extract_path(goal)

    return tree, []
