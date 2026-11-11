# 🌸 Neon Baudhayana Tree

An interactive mathematical fractal visualization built with **Python,
NumPy, and Matplotlib**.

Generate an animated Pythagoras Tree with a neon-pink gradient, glowing
geometric outlines, and interactive controls for branching angle, depth,
and animation speed.

## ✨ Features

-   **Fractal generation** --- builds a tree-like geometric pattern from
    recursively generated squares.
-   **Neon-pink gradient** --- transitions from deep pink to light pink.
-   **Glow effect** --- layered polygon outlines create a neon
    appearance.
-   **Live animation** --- watch the tree grow on screen.
-   **Interactive controls** --- adjust speed, branching angle, and
    depth.
-   **Pause and resume** --- control the animation at any time.
-   **Restart** --- regenerate the tree after changing its parameters.

## 🧮 Mathematical idea

A Baudhayana Tree is a fractal made from squares. Starting with one
square, two smaller squares are constructed along its upper edge.
Repeating this process creates a branching, tree-like pattern.

This project uses 2D vector rotation and trigonometry to calculate the
geometry of each generation. Changing the branching angle changes the
overall shape of the tree.

## 🛠️ Built with

-   **Python** --- core programming language
-   **NumPy** --- vector and mathematical operations
-   **Matplotlib** --- plotting and visualization
-   **Matplotlib PolyCollection** --- polygon rendering
-   **Matplotlib FuncAnimation** --- animation
-   **Matplotlib Widgets** --- sliders and buttons

## 📋 Requirements

-   Python 3.9 or newer
-   NumPy
-   Matplotlib

## 🚀 Getting started

### 1. Clone the repository


``` bash
git clone https://github.com/Nyt1sh/BaudhayanaTree.git
```

### 2. Open the project folder

``` bash
cd BaudhayanaTree
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```


``` bash
pip install numpy matplotlib
```

### 4. Run the project


``` bash
python Tree.py
```

A Matplotlib window will open with the animated Pythagoras Tree.

## 🎮 Controls

  Control          What it does
  ---------------- ----------------------------------------------
  Speed slider     Changes how quickly the tree grows
  Angle slider     Changes the branching angle (15°--75°)
  Depth slider     Changes the number of generations (3--14)
  Pause button     Pauses or resumes the animation
  Restart button   Rebuilds the tree using the current settings

Try different angle and depth combinations to explore different
patterns.

## 📁 Project structure

``` text
neon-pythagoras-tree/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── preview.png
```

The `assets/preview.png` file is optional. Add a screenshot of the
running project there and keep the image reference below if you include
it.


## 🔍 How it works

1.  Begin with an initial horizontal line segment.
2.  Rotate its direction vector to construct a square.
3.  Use trigonometric calculations to find the branching point.
4.  Create two new line segments for the next generation.
5.  Repeat until the selected depth is reached.
6.  Render the squares with gradient-colored edges and translucent
    fills.
7.  Reveal the polygons progressively using Matplotlib animation.

## 🤝 Contributing

Suggestions, bug reports, and improvements are welcome.

1.  Fork the repository.
2.  Create a branch for your change.
3.  Make and test your changes.
4.  Open a pull request describing what you changed.


------------------------------------------------------------------------

**Built with Python, mathematics, and creativity.** 🌸

If you enjoy the project, consider giving the repository a ⭐ on GitHub!
