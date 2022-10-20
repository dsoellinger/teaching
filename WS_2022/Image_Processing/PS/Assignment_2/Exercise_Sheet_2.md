## Important notice
- Please mention the names of all group members in the submitted notebook. 


## Exercise 2.1 (3 points)

You are given the binary map shown below. Create a [Freeman Chain Code](https://ojskrede.github.io/inf4300/notes/week_04/) that describes the object's inner border.

````
      |   0   |  1  |   2  |   3  |   4   |  -- x
--------------------------------------------
  0   |   0      0      1      0      0    
  1   |   0      1      1      1      0   
  2   |   0      1      1      0      0    
  3   |   0      1      0      0      0    
  4   |   0      0      0      0      0    
  |
  y
````

**Task 1:** Create the corresponding chain code assuming 8-connectivity. <x,y>=<1,3> as the start position. Traverse in clockwise direction.

**Task 2:** Encode the obtained chain code to be invariant to the start position.

**Remark:** 

- Not only provide the final chain code, but also explain **how** you obtained the code (show the intermediate steps)
- No coding required. 



## Exercise 2.2 (3 points)

The goal of this exercise is to get familiar with the **(cross)-correlation operation** $\otimes$ applied to 2D matrices.

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



**Correlation:**

$$\hat{I}[x,y] = I \otimes F = \sum_{m=0}^{M-1}\sum_{n=0}^{N-1} F[m,n] \cdot I[x+m, y+n]$$



- **Task 1:** Correlate the kernel *F* with the matrix *I*. How does the resulting matrix look like?

- Input padding is a way to control the size of the output matrix. To pad the input matrix *I*, you simply add values around the input matrix. The exact choice of these values is highly application dependent. However, the simplest form of padding is obviously to pad the input matrix with a constant value *c*.

  **Task 2:** Pad the image *I* with the constant *c=1*. Correlate the padded image with the kernel *F*. How does the resulting matrix look like? What is the size of the resulting matrix?

**Remark:**

- No coding is required.



# Exercise 2.3 (5 points)

As we now understand how to correlate two matrices, we can apply this knowledge to a real image. In this exercise you will blur (a.k.a. smooth) a grayscale image by means of the correlation operation. The goal is to understand how the parameters (weight, size) of the kernel influence the "blur".

You are free to choose the grayscale image, but provide the image when you submit the assignment so I can run your code.

- **Task 1:** Implement a function `mean_filter_kernel` that returns a kernel which returns the mean value of an images' local neighborhood, if you correlate the image with the kernel.

  ````python
  def mean_filer_kernel(kernel_size):
       ....
       return  # Return an numpy.ndarray
  ````
  
- **Task 2:** As can be seen in the [documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.correlate2d.html) of `scipy.signal.correlate2d`, the function provides a parameter called *mode*. Why is this parameter important? How does changing the parameter influence the output of the function?

- **Task 3:** Use `mean_filter_kernel` to generate kernels of size $3\times3$, $5\times5$, $7\times7$, $9\times9$. Correlate each kernel with the image using `scipy.signal.correlate2d`. Visualize the different versions of the blurred image.

- You now have to replace the mean filter with a Gaussian filter. To accomplish this, we first have to construct a 2D Gaussian kernel. Unfortunately, this is not easy to achieve as there is no existing function that returns a 2D Gaussian kernel. For this reason I provide a function that creates a `gaussian_filter_kernel(std)` for a given sigma.

  ````python
  def gaussian_filter_kernel(std):
  	kernel_size = int(2*np.ceil(3*std)+1)
      kernel_1d = signal.gaussian(kernel_size, std=std).reshape(kernel_size, 1)
      kernel_2d = np.outer(kernel_1d, kernel_1d)
      kernel_2d = kernel_2d / gkern2d.sum()
      return kernel_2d
  ````

- **Task 4:**  Get yourself familiar with 3D plotting in Matplotlib ([see](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)) as this a handy tool that often used in practice. Plot the some Gaussian kernels with different sigmas as 3D surface.

- **Task 5:** Correlate the Gaussian kernel with the original image and play around with different values for sigma. Which version (Mean vs. Gaussian) visually provides better results and why?



