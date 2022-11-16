# Exercise Sheet 5


## Exercise 5.1 (7 points)

In this exercise you will implement your own **template matcher** using ZNCC (Zero Normalized Cross Correlation).

For this purpose first implement the method shown below which should compute and return a correlation matrix for a given template and image. A correlation matrix is a 2D matrix that holds match scores which are obtained by comparing the given template with various image patches (regions in the image which have the same size as the template). Each match score's location in the correlation matrix simply corresponds to the location of an image patch . The scores should be calculated using the ZNCC formula which we discussed in class.



```python
def zncc(template, img):
	...
	return corr_matrix
```



Now use your method to identify at which pixel location *eye.png* appears in *lena.png*. To accomplish this you have to find the largest value in your matrix and then derive the corresponding location.

Finally, also answer the following questions:
- At which location does the eye patch occur?
- What are the theoretical minimum and maximum values of the ZNCC?
- Why do we prefer ZNCC over NCC (Normalized Cross Correlation) and Standard Cross Correlation for Template Matching?



**Note:**

- Implementing ZNCC *efficiently* is hard. Of course, a basic (probably slow) implementation is sufficient as it's only about understanding the concept.





## Exercise 5.2 (5 points)

In this exercise you will implement your own **median filter** for image denoising.  Therefore implement your own median filter function having the signature below. The function should receive a noise image and return a denoised version of the image.

```python
def median_filter(img):
 	...
	return denoised_img
```



To test your code load the lena image and add artificially **salt-and-pepper-noise**. You might want to take a look at the following [link](https://www.geeksforgeeks.org/add-a-salt-and-pepper-noise-to-an-image-with-python) to see how this can be achieved.

Finally, denoise the noisy image using (1) our own median filter and (2) skimages's [Gaussian filter](https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.gaussian). Observe how well the median filter performs on this task compared to the Gaussian filter.


.
