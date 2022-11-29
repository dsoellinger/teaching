# Exercise Sheet 7



## Exercise 7.1 (6 points)

In this exercise you will implement and test various frequency-domain lowpass/highpass filters.

**Task 1:**

- Implement the following filters/functions which should filter the given DFT coefficients of an image.

  ```````python
  def ideal_lowpass_filter(coeffs, cutoff_freq):
  	...
  	return filtered_coeffs
  
  def ideal_highpass_filter(coeffs, cutoff_freq):
      ...
      return filtered_coeffs
  
  def butterworth_lowpass_filter(coeffs, cutoff_freq, n):
      ...
      return filtered_coeffs
  
  def butterworth_highpass_filter(img, cutoff_freq, n):
      ...
      return filtered_coeffs
  ```````

**Task 2:**

- Take an image of you choice, convert it to the frequency domain. You can use functions such as `scipy.fft.fft2` for this purpose.
- Play around with each of filter functions using different parameters. Plot the magnitude spectrum and filtered image in the spatial domain.
- Note which interesting observations you have made. For instance, did you encounter ringing, etc?



## Exercise 7.2 (5 points)

In this exercise you will use the Short Time Frequency Transform (STFT) to analyze a signal.

Load the signal (numpy array) contained in `signal.npy`. This can be achieved by running `np.load('signal.npy')`

Now study the signal using the STFT (e.g., using `scipy.signal.stft`) which is composed of multiple sinusoids with different amplitudes/frequencies. The signal has been sampled with a sampling frequency of 1000 Hz.

**Task:** Name which sine waves are contained in the signal --- Which frequency and amplitude does each sine wave have? When exactly (after how many seconds) does each sine waves occur? Obviously our answer should reflect how you obtained the information from the signal.



**Note:** Alternatively, instead of using the STFT, you can checkout the Continuous Wavelet Transform (CWT) in [PyWavelet](https://pywavelets.readthedocs.io/en/latest/ref/cwt.html).

 
