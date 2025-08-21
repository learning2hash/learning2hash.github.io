---
layout: publication
title: In-memory Nearest Neighbor Search With Fefet Multi-bit Content-addressable
  Memories
authors: "Arman Kazemi, Mohammad Mehdi Sharifi, Ann Franchesca Laguna, Franz M\xFC\
  ller, Ramin Rajaei, Ricardo Olivo, Thomas K\xE4mpfe, Michael Niemier, X. Sharon\
  \ Hu"
conference: 2021 Design, Automation &amp; Test in Europe Conference &amp; Exhibition
  (DATE)
year: 2021
bibkey: kazemi2020in
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.07095'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Kazemi et al.
---
Nearest neighbor (NN) search is an essential operation in many applications,
such as one/few-shot learning and image classification. As such, fast and
low-energy hardware support for accurate NN search is highly desirable. Ternary
content-addressable memories (TCAMs) have been proposed to accelerate NN search
for few-shot learning tasks by implementing \(L_\infty\) and Hamming distance
metrics, but they cannot achieve software-comparable accuracies. This paper
proposes a novel distance function that can be natively evaluated with
multi-bit content-addressable memories (MCAMs) based on ferroelectric FETs
(FeFETs) to perform a single-step, in-memory NN search. Moreover, this approach
achieves accuracies comparable to floating-point precision implementations in
software for NN classification and one/few-shot learning tasks. As an example,
the proposed method achieves a 98.34% accuracy for a 5-way, 5-shot
classification task for the Omniglot dataset (only 0.8% lower than
software-based implementations) with a 3-bit MCAM. This represents a 13%
accuracy improvement over state-of-the-art TCAM-based implementations at
iso-energy and iso-delay. The presented distance function is resilient to the
effects of FeFET device-to-device variations. Furthermore, this work
experimentally demonstrates a 2-bit implementation of FeFET MCAM using AND
arrays from GLOBALFOUNDRIES to further validate proof of concept.