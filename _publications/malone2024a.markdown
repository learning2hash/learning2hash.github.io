---
layout: publication
title: 'A Hyperdimensional One Place Signature To Represent Them All: Stackable Descriptors
  For Visual Place Recognition'
authors: Connor Malone, Somayeh Hussaini, Tobias Fischer, Michael Milford
conference: Arxiv
year: 2024
bibkey: malone2024a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.06153'}]
tags: [Robustness, Datasets, Scalability, Evaluation, Tools & Libraries, Neural Hashing]
short_authors: Malone et al.
---
Visual Place Recognition (VPR) enables coarse localization by comparing query images to a reference database of geo-tagged images. Recent breakthroughs in deep learning architectures and training regimes have led to methods with improved robustness to factors like environment appearance change, but with the downside that the required training and/or matching compute scales with the number of distinct environmental conditions encountered. Here, we propose Hyperdimensional One Place Signatures (HOPS) to simultaneously improve the performance, compute and scalability of these state-of-the-art approaches by fusing the descriptors from multiple reference sets captured under different conditions. HOPS scales to any number of environmental conditions by leveraging the Hyperdimensional Computing framework. Extensive evaluations demonstrate that our approach is highly generalizable and consistently improves recall performance across all evaluated VPR methods and datasets by large margins. Arbitrarily fusing reference images without compute penalty enables numerous other useful possibilities, three of which we demonstrate here: descriptor dimensionality reduction with no performance penalty, stacking synthetic images, and coarse localization to an entire traverse or environmental section.