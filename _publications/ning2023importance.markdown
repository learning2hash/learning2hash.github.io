---
layout: publication
title: The Importance Of Anti-aliasing In Tiny Object Detection
authors: Jinlai Ning, Michael Spratling
conference: Arxiv
year: 2023
bibkey: ning2023importance
citations: 1
additional_links: [{name: Code, url: 'https://github.com/freshn/Anti-aliasing-Tiny-Object-Detection.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.14221'}]
tags: []
short_authors: Jinlai Ning, Michael Spratling
---
Tiny object detection has gained considerable attention in the research
community owing to the frequent occurrence of tiny objects in numerous critical
real-world scenarios. However, convolutional neural networks (CNNs) used as the
backbone for object detection architectures typically neglect Nyquist's
sampling theorem during down-sampling operations, resulting in aliasing and
degraded performance. This is likely to be a particular issue for tiny objects
that occupy very few pixels and therefore have high spatial frequency features.
This paper applied an existing approach WaveCNet for anti-aliasing to tiny
object detection. WaveCNet addresses aliasing by replacing standard
down-sampling processes in CNNs with Wavelet Pooling (WaveletPool) layers,
effectively suppressing aliasing. We modify the original WaveCNet to apply
WaveletPool in a consistent way in both pathways of the residual blocks in
ResNets. Additionally, we also propose a bottom-heavy version of the backbone,
which further improves the performance of tiny object detection while also
reducing the required number of parameters by almost half. Experimental results
on the TinyPerson, WiderFace, and DOTA datasets demonstrate the importance of
anti-aliasing in tiny object detection and the effectiveness of the proposed
method which achieves new state-of-the-art results on all three datasets. Codes
and experiment results are released at
https://github.com/freshn/Anti-aliasing-Tiny-Object-Detection.git.