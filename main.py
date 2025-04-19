# main.py
import matplotlib.pyplot as plt
from drawer import draw_obstacles
from rrt import rrt
from rrt_star import rrt_star
import matplotlib.patches as patches


def plot_on_axis(tree, path, obstacles, ax, title):
    # Vẽ vật cản lên axis
    for (ox, oy, w, h) in obstacles:
        ax.add_patch(patches.Rectangle((ox, oy), w, h, color='gray'))
    # Vẽ các cạnh của cây
    for node in tree:
        if node.parent:
            ax.plot([node.x, node.parent.x], [node.y, node.parent.y], "-g", linewidth=0.5)
    # Vẽ đường đi tìm được
    if path:
        px, py = zip(*path)
        ax.plot(px, py, '-r', linewidth=2, label='Path')
        ax.scatter([px[0]], [py[0]], c='blue', label='Start')
        ax.scatter([px[-1]], [py[-1]], c='red', label='Goal')
    ax.set_title(title)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    ax.grid(True)
    ax.set_aspect('equal', 'box')


if __name__ == "__main__":
    print("Vẽ bản đồ (vật cản)...")
    obstacles = draw_obstacles()
    
    print("Chạy RRT...")
    tree_rrt, path_rrt = rrt((10, 10), (90, 90), obstacles)
    
    print("Chạy RRT*...")
    tree_rrt_star, path_rrt_star = rrt_star((10, 10), (90, 90), obstacles)
    
    # Hiển thị 2 plot 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plot_on_axis(tree_rrt, path_rrt, obstacles, ax1, 'RRT')
    plot_on_axis(tree_rrt_star, path_rrt_star, obstacles, ax2, 'RRT*')
    plt.show()
