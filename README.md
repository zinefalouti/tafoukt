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

**Central Point Detection (Point Zero of the Agent)**
![image](https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae1.png)

**First Expansion Example with vectors (Vx,Vy)**
![image](https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/fig3.png)
