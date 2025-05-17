import matplotlib.pyplot as plt
from drawer import draw_obstacles
from rrt import rrt
import obstacles_EX
import matplotlib.patches as patches


def plot_result(tree, path, obstacles, title):
    fig, ax = plt.subplots(figsize=(10, 10))
    # Ve vat can
    for (ox, oy, w, h) in obstacles:
        ax.add_patch(patches.Rectangle((ox, oy), w, h, color='gray'))
    # Ve cay
    for node in tree:
        if node.parent:
            ax.plot([node.x, node.parent.x], [node.y, node.parent.y], "-g", linewidth=0.5)
    # Ve duong di
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
    plt.show()



if __name__ == "__main__":
    print("Vẽ bản đồ (vật cản)...")
    obstacles = obstacles_EX.id_obstacles
    
    print("Chạy RRT...")
    tree, path = rrt((10, 10), (90, 90), obstacles)

    

    if path:
        print("Da tim thay duong di!")
        plot_result(tree, path, obstacles, "Thuat toan RRT")
    else:
        print("Khong tim thay duong di trong so lan lap cho phep.")


    plt.show()
