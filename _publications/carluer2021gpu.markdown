---
layout: publication
title: GPU Optimization Of The 3D Scale-invariant Feature Transform Algorithm And
  A Novel Brief-inspired 3D Fast Descriptor
authors: Jean-Baptiste Carluer, Laurent Chauvin, Jie Luo, William M. Wells, Ines MacHado,
  Rola Harmouche, Matthew Toews
conference: Arxiv
year: 2021
bibkey: carluer2021gpu
citations: 0
additional_links: [{name: Code, url: 'https://github.com/CarluerJB/3D_SIFT_CUDA'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.10258'}]
tags: ["Efficiency"]
short_authors: Carluer et al.
---
This work details a highly efficient implementation of the 3D scale-invariant
feature transform (SIFT) algorithm, for the purpose of machine learning from
large sets of volumetric medical image data. The primary operations of the 3D
SIFT code are implemented on a graphics processing unit (GPU), including
convolution, sub-sampling, and 4D peak detection from scale-space pyramids. The
performance improvements are quantified in keypoint detection and
image-to-image matching experiments, using 3D MRI human brain volumes of
different people. Computationally efficient 3D keypoint descriptors are
proposed based on the Binary Robust Independent Elementary Feature (BRIEF)
code, including a novel descriptor we call Ranked Robust Independent Elementary
Features (RRIEF), and compared to the original 3D SIFT-Rank
method\citep\{toews2013efficient\}. The GPU implementation affords a speedup of
approximately 7X beyond an optimised CPU implementation, where computation time
is reduced from 1.4 seconds to 0.2 seconds for 3D volumes of size (145, 174,
145) voxels with approximately 3000 keypoints. Notable speedups include the
convolution operation (20X), 4D peak detection (3X), sub-sampling (3X), and
difference-of-Gaussian pyramid construction (2X). Efficient descriptors offer a
speedup of 2X and a memory savings of 6X compared to standard SIFT-Rank
descriptors, at a cost of reduced numbers of keypoint correspondences,
revealing a trade-off between computational efficiency and algorithmic
performance. The speedups gained by our implementation will allow for a more
efficient analysis on larger data sets. Our optimized GPU implementation of the
3D SIFT-Rank extractor is available at
https://github.com/CarluerJB/3D_SIFT_CUDA.