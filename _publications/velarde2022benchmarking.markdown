---
layout: publication
title: Benchmarking Algorithms For Automatic License Plate Recognition
authors: Marcel del Castillo Velarde, Gissel Velarde
conference: Arxiv
year: 2022
bibkey: velarde2022benchmarking
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14298'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Marcel del Castillo Velarde, Gissel Velarde
---
We evaluated a lightweight Convolutional Neural Network (CNN) called LPRNet
[1] for automatic License Plate Recognition (LPR). We evaluated the algorithm
on two datasets, one composed of real license plate images and the other of
synthetic license plate images. In addition, we compared its performance
against Tesseract [2], an Optical Character Recognition engine. We measured
performance based on recognition accuracy and Levenshtein Distance. LPRNet is
an end-to-end framework and demonstrated robust performance on both datasets,
delivering 90 and 89 percent recognition accuracy on test sets of 1000 real and
synthetic license plate images, respectively. Tesseract was not trained using
real license plate images and performed well only on the synthetic dataset
after pre-processing steps delivering 93 percent recognition accuracy. Finally,
Pareto analysis for frequency analysis of misclassified characters allowed us
to find in detail which characters were the most conflicting ones according to
the percentage of accumulated error. Depending on the region, license plate
images possess particular characteristics. Once properly trained, LPRNet can be
used to recognize characters from a specific region and dataset. Future work
can focus on applying transfer learning to utilize the features learned by
LPRNet and fine-tune it given a smaller, newer dataset of license plates.