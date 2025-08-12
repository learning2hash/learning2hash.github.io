---
layout: publication
title: Performance Analysis Of Keypoint Detectors And Binary Descriptors Under Varying
  Degrees Of Photometric And Geometric Transformations
authors: Shuvo Kumar Paul, Pourya Hoseini, Mircea Nicolescu, Monica Nicolescu
conference: Journal of Image and Graphics
year: 2021
bibkey: paul2020performance
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.04135'}]
tags: ["Evaluation"]
short_authors: Paul et al.
---
Detecting image correspondences by feature matching forms the basis of
numerous computer vision applications. Several detectors and descriptors have
been presented in the past, addressing the efficient generation of features
from interest points (keypoints) in an image. In this paper, we investigate
eight binary descriptors (AKAZE, BoostDesc, BRIEF, BRISK, FREAK, LATCH, LUCID,
and ORB) and eight interest point detector (AGAST, AKAZE, BRISK, FAST,
HarrisLapalce, KAZE, ORB, and StarDetector). We have decoupled the detection
and description phase to analyze the interest point detectors and then evaluate
the performance of the pairwise combination of different detectors and
descriptors. We conducted experiments on a standard dataset and analyzed the
comparative performance of each method under different image transformations.
We observed that: (1) the FAST, AGAST, ORB detectors were faster and detected
more keypoints, (2) the AKAZE and KAZE detectors performed better under
photometric changes while ORB was more robust against geometric changes, (3) in
general, descriptors performed better when paired with the KAZE and AKAZE
detectors, (4) the BRIEF, LUCID, ORB descriptors were relatively faster, and
(5) none of the descriptors did particularly well under geometric
transformations, only BRISK, FREAK, and AKAZE showed reasonable resiliency.