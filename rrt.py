import random
import math
from utils import Node, distance, obstacle_free, extract_path

def steer(from_node, to_node, step_size):
    #tìm khoảng cách và hướng đi từ from_node đến to_node
    # nếu khoảng cách nhỏ hơn step_size thì trả về to_node
    dist = distance(from_node, to_node)
    if dist <= step_size:
        return Node(to_node.x, to_node.y)
    angle = math.atan2(to_node.y - from_node.y, to_node.x - from_node.x)

    # tính toán tọa độ mới của node mới
    # sử dụng step_size để di chuyển từ from_node đến to_node
    return Node(from_node.x + step_size * math.cos(angle),
                from_node.y + step_size * math.sin(angle))

def rrt(start_coords, goal_coords, obstacles, iterations=1500, step_size=5):
    start = Node(*start_coords)
    goal = Node(*goal_coords)
    tree = [start]
    # tạo một cây RRT với node bắt đầu là start

    for _ in range(iterations):

        # tạo một node ngẫu nhiên trong không gian
        rand = Node(random.uniform(0, 100), random.uniform(0, 100)) # tọa độ ngẫu nhiên trong không gian 2D
        nearest = min(tree, key=lambda n: distance(n, rand)) # tìm node gần nhất trong cây đến rand
        new_node = steer(nearest, rand, step_size) # tạo node mới từ nearest đến rand

        if not obstacle_free(nearest, new_node, obstacles):
            continue # bỏ qua nếu không có đường đi từ nearest đến new_node

        # thêm new_node vào cây
        new_node.parent = nearest
        tree.append(new_node)

        # kiểm tra đã đến node đích chưa
        if distance(new_node, goal) < step_size and obstacle_free(new_node, goal, obstacles):
            goal.parent = new_node
            tree.append(goal)
            # nếu có đường đi đến node đích, thêm goal vào cây và trả về cây cùng đường đi
            return tree, extract_path(goal)

    # không tìm được đường đi đến node đích, trả về cây và đường đi rỗng
    return tree, []
