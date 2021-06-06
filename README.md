# ApriltagExperiment
In this repository, we want to share our experiment with apriltag. And also, we answer the questions of what is apriltag, how we use it, which component do we use and why. 
You can reach our steps from Documeents folder. And, under Code folder, test and project codes can be found. 
* Step 0 --> What is AprilTag?
* Step 1 --> Needed Componnets for our Project
* Step 2 --> AprilTag Usage with Raspberry Pi Zero W
* Step 3 --> Basic Car with Raspberry Pi Zero
* Step 4 --> Giving Basic Command to Car with AprilTag

## Introdction
We start the our project with searching what is AprilTag, how did AprilTag originate and envolve, what is the science behind it. AprilTag is a visual fiducial system, useful for a wide variety of tasks including augmented reality, robotics, and camera calibration. Targets can be created from an ordinary printer, and the AprilTag detection software computes the precise 3D position, orientation, and identity of the tags relative to the camera. The AprilTag library is implemented in C with no external dependencies. It is designed to be easily included in other applications, as well as be portable to embedded devices. Real-time performance can be achieved even on cell-phone grade processors.
You can easily reach more information from [Project Page](https://april.eecs.umich.edu/software/apriltag). 
You can reach github repo from [here](https://github.com/AprilRobotics/apriltag).
* With a QR code, a human is typically involved in aligning the camera with the tag and photographs it at fairly high resolution obtaining hundreds of bytes, such as a web address. In contrast, a visual fiducial has a small information payload (perhaps 12 bits), but is designed to be automatically detected and localized even when it is at very low resolution, unevenly lit, oddly rotated, or tucked away in the corner of an otherwise cluttered image. Visual fiducial systems are perhaps best known for their application to augmented reality, which spurred the development of several popular systems including ARToolkit and ARTag. Real-world objects can be augmented with visual fiducials, allowing virtually-generated imagery to be super-imposed. Similarly, visual fiducials can be used for basic motion capture. For more [here](https://april.eecs.umich.edu/media/pdfs/olson2011tags.pdf).
* We use AprilTag3 in our project. This work is based on the earlier AprilTag system. The design of AprilTags as a black-and-white square tag with an encoded binary payload is based on the earlier ARTag and ARToolkit. AprilTag introduced an improved method of generating binary payloads, guaranteeing a minimum Hamming distance between tags under all possible rotations, making them more robust than earlier designs. The tag generation process, a lexicode-based process with minimum complexity heuristics, was empirically shown to reduce the false positive rate compared to ARTag designs of similar bit length. For more [here](https://april.eecs.umich.edu/media/pdfs/wang2016iros.pdf). 
### Step 0
First of all, we started by understanding and summarizing the articles mentioned in the introduction section. After reviewing these articles, we reviewedAaprilTag's github page. And in this step, we've summarized what we've learned about AprilTag.
### Step 1
In this step, we mentioned which components we use and why. We initially tried to work through windows but we were unsuccessful. At the same time, as stated on the github page, linux operating systems are supported, although there have been successful ones on windows.
### Step 2
This step briefly summarizes how you can work with the Raspberry Pi Zero. It also explains the setup required for AprilTag and how to do your first test.
### Step 3 
How to connect and test the car to be created using Raspberry Pi is explained in this section.
### Step 4
How to steer the car using AprilTag is explained in this step. At the same time, the processing time of the information received from the tags is examined.
