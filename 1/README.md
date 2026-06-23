# Assignment CA1: Lights Out Puzzle - Search Algorithms

## 📌 Overview
This assignment implements various search algorithms to solve the **Lights Out puzzle** - a classic problem where the goal is to turn off all lights in an n×n grid by toggling switches. Toggling a switch at position (x,y) flips the state of that light and its four adjacent neighbors (up, down, left, right). The challenge is to find the optimal sequence of moves with the fewest switches pressed.

## 🎯 Learning Objectives
- Implement **uninformed search algorithms** (BFS, IDS) and **informed search** (A*, Weighted A*)
- Model real-world problems as **state-space search** problems
- Design and evaluate **heuristic functions** for informed search
- Compare algorithm performance across different problem sizes
- Understand **admissible** and **consistent** heuristics
- Implement **weighted A*** with different alpha values

## 🧠 Key Concepts & Algorithms

### Problem Modeling
- **State**: n×n binary matrix (1 = light ON, 0 = light OFF)
- **Actions**: Toggling any cell (x,y) in the grid
- **Transition Model**: Toggling (x,y) flips (x,y) and its four neighbors (up, down, left, right)
- **Goal State**: All lights are OFF (matrix all zeros)
- **Initial State**: Randomly generated board

### Algorithms Implemented

#### Uninformed Search
1. **BFS (Breadth-First Search)**:
   - Guarantees optimal solution (shortest path)
   - Explores all states level by level
   - Memory-intensive for larger boards

2. **IDS (Iterative Deepening Search)**:
   - Combines benefits of DFS and BFS
   - Depth-limited DFS with increasing depth limits
   - Finds optimal solution with less memory than BFS

#### Informed Search
3. **A* Search**:
   - Uses heuristic to guide search
   - Optimal when heuristic is admissible and consistent
   - Evaluates nodes by f(n) = g(n) + h(n)

4. **Weighted A***:
   - Accelerates search by multiplying heuristic
   - f(n) = g(n) + α × h(n)
   - Faster but may sacrifice optimality

### Heuristic Functions
| Heuristic | Description | Admissible? | Consistent? |
|-----------|-------------|-------------|-------------|
| **Heuristic 1** | Number of lit lights (sum of board) | Yes (underestimates) | Yes (changes by at most 1) |
| **Heuristic 2** | Manhattan distance from each lit light to nearest solution | Yes | Yes (well-designed) |

## 📊 Dataset
- **Test Cases**: 6 random boards (3×3 and 4×4)
- **Board Generation**: Random toggling with varying seeds
- **Time Limits**:
  - BFS/IDS: 1s (3×3), 5s (4×4)
  - A*/Weighted A*: 1s (3×3), 1s (4×4), 2min (5×5)
- **Note**: 5×5 boards tested but results not shown in main run

## ⚙️ Implementation Details

### Tech Stack
- **Language**: Python 3.11
- **Libraries**:
  - `NumPy` - Board manipulation
  - `heapq` - Priority queue for A*
  - `collections.deque` - Queue for BFS
  - `threading/signal` - Timeout handling
  - `tabulate` - Results formatting
- **Environment**: Jupyter Notebook / Google Colab


## 📈 Results & Analysis

### Performance Comparison (3×3 Boards)

| Test Case | Algorithm | Solution | Nodes Visited | Time (s) |
|-----------|-----------|----------|---------------|----------|
| Test 1 | BFS | [(0,2), (1,0)] | 26 | 0.007 |
| | IDS | [(0,2), (1,0)] | 5 | 0.000 |
| | A* (h1) | [(1,0), (0,2)] | 4 | 0.000 |
| | A* (h2) | [(1,0), (0,2)] | 11 | 0.000 |
| | Weighted A* (h1, α=5) | [(1,0), (0,2)] | 6 | 0.000 |

### Performance Comparison (4×4 Boards)

| Test Case | Algorithm | Solution | Nodes Visited | Time (s) |
|-----------|-----------|----------|---------------|----------|
| Test 4 | BFS | [(0,2), (0,3), (1,0), (1,1)] | 1457 | 0.932 |
| | IDS | [(0,2), (0,3), (1,0), (1,1)] | 472 | 0.199 |
| | A* (h1) | [(1,0), (1,1), (0,2), (0,3)] | 17 | 0.000 |
| | Weighted A* (h1, α=5) | [(1,0), (1,1), (0,2), (0,3)] | 5 | 0.000 |

### Key Observations
1. **A* (heuristic1) consistently visits fewest nodes** due to strong guidance
2. **IDS uses significantly less memory than BFS** while maintaining optimality
3. **Weighted A* with α=5** is fastest but may sacrifice optimality (sometimes finding non-optimal solutions)
4. **Heuristic1 (number of lit lights)** performs better than heuristic2 (Manhattan distance)
5. **Heuristic2's Manhattan distance calculation** is more expensive and less effective

