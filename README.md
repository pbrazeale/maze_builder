# 🧩 Maze Solver in Python

A graphical maze generator and visualizer built with Python and `tkinter`. This project was inspired by the [Boot.dev](https://www.boot.dev/courses/build-maze-solver-python) curriculum and serves as both an educational exercise and a demonstration of recursive backtracking in maze generation.

## 📸 Demo

![Maze Generation Animation](https://pbrazeale.github.io/images/maze_solver.gif)
![Completed Maze](https://pbrazeale.github.io/images/completed_maze.jpg)

## 🚀 Features

- Generates random mazes of configurable/random size using recursive backtracking
- Animates the drawing of the maze as it's being generated
- Built using a lightweight custom graphics library on top of `tkinter`
- Modular design with `Cell`, `Maze`, and `Window` abstractions

## 🛠️ Technologies Used

- Python 3.12
- `tkinter` for GUI rendering
- Object-Oriented Programming principles
- Recursive backtracking for maze generation

## 🧠 How It Works

- The screen is divided into a grid of `Cell` objects.
- Each cell starts with all four walls.
- The algorithm recursively visits unvisited neighbors, knocking down walls between the current and next cell.
- The entrance and exit are created by removing the top wall of the starting cell and the bottom wall of the ending cell.

## 🧪 Running the Project

### Prerequisites

- Python 3.12 installed on your system

### Run Instructions

- Fork the repo and run

```bash
python main.py
