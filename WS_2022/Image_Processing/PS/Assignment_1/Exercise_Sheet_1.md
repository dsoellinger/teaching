# Exercise sheet 1



## Exercise 1.1 (5 points)

To goal of this exercise is to get familiar with different color models and how to load, show and manipulate images in Python.

- Choose an arbitrary RGB image, load the image (e.g. using PIL) and visualize the image using Matplotlib

- Convert the image to the HSV color space and modify (increase / decrease) it's channels. How does changing the different channels affect the resulting image?

- How do you convert the RGB image to a grayscale image?

- Suppose you want to change the brightness of the image of the RGB image. How would you do achieve this? How would you modify the brightness it if you were not allowed to use a function that is already implemented in a framework? How does changing the brightness affect on the luminance histogram?

- Get yourself familiar the terms hue, saturation, value and lightness. How would you describe those terms? Also consider adding pictures / additional resources if it helps to explain the terms.

  

## Exercise 1.2 (5 points)

You are given a binary map shown below. Implement an function `connected_components(mat, connectivity)` that identifies the connected components in the image for *4-connectivity* and *8-connectivity*. How does the output of your function compare to the output of `skimage.measure.label`?

```python
m = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def connected_components(mat, connectivity='4'):
    ...
```



## Exercise 1.3 (5 points)

A *Laplacian pyramid* is a hierarchical multi-scale representation of an image that saves the difference image between the a smooth and non-smooth versions of the image at different scales. Smoothing (Blurring) is achieved by means of a Gaussian filter. A more detailed explanation of how Laplacian pyramids are constructed can be found [here](http://sepwww.stanford.edu/data/media/public/sep/morgan/texturematch/paper_html/node3.html)

In this exercise you should implement a function (function signature below) that generates the N-level Laplacian pyramid for a given RGB image. For instance, you can use the `lena.png` image provided in the repository. Implement it yourself (don't use functions such as `skimage.transform.pyramid_gaussian`). What would be a good choice for sigma and the corresponding kernel size?  How many levels can our pyramid have?

```python
def compute_laplacian_pyramid(img, levels, sigma):
    ...
```

Once you have constructed the pyramid, implement another function that retrieves the pyramid and reassembles the original image. Is the resulting image the same as the original image?

```python
def reassemble_laplacian_pyramid(pyramid):
    ...
```

"Bonus" question for those who are already familiar with the concept of "frequency domain" ... What effect does a Gaussian filter applied in the spatial domain have in the frequency domain?
