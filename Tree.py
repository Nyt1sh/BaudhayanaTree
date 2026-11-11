import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
 
BG = "#000000"
CMAP = LinearSegmentedColormap.from_list(
    "neon_pink", ["#C2007A", "#FF1493", "#FF2EC4", "#FF6EF0", "#FFC2F7"]
)
 
 
def rot(v, a):
    c, s = np.cos(a), np.sin(a)
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])
 
 
def build_tree(depth, angle):
   
    squares, gens = [], []
    level = [(np.array([-0.5, 0.0]), np.array([0.5, 0.0]))]
    for g in range(depth):
        nxt = []
        for a, b in level:
            n = rot(b - a, np.pi / 2)
            d, c = a + n, b + n
            squares.append(np.array([a, b, c, d]))
            gens.append(g)
            e = d + np.cos(angle) * rot(c - d, angle)   # triangle apex
            nxt.append((d, e))                          # left branch
            nxt.append((e, c))                          # right branch
        level = nxt
    return squares, np.array(gens)
 
 
# ---------------------------------------------------------------- figure
fig = plt.figure(figsize=(11, 8.5), facecolor=BG)
try:
    fig.canvas.manager.set_window_title("Pythagoras Tree - live")
except Exception:
    pass
ax = fig.add_axes([0.02, 0.17, 0.96, 0.81], facecolor=BG)
ax.set_aspect("equal")
ax.axis("off")
 
# glow layers (wide faint strokes) + crisp layer on top
glow_specs = [(7, 0.04), (4.5, 0.07), (2.5, 0.14)]
glows = [PolyCollection([], facecolors="none", linewidths=lw, alpha=al)
         for lw, al in glow_specs]
main = PolyCollection([], linewidths=0.9)
for coll in glows + [main]:
    ax.add_collection(coll)
 
state = dict(polys=[], edge=None, fill=None, shown=0.0, paused=False)
 
 
def rebuild(_=None):
    depth = int(s_depth.val)
    angle = np.radians(s_angle.val)
    polys, gens = build_tree(depth, angle)
    t = gens / max(depth - 1, 1)
    edge = CMAP(t)
    fill = edge.copy()
    fill[:, 3] = 0.12
    state.update(polys=polys, edge=edge, fill=fill, shown=0.0)
 
    allp = np.vstack(polys)
    pad = 0.15
    ax.set_xlim(allp[:, 0].min() - pad, allp[:, 0].max() + pad)
    ax.set_ylim(allp[:, 1].min() - pad, allp[:, 1].max() + pad)
    for coll in glows + [main]:
        coll.set_verts([])
 
 
def update(_frame):
    if state["paused"] or not state["polys"]:
        return []
    total = len(state["polys"])
    state["shown"] = min(total, state["shown"] + s_speed.val)
    n = int(state["shown"])
    verts = state["polys"][:n]
    edge = state["edge"][:n]
    for coll in glows:
        coll.set_verts(verts)
        coll.set_edgecolor(edge)
    main.set_verts(verts)
    main.set_edgecolor(edge)
    main.set_facecolor(state["fill"][:n])
    return []
 
 
# ---------------------------------------------------------------- controls
txt = "#FF6EF0"
def make_slider(rect, label, lo, hi, init, step=None):
    a = fig.add_axes(rect, facecolor="#1a0014")
    s = Slider(a, label, lo, hi, valinit=init, valstep=step, color="#FF2EC4")
    s.label.set_color(txt)
    s.valtext.set_color(txt)
    return s
 
s_speed = make_slider([0.12, 0.11, 0.55, 0.025], "Speed", 0.5, 150, 6)
s_angle = make_slider([0.12, 0.07, 0.55, 0.025], "Angle", 15, 75, 40)
s_depth = make_slider([0.12, 0.03, 0.55, 0.025], "Depth", 3, 14, 12, step=1)
 
ax_pause = fig.add_axes([0.76, 0.085, 0.10, 0.045])
ax_reset = fig.add_axes([0.87, 0.085, 0.10, 0.045])
b_pause = Button(ax_pause, "Pause", color="#1a0014", hovercolor="#4a0036")
b_reset = Button(ax_reset, "Restart", color="#1a0014", hovercolor="#4a0036")
for b in (b_pause, b_reset):
    b.label.set_color(txt)
 
 
def toggle_pause(_):
    state["paused"] = not state["paused"]
    b_pause.label.set_text("Play" if state["paused"] else "Pause")
    fig.canvas.draw_idle()
 
 
b_pause.on_clicked(toggle_pause)
b_reset.on_clicked(rebuild)
s_angle.on_changed(rebuild)   # changing angle/depth regrows the tree
s_depth.on_changed(rebuild)
 
rebuild()
anim = FuncAnimation(fig, update, interval=25, blit=False, cache_frame_data=False)
plt.show()
 