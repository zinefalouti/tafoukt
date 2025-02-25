[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14791340.svg)](https://doi.org/10.5281/zenodo.14791340)
---
# Introduction
This repository contains three distinct yet complementary algorithms designed to explore and optimize data in large matrices. Each method provides unique strategies for handling search and analysis, catering to different use cases in both exploratory and precision-driven tasks.

### R.E.B.S (Rhythmic Expansion Batch Search)
R.E.B.S is a radial expansion search algorithm that explores a dataset/matrix using two vectors Vx and Vy while isolating the crust during (n) from the explored submatrix during (n-1).

### G.E.B.S (Gradient Expansion Batch Search)
G.E.B.S slices the larger matrix globally using both movement vectors Vx and Vy then isolates two areas, "Core" which is thoroughly searched, and the "Gradient" which is gradually searched using min and max precision parameters.

### L.E.B.S (Learning Exploration Batch Search)
L.E.B.S slices the larger matrix globally using the width of sector Sx and the height of sector Sy, and searches each using two different methods, "Brutal," and "Prudent." The "Prudent" method uses submatrices M(0), M(n/2), and M(n) to study the 3 patterns found in these 3 submatrices and layers them together to produce a global one using "Poisson," the global pattern then is used a mask of search while looping to find objectives within each sector. 

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
- (260,260): (VectorX,VectorY) of how the split between "Core" and "Gradient" Areas will happen, including the global slice. The Core area is formed with a spiral alongside the center of the larger matrix from the central submatrix, while the gradient begins at  its most intense point and falls off at both edges of the larger matrix extremities.
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
- (630,630): (Total Columns, Total Rows) of each sector/submatrix. This defines how you want to slice the larger matrix (data)
- False: A boolean that switches between "Brutal" and "Prudent" modes, where True activates the "Brutal" mode and "False" the "Prudent" one.

> **L.E.B.S Brutal and Prudent Modes** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/Figure9.png" width="630"> <br><br>

> **Learning Method from subM(0), subM(n/2), and subM(n)** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae8.png" width="600"> <br><br>

> **Poisson for Layering the Recorded Patterns from the learning submatrices** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/formulae9.png" width="500"> <br><br>

---

# Why "Tafoukt"?
Tafoukt (ⵜⴰⴼⵓⴽⵜ) means "the Sun" in Tamazight (North African Native). It also symbolizes guidance through obstacles, but in the case of R.E.B.S, G.E.B.S, and L.E.B.S it is a mere base inspiration of the shape drawn by these 3 algorithms in a geometrical sense while batch searching a large matrix. Starting from the center in the radial core precise search, then emitting rays throughout the core diameter either using a gradient approach (G.E.B.S), or a learning approach (L.E.B.S).

> **Geometric Representation of R.E.B.S, G.E.B.S, and L.E.B.S** <br>
<img src="https://raw.githubusercontent.com/zinefalouti/griidtech-hosting/refs/heads/main/Research4-images/Global-Figure.png">

---

# Conclusion
May these algorithms serve as a helpful tool in your journey through data exploration, batch searching, and optimization. Whether they spark new ideas or simply offer a fresh perspective. I hope that this small contribution adds to the ever-growing body of knowledge. Thank you for visiting. Enjoy!

---

# Resources and Literature

> Tardos, E., & Kleinberg, J. (2005). Algorithm Design. Pearson.

> Gale, D., & Shapley, L. S. (1962). College admissions and the stability of marriage. The American Mathematical Monthly, 69(1), 9-15.

> Koutsoupias, E. (2021). The Price of Anarchy in the Control of Complex Systems. Springer.

> Beckon, N., et al. (2007). On the Statistical Properties of Random Variables. Journal of Applied Mathematics, 34(2), 58-72.

> Schesser, J. (n.d.). Sinusoidal Signals. New Jersey Institute of Technology.

> Python. (n.d.). Python Programming Language.

> Numpy. (n.d.). NumPy Documentation.

> D'Agostini, G. (1995). Likelihood Analysis of Systematic Uncertainties. Nuclear Instruments and Methods in Physics Research, 346(2), 1-19.

> Nakazato, H. (n.d.). Fundamentals of Digital Signal Processing. Waseda University.

> Daley, D. J., & Vere-Jones, D. (2003). An Introduction to the Theory of Point Processes. Springer.

> Müller, A., & Wessel, S. (2006). Algorithmic Foundations of Data Structures. Springer.

> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.

> Kingman, J. F. C. (1993). Poisson Processes. Oxford University Press.

> Billingsley, P. (1999). Convergence of Probability Measures (2nd ed.). Wiley-Interscience.

> Eppstein, D. (2015). Approximation Algorithms for NP-Hard Problems. Journal of Algorithms, 55(2), 126-145.
Kullback, S., & Leibler, R. A. (1951). On information and sufficiency. Annals of Mathematical Statistics, 22(1), 79-86.

> Gelman, A., Carlin, J. B., Stern, H., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). Bayesian Data Analysis (3rd ed.). CRC Press.

> Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning (2nd ed.). Springer.

> Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.

> Kullback, S. (1959). Information Theory and Statistics. Dover Publications.

> Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley-Interscience.



