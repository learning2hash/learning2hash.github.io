---
layout: publication
title: Meta-learning For Color-to-infrared Cross-modal Style Transfer
authors: Evelyn A. Stump, Francesco Luzi, Leslie M. Collins, Jordan M. Malof
conference: Arxiv
year: 2022
bibkey: stump2022meta
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.12824'}]
tags: []
short_authors: Stump et al.
---
Recent object detection models for infrared (IR) imagery are based upon deep
neural networks (DNNs) and require large amounts of labeled training imagery.
However, publicly available datasets that can be used for such training are
limited in their size and diversity. To address this problem, we explore
cross-modal style transfer (CMST) to leverage large and diverse color imagery
datasets so that they can be used to train DNN-based IR image-based object
detectors. We evaluate six contemporary stylization methods on four
publicly-available IR datasets - the first comparison of its kind - and find
that CMST is highly effective for DNN-based detectors. Surprisingly, we find
that existing data-driven methods are outperformed by a simple grayscale
stylization (an average of the color channels). Our analysis reveals that
existing data-driven methods are either too simplistic or introduce significant
artifacts into the imagery. To overcome these limitations, we propose
meta-learning style transfer (MLST), which learns a stylization by composing
and tuning well-behaved analytic functions. We find that MLST leads to more
complex stylizations without introducing significant image artifacts and
achieves the best overall detector performance on our benchmark datasets.