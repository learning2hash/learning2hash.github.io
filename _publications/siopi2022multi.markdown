---
layout: publication
title: A Multi-stream Fusion Network For Image Splicing Localization
authors: Maria Siopi, Giorgos Kordopatis-zilos, Polychronis Charitidis, Ioannis Kompatsiaris,
  Symeon Papadopoulos
conference: Lecture Notes in Computer Science
year: 2023
bibkey: siopi2022multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.01128'}]
tags: []
short_authors: Siopi et al.
---
In this paper, we address the problem of image splicing localization with a
multi-stream network architecture that processes the raw RGB image in parallel
with other handcrafted forensic signals. Unlike previous methods that either
use only the RGB images or stack several signals in a channel-wise manner, we
propose an encoder-decoder architecture that consists of multiple encoder
streams. Each stream is fed with either the tampered image or handcrafted
signals and processes them separately to capture relevant information from each
one independently. Finally, the extracted features from the multiple streams
are fused in the bottleneck of the architecture and propagated to the decoder
network that generates the output localization map. We experiment with two
handcrafted algorithms, i.e., DCT and Splicebuster. Our proposed approach is
benchmarked on three public forensics datasets, demonstrating competitive
performance against several competing methods and achieving state-of-the-art
results, e.g., 0.898 AUC on CASIA.