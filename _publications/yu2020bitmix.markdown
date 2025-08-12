---
layout: publication
title: 'Bitmix: Data Augmentation For Image Steganalysis'
authors: In-Jae Yu, Wonhyuk Ahn, Seung-Hun Nam, Heung-Kyu Lee
conference: Electronics Letters
year: 2020
bibkey: yu2020bitmix
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.16625'}]
tags: ["Evaluation"]
short_authors: Yu et al.
---
Convolutional neural networks (CNN) for image steganalysis demonstrate better
performances with employing concepts from high-level vision tasks. The major
employed concept is to use data augmentation to avoid overfitting due to
limited data. To augment data without damaging the message embedding, only
rotating multiples of 90 degrees or horizontally flipping are used in
steganalysis, which generates eight fixed results from one sample. To overcome
this limitation, we propose BitMix, a data augmentation method for spatial
image steganalysis. BitMix mixes a cover and stego image pair by swapping the
random patch and generates an embedding adaptive label with the ratio of the
number of pixels modified in the swapped patch to those in the cover-stego
pair. We explore optimal hyperparameters, the ratio of applying BitMix in the
mini-batch, and the size of the bounding box for swapping patch. The results
reveal that using BitMix improves the performance of spatial image steganalysis
and better than other data augmentation methods.