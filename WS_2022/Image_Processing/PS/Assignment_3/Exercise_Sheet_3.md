# Exercise Sheet 3



## Exercise 3.1 (5 points)

Take a look at the three versions of the waterfall image (`waterfall1.jpg`, `waterfall2.jpg` and `waterfall3.jpg`).

One image was enhanced using global-histogram-equalization, one using CLAHE and one has not been enhanced.

- Which of the images is the (1) global-histogram-equalized, (2) CLAHE-equalized and (3) non-equalized version? Justify your answer. Also consider adding some plots of the image statistics to better justify your answer.

- Apparently the global histogram equalized version has not been "sufficiently enhancement". Explain why global histogram equalization performs poorly on the image and how CLAHE circumvents the problem.



## Exercise 3.2 (5 points)

Write a function that receives a source image (grayscale) as input and performs global-histogram-equalization. The function should return a global-histogram-equalized image.

```python
def histogram_equalize(img):
    #...
    return out
```

Test your function on `lena.png` or another image of your choice (don't forget to include the image in the final submission). 

Proof that your method works by ...

- Plotting the image before and after global-histogram-equalization
- Comparing the *PDF* and *CDF* of both images

**Hint:**

- It's ok to use functions such as `skimage.exposure.cumulative_distribution`, `np.histogram` or `np.cumsum` (no need to implement those yourself)
- `np.interp` allows you to interpolate



## Exercise 3.3 (5 points)

Write a function that receives two images, a source image and a target image (both grayscale) and then matches the source image's histogram to the target image's histogram.

```python
def histogram_match(source, target):
    #...
    return matched
```

Visualize the *CDF* of the (1) source, the (2) target and (3) the histogram-equalized source image. Use `lena.jpg` as source image and `stairs.jpg` as the target image.

