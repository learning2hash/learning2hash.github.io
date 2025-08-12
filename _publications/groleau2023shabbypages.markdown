---
layout: publication
title: 'Shabbypages: A Reproducible Document Denoising And Binarization Dataset'
authors: Alexander Groleau, Kok Wei Chee, Stefan Larson, Samay Maini, Jonathan Boarman
conference: Arxiv
year: 2023
bibkey: groleau2023shabbypages
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.09339'}]
tags: ["Datasets", "Evaluation"]
short_authors: Groleau et al.
---
Document denoising and binarization are fundamental problems in the document
processing space, but current datasets are often too small and lack sufficient
complexity to effectively train and benchmark modern data-driven machine
learning models. To fill this gap, we introduce ShabbyPages, a new document
image dataset designed for training and benchmarking document denoisers and
binarizers. ShabbyPages contains over 6,000 clean "born digital" images with
synthetically-noised counterparts ("shabby pages") that were augmented using
the Augraphy document augmentation tool to appear as if they have been printed
and faxed, photocopied, or otherwise altered through physical processes. In
this paper, we discuss the creation process of ShabbyPages and demonstrate the
utility of ShabbyPages by training convolutional denoisers which remove real
noise features with a high degree of human-perceptible fidelity, establishing
baseline performance for a new ShabbyPages benchmark.