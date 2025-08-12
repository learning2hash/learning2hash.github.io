---
layout: publication
title: Forming Local Intersections Of Projections For Classifying And Searching Histopathology
  Images
authors: Aditya Sriram, Shivam Kalra, Morteza Babaie, Brady Kieffer, Waddah Al Drobi,
  Shahryar Rahnamayan, Hany Kashani, Hamid R. Tizhoosh
conference: Arxiv
year: 2020
bibkey: sriram2020forming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.03553'}]
tags: []
short_authors: Sriram et al.
---
In this paper, we propose a novel image descriptor called Forming Local
Intersections of Projections (FLIP) and its multi-resolution version (mFLIP)
for representing histopathology images. The descriptor is based on the Radon
transform wherein we apply parallel projections in small local neighborhoods of
gray-level images. Using equidistant projection directions in each window, we
extract unique and invariant characteristics of the neighborhood by taking the
intersection of adjacent projections. Thereafter, we construct a histogram for
each image, which we call the FLIP histogram. Various resolutions provide
different FLIP histograms which are then concatenated to form the mFLIP
descriptor. Our experiments included training common networks from scratch and
fine-tuning pre-trained networks to benchmark our proposed descriptor.
Experiments are conducted on the publicly available dataset KIMIA Path24 and
KIMIA Path960. For both of these datasets, FLIP and mFLIP descriptors show
promising results in all experiments.Using KIMIA Path24 data, FLIP outperformed
non-fine-tuned Inception-v3 and fine-tuned VGG16 and mFLIP outperformed
fine-tuned Inception-v3 in feature extracting.