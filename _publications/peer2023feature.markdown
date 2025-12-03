---
layout: publication
title: Feature Mixing For Writer Retrieval And Identification On Papyri Fragments
authors: Marco Peer, Robert Sablatnig
conference: Proceedings of the 7th International Workshop on Historical Document Imaging
  and Processing
year: 2023
bibkey: peer2023feature
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.12939'}]
tags: ["Evaluation", "Neural Hashing"]
short_authors: Marco Peer, Robert Sablatnig
---
This paper proposes a deep-learning-based approach to writer retrieval and
identification for papyri, with a focus on identifying fragments associated
with a specific writer and those corresponding to the same image. We present a
novel neural network architecture that combines a residual backbone with a
feature mixing stage to improve retrieval performance, and the final descriptor
is derived from a projection layer. The methodology is evaluated on two
benchmarks: PapyRow, where we achieve a mAP of 26.6 % and 24.9 % on writer and
page retrieval, and HisFragIR20, showing state-of-the-art performance (44.0 %
and 29.3 % mAP). Furthermore, our network has an accuracy of 28.7 % for writer
identification. Additionally, we conduct experiments on the influence of two
binarization techniques on fragments and show that binarizing does not enhance
performance. Our code and models are available to the community.