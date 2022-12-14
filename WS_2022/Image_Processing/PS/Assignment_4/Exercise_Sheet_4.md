# Exercise Sheet 4

#### Submission: 
The following exercise can be submitted as PDF file. No Jupyter Notebook file is required.

## Exercise 4.1 (6 points)



The goal of this exercise is to get familiar with **padding** and the **convolution operation** $\star$ applied to 2D matrices.

All calculation needed should be done by hand. If not otherwise stated, no input padding is required.

You are given the matrix $I$ and the kernel $F$ shown below.



$$I = \begin{bmatrix}
4 & 1 & 4 & 2 \\
0 & 1 & 3 & 2 \\
1 & 3 & 1 & 1 \\
3 & 4 & 2 & 0 \\
\end{bmatrix} $$

$$F = \begin{bmatrix}
1 & 0 & 1 \\
2 & 1 & 0 \\
1 & 0 & 1 \\
\end{bmatrix} $$



- **Task 1:** Convolve the the matrix $I$ with the kernel $F$.  How does the resulting matrix look like?

- **Task 2:** Zero-Pad the matrix $I$ using a padding factor of 2 and convolve $I$ with $F$ using a **stride of 2**.

- **Task 3:** Flip/mirror the kernel $F$ and correlate $I$ with $F$. Verify that you again get the same output as in Task 1.

- **Task 4:** Flip/mirror the matrix $I$ and correlate $I$ with $F$ . Do we still get the same result?

- **Task 5:** Apply circular padding to the kernel $F$ using a padding "factor" of 2. How does the padded matrix look like?

- **Task 6:** Apply either symmetric or reflective padding to the kernel $F$ using a padding "factor" of 2. How does the padded matrix look like?

  
