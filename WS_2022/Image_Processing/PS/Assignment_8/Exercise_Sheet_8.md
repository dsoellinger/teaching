# Exercise Sheet 8



## Exercise 8.1 (4 points)

In this exercise, we implement an additive (spread-spectrum) watermarking scheme, based on the 2D wavelet transform. The idea is
to run a 2D wavelet decomposition on a **grayscale image**, choose a subband and add a bipolar (-1,+1) watermark sequence `w` to the wavelet
coefficients `y` of this subband. This sequence is added with a certain *strength* `alpha` (i.e., a multiplicative factor), i.e., `y = x + alpha*w`.
This is called *additive spread-spectrum watermarking*. Finally, we will reconstruct the image from the wavelet coefficients.

In principle, the **steps** are as follows:
1. Wavelet-decompose the image
2. Choose a subband
3. Generate a random bipolar watermark sequence
4. Add the sequence to the wavelet coefficients of the subband
5. Reconstruct the image from the coefficients

A possible embedding function for the watermark could look like this:

```python
def embed_watermark(img, where, alpha, seed):
    # ...
    return watermarked_image, watermark_sequence
```

The function returns the watermarked image and the watermark sequence.

**Task:** Embed a watermark in an image of your choice and plot the result. Test different subbands and values for alpha. Are there visible degradations in quality?



## Exercise 8.2 (4 points)

In this exercise, we will implemented a simple (correlation-based) watermark detector to test the watermarking algorithm.

In principle, the **steps** are as follows:
1. Embed a watermark
```python
# e.g., embed the watermark into the "dd" subband of level 2
wm_img, wm = embed(img, (2, 'dd'), 0.1, 1234)
```
2. Detect the watermark by decomposing the image using the 2D wavelet transform, select the subband and correlate the coefficients `x` with the watermark sequence `w`, e.g.,
```python
def detect(img, where, w):
    # ...
    return score
```
You can compute the correlation as follows:  `1/N * (x[0]*w[0] + ... + w[N]*x[N])`where `N` denotes the number of coefficients in the subband.

**Task:**  Generate 1000 random watermarks and plot/compare the detection scores to the detection score you get with the actual embedded watermark (using the correct random number generator seed).



### Resources

Use the `PyWavelets` Python package, e.g., with Anaconda you can install it using

```bash
conda install pywavelets
```

