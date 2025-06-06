# obstacles.py

# Mỗi vật cản: [x, y, w, h]
simple_obstacles = [
    [20, 20, 10, 30],
    [50, 50, 15, 15],
    [70, 10, 20, 10],
    [10, 70, 30, 10]
]

id_obstacles = [
    [0, 75, 55, 5],
    [25, 50, 40, 5],
    [40, 10, 60, 5],
    [70, 60, 30, 5],

    [40, 10, 5, 20],
    [50, 50, 5, 20],
    [55, 40, 5, 10]


]

trap_corridor_obstacles = [
    [10, 20, 80, 5],
    [0, 60, 80, 5],

    [85, 0, 5, 25],
    [10, 40, 5, 25],
    [85, 40, 5, 25],

    [30, 45, 5, 15],
    [50, 45, 5, 15],
    [70, 45, 5, 15],
]

snaking_path_obstacles = [
    [0, 20, 80, 5],
    [20, 40, 80, 5],
    [0, 60, 80, 5],
    [20, 80, 80, 5],
    
    [75, 20, 5, 25],
    [15, 40, 5, 25],
    [75, 60, 5, 25],
    [15, 80, 5, 20]
]


blocking_path_obstacles = [
    [40, 0, 10, 60],
    [60, 40, 10, 60],
    [20, 20, 10, 10],
    [80, 80, 15, 15]
]

city_map_obstacles = [
    [10, 10, 10, 10],
    [30, 10, 10, 10],
    [50, 10, 10, 10],
    [70, 10, 10, 10],
    [10, 30, 10, 10],
    [30, 30, 10, 10],
    [50, 30, 10, 10],
    [70, 30, 10, 10],
    [10, 50, 10, 10],
    [30, 50, 10, 10]
]

narrow_passage_obstacles = [
    [20, 0, 10, 80],
    [70, 20, 10, 80],
    [40, 20, 10, 60]
]

maze_obstacles = [
    [0, 0, 100, 5],     # Tường trên
    [0, 95, 100, 5],    # Tường dưới
    [0, 0, 5, 100],     # Tường trái
    [95, 0, 5, 100],    # Tường phải

    # Các tường bên trong
    [10, 5, 5, 60],
    [10, 65, 60, 5],
    [65, 20, 5, 50],
    [30, 20, 35, 5],
    [30, 25, 5, 35],
    [35, 55, 30, 5],
    [60, 35, 5, 20],
    [20, 35, 40, 5],
    [20, 35, 5, 25],
    [20, 60, 25, 5],
    [45, 60, 5, 20],
    [50, 75, 30, 5],
    [75, 50, 5, 30],
    [75, 50, 15, 5],
    [85, 20, 5, 30]
]

# Danh sách gộp để dễ lựa chọn
all_maps = {
    "simple": simple_obstacles,
    "blocking_path": blocking_path_obstacles,
    "city_map": city_map_obstacles,
    "narrow_passage": narrow_passage_obstacles
}
