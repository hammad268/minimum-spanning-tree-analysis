# 🌳 Minimum Spanning Tree (MST) Visualizer in Python

## 📌 Overview

This project is a Python-based implementation of **Minimum Spanning Tree (MST)** algorithms with interactive visualization. It demonstrates how two classic algorithms — **Kruskal’s Algorithm** and **Prim’s Algorithm** — work on both predefined and randomly generated graphs.

The program allows users to:

* Generate graphs
* Apply MST algorithms
* Visualize results using graphical output

---

## ⚙️ How It Works

### 1. Graph Creation

The project supports two types of graphs:

* **Sample Graph**

  * A predefined graph with nodes (A–F)
  * Useful for testing and understanding algorithm behavior

* **Random Graph**

  * User-defined number of nodes and edges
  * Ensures the graph is connected
  * Random weights are assigned to edges

---

### 2. Graph Representation

* The graph is stored as an **edge list** in the format:

  ```
  (weight, source, destination)
  ```
* Nodes are stored separately
* The graph is treated as **undirected**

---

### 3. Kruskal’s Algorithm

Kruskal’s algorithm builds the MST by selecting edges in increasing order of weight.

#### Steps:

1. Sort all edges by weight
2. Initialize a **Disjoint Set (Union-Find)** structure
3. Iterate through edges:

   * Add edge if it does NOT form a cycle
   * Use union-find to track connected components
4. Stop when MST contains (V - 1) edges

#### Key Feature:

* Efficient cycle detection using **Union-Find (Disjoint Set)**

---

### 4. Prim’s Algorithm

Prim’s algorithm builds the MST starting from a single node.

#### Steps:

1. Choose a starting vertex
2. Add all its edges to a **min-heap (priority queue)**
3. Repeatedly:

   * Select the smallest edge
   * Add the new vertex to MST
   * Push its adjacent edges into the heap
4. Continue until all vertices are included

#### Key Feature:

* Uses **heapq (priority queue)** for efficient edge selection

---

### 5. Visualization

The project uses:

* **NetworkX** → Graph structure
* **Matplotlib** → Graph drawing

#### Visual Features:

* Nodes displayed in a clean layout
* Edge weights shown clearly
* MST edges highlighted in **red**
* Normal edges shown in **gray**

#### Layout:

* Fixed layout for sample graph (A–F)
* Automatic layout for random graphs

---

### 6. User Interaction

The program runs in a **menu-driven interface**:

#### Main Menu:

* Use sample graph
* Generate random graph
* Exit

#### Algorithm Menu:

* Run Kruskal’s Algorithm
* Run Prim’s Algorithm
* Run both algorithms
* Return to main menu

---

### 7. Output

For each algorithm:

* Step-by-step edge selection is printed
* Total MST weight is displayed
* Graph visualization is shown
* Option to save the graph as a PNG file

---

## 🧠 Concepts Used

* Graph Theory
* Minimum Spanning Tree (MST)
* Greedy Algorithms
* Disjoint Set (Union-Find)
* Priority Queue (Heap)
* Data Visualization

---

## 📦 Requirements

Make sure you have the following installed:

```
pip install matplotlib networkx
```

---

## ▶️ How to Run

```
python your_file_name.py
```

Follow the on-screen menu to interact with the program.

---

## 🎯 Learning Purpose

This project is ideal for:

* Understanding MST algorithms visually
* Comparing Kruskal vs Prim
* Practicing graph data structures in Python

---

## 📸 Features Summary

* ✅ MST using Kruskal’s Algorithm
* ✅ MST using Prim’s Algorithm
* ✅ Graph visualization
* ✅ Random graph generation
* ✅ Step-by-step output
* ✅ Save graph as image

---

## 👨‍💻 Author

Developed as a learning project for Data Structures and Algorithms.

---


