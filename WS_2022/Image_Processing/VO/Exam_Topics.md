## Image acquisition

##### Electromagnetic spectrum

How are colors represented in the electromagnetic spectrum? Which colors can be found in the spectrum? How do we create "missing" colors (colors which do not appear in the spectrum)? How does visible light differ from other types of "signals" such as x-ray, infrared, etc.? What is the difference between "everyday" photography and, for example, medical imaging (remember that we typically need an emitter that produces a signal + a sensor for capturing)?

##### Human eye

Be able to explain the main components of the human eye and how it works. Remember the purpose of the rods/cones

##### Camera model

Be able to illustrate the working principle of a camera based on pinhole / thin lens model. Basically you should know: What is the purpose of a lens (why don't we use pinhole camera anymore)? How do we determine if on object is in focus (which parameter do we need to change). What's the purpose of the aperture and what happens if we increase/decrease the aperture (remember "circle of confusion")? How aperture relate to a pinhole camera? What do we mean when we talk about the "circle of confusion"? What happens when we "zoom" (field of view)? What is the "depth of field"?

You don't have to memorize the formulas; just make sure that you are able to sketch what's going on

##### Sensors (CMOS & CCD)

What is the main difference in the way how CMOS and CCD sensor operate? Remember charge-to-voltage and photo-to-electron conversion; and that CCD requires us to shift whereas CMOS allow direct read-out individual cells. Why are CCD sensors more difficult to operate?

What is the purpose of a Color Filter Array?

Note: You don't have to remember the different CCD read-out techniques (FF, FT, etc.)



## Image representation

##### Color representations

How do grayscale images differ from color images (multiple channels, etc)? Name a few color spaces and the differences (e.g, RGB; HSV/HSL; YUV; CYMK)? How do we convert RGB to grayscale? Where do the factors 0.5/0.3/0.2 come from? 

##### Image representations

 Be able to explain the relationship between image resolution, quantisation, storage requirements and the impact on image quality/details.

##### Distances / Connectivity

Different types of distances; What do we mean by "4/8-connectivity" (see 4/8 neighbourhood on the slides) and how does connectivity relate to different types of distances? What do we mean when we say that something is "adjacent"?

##### Pyramids / Quadtrees

What are pyramids and quad-trees? How do we construct a pyramid/quadtree? Why/where are they useful?



## Image enhancement

##### Contrast

What is contrast? How can we modify the contrast of a grayscale image? Remember that for RGB images we require a color space conversion (PS example)

##### Histogram modification / specification/ equalization

What is the goal of histogram equalization/modification? Why is probability theory (probability density) important in this context? What's the purpose of a transfer function? What steps do we need to take to histogram-equalize an image? What should an equalized histogram look like? How is "histogram equalization" related to "histogram specification"? What is the "problem" in the case of discrete images (finding the inverse function)

##### Global Histogram Equalization (GHE) / AHE / CLAHE

What is the difference between GHE and / AHE? What is the problem with AHE and how does CLAHE improve the situation?

##### Spatial domain image filters

Explain Neighbourhood Averaging and Median Filtering; How do we determine the values of a NxN kernel for neighbourhood averaging? What is a Gaussian filter and where its parameters come from?

##### Fourier Transformation / DFT

Explain Fourier Analysis and Synthesis. What information do we find in the frequency/magnitude spectrum? What information is lost in the magnitude spectrum? (--> spatial information);  What happens to the frequency spectrum in case of real signals? (--> symmetry). What does a sinusoid look like in the frequency spectrum? What does a DC signal look like in the frequency spectrum? Why do we usually shift (fftshift) the spectrum after the analysis step? (---> remember that we want to have the DC component at the center; why?); How can we replace a convolution with a fourier transform?

##### Frequency domain filters

Explain how to low-pass/high-pass filter an image in the frequency domain. What is the magnitude spectrum? Where do we find the "missing" spatial information after filtering of the magnitude spectrum? (--> phase) How do does an Ideal LPF/HPF change the frequency spectrum? What is the problem with ILPF/IHPF and what are the alternatives (e.g. Butterworth)? 

##### STFT

What is the drawback of the Fourier transform? How does the STFT solve the problem?

##### CWT / DWT

Explain the idea behind the continuous wavelet transform; How is the continuous wavelet transform different from a Fourier transform? What is a mother wavelet?; What happens to the mother wavelet during the transformation? (--> scaling+shifting); How is the DWT different from a CWT? (--> choice of the scaling/shifting parameters)

##### MRA / Filterbanks

Sketch the basic idea of the MRA; How does a filterbank (FWT) allow the fast computation of the Wavelet coefficients in O(n)?; How do we typically visualize an image that has been "wavelet-transformed"? (--> pyramid with LL, HL, LH, HH subbands)



## Convolution and Correlation

##### Convolution / Correlation

What it a kernel? Explain 1D/2D convolution/correlation. What is the "stride"? Be able to "calculate" a simple 2D convolution/correlation(!); What is the difference between a correlation/convolution and why do we typically prefer to work with the convolution? What is the purpose of padding? Name/Explain different types of padding; How can we easily turn a correlation into a convolution and vice versa?; Be able to calculate the output size for a given kernel input image;

##### Template Matching / NCC / ZNCC

Name an application for template matching; Explain the idea behind the cross-correlation formula?; What is the problem with this formula and how does the ZNCC solve this problem (PS example)



## Edge Detection

##### Edge detection using 1st derivatives

Explain how edge detection is done using 1st derivative operators; Name some kernels that approximate the 1st derivative? Why do we have two kernels (horizontal/vertical)? How can we obtain the edge orientation/normal from the gradients? How do we determine the "strength" of the edge/normal? How can we determine the orientation of an edge? How can we finally determine the boundary of an object? (--> find larger gradients + threshold)

What are compass edge detectors?

##### Edge detection using 2nd derivatives

What is a Laplacian operator? What does "isotropic" mean? What is a Mexican Hat operator / LoG?  What is the effect of the Gaussian filter on the gradients?  (what happens if we change sigma?) How can the LoG be replaced by a DoG (Difference of Gaussian)? How can we determine the boundary based on the 2nd derivatives? (find the zero-crossings)

##### Canny Edge detector

Explain the canny edge detector; Which techniques does it apply to improve the result (Hysteresis Thresholding + non-maximum suppression)? How does Non-maximum suppression work? How does hysteresis thresholding work?

##### Hough transform

Explain how the Hough transform is able to detect straight lines? Explain the alternative version of the line equation; Can we generalize this technique to support other shapes?



## Segmentation

##### Thresholding-based segmentation

What is the goal of optimal thresholding (why is it called"optimal")? Explain the idea behind Iterative Threshold Selection and the Otsu method? (you don't have to memorize the formulas). What is the problem with global thresholding and how does local thresholding solve the problem?

##### Region-based segmentation

Explain region growing/splitting/merging; What does homogeneity mean in this context? Explain K-Means clustering and Mean Shift segmentation; Explain the basic idea behind graph cut segmentation? What is a min-cut? How can we turn an image into a graph? Remember Max-flow, min-cut; What do we mean by over-segmentation? 

##### Edge-based segmentation

What problem does edge relaxation try two solve? How does edge relaxation determine with edges should be kept? What is a crack edge? Sketch the basic idea; 

How can graph search be used to detect edges? What is the purpose of the heuristics in this context? ow can we build a graph of edges to perform a graph search? Explain the algorithm based on a simple example

What is the basic idea behind the dynamic-programming based search? How does it differ from graph-search? What are the advantage/disadvantage of this approach? Explain the algorithm based on a simple example 

What is an active contour / snake? What is the basic idea? What is the purpose of the energy function? Why is the gradient important for the energy function? What properties (e.g., curvature of the snake) of the snake/split might E_int take into account?



 ## Morphological operators

Explain Erosion and Dilation based on a simple example; Explain Opening/Closing; Give some examples where it might be beneficial to use these operators; What problem does opening/closing try to solve? What effect does the size of the SE element have? What is the purpose of a hit-and-miss transform. How can we efficiently implement the operators using lookup-tables? How can we use morphological operators to extract object boundaries? How can we use morphological operators to thin/thicken an object? What is a skeleton? How does the skeletonization (MAT) differ from thinning-based approaches? What is the purpose of pruning?

What is the basic idea behind the watershed algorithm? What is a common problem with this approach? (->oversegmentation) Why do we need the morphological operators in the context of the watershed segmentation (--> dam construction)



