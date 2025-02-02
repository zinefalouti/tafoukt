# Introduction
This repository contains three distinct yet complementary algorithms designed to explore and optimize data in large matrices. Each method provides unique strategies for handling search and analysis, catering to different use cases in both exploratory and precision-driven tasks.

### R.E.B.S (Random Exploration Batch Search)
R.E.B.S is a stochastic approach that combines random search techniques with batch processing to identify key patterns within large datasets. By leveraging randomness, it is effective in situations where a broad, less structured search is required.

### G.E.B.S (Gradient Expansion Batch Search)
G.E.B.S focuses on expanding search regions dynamically, guided by gradients, to refine search precision. It is designed for use cases where the search space is large but structured in a way that allows for targeted, gradient-based exploration.

### L.E.B.S (Learning Exploration Batch Search)
L.E.B.S combines learning-based exploration with batch search methods. It adapts over time, fine-tuning its search patterns based on previous findings, which makes it particularly useful for iterative optimization tasks in evolving datasets.

*These methods can be employed independently or in combination to suit a variety of problem domains, ranging from exploratory analysis to precise optimization.*


---

# Code
### Dependencies:
While R.E.B.S doesn't require any dependencies, G.E.B.S and L.E.B.S require only one:
```
pip install numpy
```
---
### Using R.E.B.S
Assuming R.E.B.S exists at the same level as your program, please use the following:
```
import rebs
```
And call the function:
```
rebs.allin(data,objectives,(360,360),1,1,False)
```

Where:
- data: The grid or matrix containing the target data
- objectives: A list [] of multiple objectives
- (360,360): (VectorX,VectorY) of how the larger data will be sliced and the movement of the expansion, where Y moves row by row and X moves column by column
- 1: Precision through X (Columns) a value clamped between 0.1 and 1, where 1 is full precision search.
- 1: Precision through Y (Rows) a value clamped between 0.1 and 1, where 1 is full precision search.
- False: A boolean to activate or deactivate the debug mode

> **Central Point Detection (Point Zero of the Agent)** <br><br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae1.png" width="500"> <br>

> **First Expansion Example with vectors (Vx,Vy)** <br><br>
![image](https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/fig3.png) <br>

---
### Using G.E.B.S
Assuming G.E.B.S exists at the same level as your program, please use the following:
```
import gebs
```
And call the function
```
gebs.oversee(data,objectives,(260,260),(0.3,0.7))
```
Where:
- data: The grid or matrix containing the target data
- objectives: A list [] of multiple objectives
- (260,260): (VectorX,VectorY) of how the split between "Core" and "Gradient" Areas will happen, including the global slice. The Core area is formed with a spiral alongside the center of the larger matrix and from the central submatrix the gradient begins and at its most intense point and falls off at both edges of the larger matrix extremities.
- (0.3,0.7): 0.3 represents the min pruning during the gradient, and 0.7 represents the max pruning during the gradient.

> **Drawing the Core Area in G.E.B.S (Vx,Vy)** <br><br>
![image](https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/fig6.png) <br><br>

> **The Split of The Two Groups of Submatrices to "Core" and "Gradient" Areas** <br><br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae5.png" width="630"> <br><br>

> **Sinusoidal Function for the Gradient Zone** <br><br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae6.png" width="500"> <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/Figure8.png" width="500"> <br>

---

## Using L.E.B.S
Assuming L.E.B.S exists at the same level as your program, please use the following:
```
import lebs
```
And call the function
```
lebs.learner(data,objectives,(630,630),False)
```
Where:
- data: The grid or matrix containing the target data
- objectives: A list [] of multiple objectives
- (630,630): (Total Columns, Total Rows) of the each sector/submatrix. This defines how you want to slice the larger matrix (data)
- False: A boolean that switches between "Brutal" and "Prudent" modes, where True activates the "Brutal" mode and "False" the "Prudent" one.

> **L.E.B.S Brutal and Prudent Modes** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/Figure9.png" width="630"> <br><br>

> **Learning Method from subM(0), subM(n/2), and subM(n)** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae8.png" width="600"> <br><br>

> **Poisson for Layering the Recorded Patterns from the learning submatrices** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae9.png" width="500"> <br><br>

---

# Why "Tafoukt"?
Tafoukt (ⵜⴰⴼⵓⴽⵜ) means "the Sun" in Tamazight (North African Native). It also symbolizes guidance through obstacles, but in the case of R.E.B.S, G.E.B.S, and L.E.B.S it is a mere base inspiration of the shape drawn by these 3 algorithm in a geometrical sense while batch searching a large matrix. Starting from the center in radial core precise search, then emitting rays throughout the core diameter either using a gradient approach (G.E.B.S), or a learning approach (L.E.B.S).

> **Geometric Representation of R.E.B.S, G.E.B.S, and L.E.B.S** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/Global-Figure.png">




