---
layout: publication
title: Synthetic Data Generation For Anomaly Detection On Table Grapes
authors: Ionut Marian Motoi, Valerio Belli, Alberto Carpineto, Daniele Nardi, Thomas
  Alessandro Ciarfuglia
conference: Smart Agricultural Technology
year: 2025
bibkey: motoi2024synthetic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.12949'}]
tags: ["Datasets"]
short_authors: Motoi et al.
---
Early detection of illnesses and pest infestations in fruit cultivation is
critical for maintaining yield quality and plant health. Computer vision and
robotics are increasingly employed for the automatic detection of such issues,
particularly using data-driven solutions. However, the rarity of these problems
makes acquiring and processing the necessary data to train such algorithms a
significant obstacle. One solution to this scarcity is the generation of
synthetic high-quality anomalous samples. While numerous methods exist for this
task, most require highly trained individuals for setup.
  This work addresses the challenge of generating synthetic anomalies in an
automatic fashion that requires only an initial collection of normal and
anomalous samples from the user - a task that is straightforward for farmers.
We demonstrate the approach in the context of table grape cultivation.
Specifically, based on the observation that normal berries present relatively
smooth surfaces, while defects result in more complex textures, we introduce a
Dual-Canny Edge Detection (DCED) filter. This filter emphasizes the additional
texture indicative of diseases, pest infestations, or other defects. Using
segmentation masks provided by the Segment Anything Model, we then select and
seamlessly blend anomalous berries onto normal ones. We show that the proposed
dataset augmentation technique improves the accuracy of an anomaly classifier
for table grapes and that the approach can be generalized to other fruit types.