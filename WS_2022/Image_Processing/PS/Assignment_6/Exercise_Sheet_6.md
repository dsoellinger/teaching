# Exercise Sheet 6



## Exercise 6.1 (8 points)

In this exercise, will will improve our understanding of the Fourier transform, or more precisely, the **Discrete Fourier Transform (DFT)**.



**Discrete Fourier Transform (DFT):**

The Fourier coefficient(s) $\hat{f}(u)$ of a discrete 1-D signal $f(x)$ of length $N$ can be computed as follows:

$\hat{f}(u) = \frac{1}{N}\sum_{x=0}^{N-1} f(x) e^{-i2 \pi \frac{ux}{N}}$ 

where $u= 0,1,...,N-1$

**Inverse Discrete Fourier Transform (IDFT):**

The following formula recovers $f(x)$ from a series coefficients $\hat{f}(u)$.

$f(x) = \sum_{u=0}^{N-1} \hat{f}(u) e^{i2 \pi \frac{ux}{N}}$

where $x=0,1,...,N-1$



**Task 1:**

Generate the signal $f(x)$ below which consists of multiple sin and cosine terms with different amplitudes. The sampling frequency $fs$ should be 500Hz (500 sample points/second). Sample points over two periods (N=1000)

$f(x) = 1.5 + 3 \cdot \sin(2 \pi \cdot 15 \cdot x) + \cos(2\pi \cdot 15 \cdot x) + 2 \cdot \sin(2pi \cdot 30 \cdot x) + \sin(2\pi \cdot 50 \cdot x)$

Finally, plot the generated signal.



**Task 2**:

- Implement two functions `dft` and `idft` that compute the DFT and IDFT.

  ````python
  def dft(signal):
     	....
  	return coeffs
  
  def idft(coeffs):
      ....
      return signal
  ````



**Task 3:**

- Use `dft` to convert the generated signal $f(x)$ into the frequency domain. Plot the magnitude spectrum of the signal. If implemented correctly, the spectrum should have 7 spikes.

  Explain why there are 7 spikes and not less? Hint: Think about what we said about Euler's Formula and what happens to the imaginary parts.



**Task 4:**

- Assuming that we do not know frequencies which are contained in the original signal, recover the contained frequencies and "strength" of the contribution to the signal from the spectrum.

  **Hint:** Frequency per Bin = fs / N



**Task 5:**

- Remove the sinusoid with frequency $f=50$ by "filtering" in the frequency domain. Afterwards, us the `idft` function to obtain the filtered signal in the time domain. Verify that the result is correct (e.g., by comparing it to another synthesized signal)



**Task 6:**

- For frequency $f=15$, we have both a sine and a cosine. How can we determine the amplitudes of the sine and cosine wave from the coefficients?
