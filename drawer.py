# drawer.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_obstacles():
    obstacles = []
    rect_start = None
    finished = False

    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Vẽ vật cản (nhấn Enter để hoàn tất)")
    ax.grid(True)

    def on_click(event):
        nonlocal rect_start
        # Kiểm tra nhấn chuột trái và có tọa độ hợp lệ
        if event.button == 1 and event.xdata is not None:
            if rect_start is None:
                rect_start = (event.xdata, event.ydata)
            else:
                x0, y0 = rect_start
                x1, y1 = event.xdata, event.ydata
                ox, oy = min(x0, x1), min(y0, y1)
                w, h = abs(x1 - x0), abs(y1 - y0)
                obstacles.append((ox, oy, w, h))
                ax.add_patch(patches.Rectangle((ox, oy), w, h, color='gray'))
                rect_start = None
                fig.canvas.draw()

    def on_key(event):
        nonlocal finished
        if event.key == 'enter':
            finished = True

    cid_click = fig.canvas.mpl_connect('button_press_event', on_click)
    cid_key = fig.canvas.mpl_connect('key_press_event', on_key)

    # Vòng lặp đơn giản để chờ người dùng nhấn Enter (không đóng cửa sổ)
    while not finished:
        plt.pause(0.1)

    # Sau khi kết thúc, ngắt kết nối các event handler
    fig.canvas.mpl_disconnect(cid_click)
    fig.canvas.mpl_disconnect(cid_key)

    # Trả về danh sách vật cản cùng figure, ax để sử dụng tiếp
    return obstacles
