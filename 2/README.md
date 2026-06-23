# Assignment CA2: Genetic Algorithm & Minimax Game AI

## 📌 Overview
This assignment consists of two independent projects exploring different areas of artificial intelligence:

### Part 1: Genetic Algorithm - Image Reconstruction with Triangles
An evolutionary approach to create art by reconstructing target images using semi-transparent triangles. The algorithm evolves a population of chromosome (individuals), each representing an image composed of colored triangles, to minimize the visual difference from a target image. This demonstrates how genetic algorithms can solve complex optimization problems with large state spaces.

### Part 2: Minimax Algorithm - Connect 4 Game AI
An implementation of the Minimax algorithm with Alpha-Beta pruning for playing the classic Connect 4 game. The AI uses a heuristic evaluation function to assess board positions and make optimal moves, simulating different game depths to decide the best strategy. This showcases adversarial search techniques in game-playing AI.

## 🎯 Learning Objectives
- Implement **Genetic Algorithms** for image reconstruction problems
- Understand **chromosome representation** and **fitness functions**
- Apply **crossover**, **mutation**, and **selection** strategies in evolutionary computation
- Implement **Minimax algorithm** with **Alpha-Beta pruning**
- Design **heuristic evaluation functions** for game-playing AI
- Analyze algorithm performance with different parameters (population size, depth, pruning)

---

# Part 1: Genetic Algorithm - Art Generation

## 🧠 Key Concepts & Algorithms

### Chromosome Representation
- Each chromosome represents an image composed of **triangles**
- **Gene**: A colored triangle defined by:
  - Three vertices (x, y coordinates)
  - RGBA color (Red, Green, Blue, Alpha/transparency)
- **Chromosome**: Collection of triangles forming the complete image

### Genetic Operators
1. **Crossover Methods**:
   - **Blend Crossover** (`crossover`): Creates child by blending pixel values from both parents
   - **Point Crossover** (`crossover_2`): Splits image horizontally/vertically and combines halves from different parents
   - **Pixel-wise Crossover** (`crossover_3`): Randomly selects each pixel from either parent

2. **Mutation** (`mutate`): Adds random triangles or modifies pixel values
3. **Selection**: Tournament selection with configurable tournament size

### Fitness Function
- **CIE 1976 Delta-E** color difference metric (`get_fitness`)
- **Euclidean distance** as alternative measurement (`get_fitness_euclidean`)
- Lower fitness values indicate better similarity to target image

### Parameters Explored
- Population size (tested with different values)
- Number of generations (5000 in main run)
- Triangle count per chromosome (randomized)
- Image size (resized for faster computation)

## 📊 Dataset
- Three sample target images provided (e.g., eagle.png)
- Students can test with any image of their choice
- Images are resized (to 100x66 in main run) for faster processing

## ⚙️ Implementation Details

### Tech Stack
- **Language**: Python 3.11
- **Libraries**:
  - `PIL/Pillow` - Image manipulation
  - `NumPy` - Array operations
  - `matplotlib` - Visualization
  - `colour` - Color difference calculations
  - `pandas` - Data logging
- **Environment**: Jupyter Notebook

## 📈 Results & Analysis
- Fitness values progressively decrease (improve) over generations
- Visual comparison between reconstructed and target images
- Performance comparison with different crossover methods
- Impact of population size on convergence speed

---

# Part 2: Minimax Algorithm - Connect 4

## 🧠 Key Concepts & Algorithms

### Minimax Algorithm
- Implements adversarial search for two-player games
- **Maximizing player** (CPU/Yellow): Tries to maximize score
- **Minimizing player** (Human/Red): Tries to minimize score
- **Depth-limited search** with configurable depth (1-6)

### Alpha-Beta Pruning
- Optimizes Minimax by pruning unnecessary branches
- Reduces node visits significantly
- Configurable via `prune` parameter
- Performance comparison with/without pruning

### Heuristic Evaluation
Features evaluated:
- **Four-in-a-row detection** (winning condition)
- **Center control** (preference for middle columns)
- **Window scoring**: Evaluates sliding windows of 4 cells
- Scores based on:
  - Having 3 pieces + 1 empty space (+5)
  - Having 2 pieces + 2 empty spaces (+2)
  - Opponent's threats (-4)
  - Winning configuration (+100)

### Game Flow
1. Random player starts the game
2. Human (player) uses Minimax for move selection
3. CPU uses Best Score + randomness (30%)
4. Game continues until win/draw

## ⚙️ Implementation Details

### Tech Stack
- **Language**: Python 3.11
- **Libraries**:
  - `NumPy` - Board representation
  - `Pygame` - Graphical user interface (optional)
  - `time` - Performance measurement
- **Environment**: Jupyter Notebook / Python Script

### Performance Testing
The code includes comprehensive testing:
- **100 iterations** per configuration
- Variables tested: Depth (1-6), Pruning (enabled/disabled)
- Metrics recorded:
  - User win rate
  - CPU win rate
  - Tie rate
  - Average time per game
  - Nodes visited (implicit)

## 📈 Results & Observations
- **Depth 1**: Fast, but weak gameplay
- **Depth 2-3**: Good balance of speed and performance
- **Depth 4-6**: Stronger AI but significantly slower
- **Pruning effect**: Up to 8x speedup at depth 5
- **Win rates**: CPU wins increase with depth
