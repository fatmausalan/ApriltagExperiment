
## AprilTag: A robust and flexible visual fiducial system
  
  &emsp;AprilTags are unlike 2D barcode systems in which the position of the barcode in the image is unimportant, visual fiducial systems provide camera-relative position and orientation of a tag. Fiducial systems also are designed to detect multiple markers in a single image.

### Detector
  
  &emsp;In this section, we will examine the detector whose job is to estimate the position of possible tags in an image.
![Screenshot_10](https://user-images.githubusercontent.com/49456613/121805023-f2a13300-cc51-11eb-8ad9-4374cf5761b4.jpg)

1. Detecting line segments
  
  &emsp; A graph is created in which each node represents a pixel. Edges are added between adjacent pixels with an edge weight equal to the pixels’ difference in gradient direction. These edges are then sorted and processed in terms of increasing edge weight: for each edge, we test whether the connected components that the pixels belong to should be joined together. 
  &emsp;Gradient-based clustering method has used is sensitive to noise in the image: even modest amounts of noise will cause local gradient directions to vary, inhibiting the growth of the components. The solution to this problem is to low-pass filter the image.
  
  ![image](https://user-images.githubusercontent.com/49456613/121805136-7a873d00-cc52-11eb-8642-59b659e65f07.png)
    
  &emsp;Once the clustering operation is complete, line segments are fit to each connected component using a traditional least-squares procedure, weighting each point by its gradient magnitude (see Fig. 3). We adjust each line segment so that the dark side of the line is on its left, and the light side is on its right. In the next phase of processing, this allows us to enforce a winding rule around each quad.

2. Quad detection
  
  &emsp; At this point, a set of directed line segments have been computed for an image. The next task is to find sequences of line segments that form a 4-sided shape, i.e., a quad. The challenge is to do this while being as robust as possible to occlusions and noise in the line segmentations.
  &emsp; Once four lines have been found, a candidate quad detection is created. The corners of this quad are the intersections of the lines that comprise it. Because the lines are fit using data from many pixels, these corner estimates are accurate to a small fraction of a pixel.
  
3. Homography and extrinsics estimation
    
  &emsp; Computation of the tag’s position and orientation requires additional information: the camera’s focal length and the physical size of the tag. The 3 × 3 homography matrix (computed by the DLT (Direct Linear Transform)) can be written as the product of the 3 × 4 camera projection matrix P (which we assume is known) and the 4×3 truncated extrinsics matrix E. Extrinsics matrix are typically 4 × 4, but every position on the tag is at z = 0 in the tag’s coordinate system. Thus, we can rewrite every tag coordinate as a 2D homogeneous point with z implicitly zero, and remove the third column of the extrinsics matrix, forming the truncated extrinsics matrix.
  
### Payload Decoding
  &emsp; The final task is to read the bits from the payload field. We do this by computing the tag-relative coordinates of each bit field, transforming them into image coordinates using the homography, and then thresholding the resulting pixels. In order to be robust to lighting (which can vary not only from tag to tag, but also within a tag), we use a spatially-varying threshold.
  
  &emsp; Specifically, we build spatially-varying model of the intensity of “black” pixels, and a second model for the intensity of “white” models. We use the border of the tag, which contains known examples of both white and black pixels, to learn this model (see Fig. 4). We use the following intensity model:
    
  &emsp; &emsp; I(x, y) = Ax + Bxy + Cy + D (4)
    
    
  &emsp; This model has four parameters which are easily computed using least squares regression. We build two such models, one for black, the other for white. The threshold used when decoding data bits is then just the average of the predicted intensity values of the black and white models.


### Coding System
  &emsp; Once the data payload is decoded from a quad, it is the job of the coding system to determine it is valid or not. The goals of a coding system are to:
      
    - Maximize the number of distinguishable codes  
    - Maximize the number of bit errors that can be detected or corrected
    - Minimize the false positive/inter-tag confusion rate
    - Minimize the total number of bits per tag (and thus the size of the tag)
  &emsp; These goals are often in conflict, and so a given code represents a trade-off. In this section, we describe a new coding system based on lexicodes that provides significant advantages over previous methods. Our procedure can generate lexicodes with a variety of properties, allowing the user to use a code that best fits their needs.
  
### Conclusion

  We have described a visual fiducial system that significantly improves upon previous methods. We described a new approach for detecting edges using a graph-based clustering method along with a coding system that is demonstrably stronger than previous methods.
    
  &emsp; In contrast to other systems (with the notable exception of ARToolkit), our implementation is fully open. Our source code and benchmarking software are freely available:
  
  http://april.eecs.umich.edu/
  
  
## References 
* https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf
