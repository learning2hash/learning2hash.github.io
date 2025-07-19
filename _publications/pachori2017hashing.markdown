---
layout: publication
title: Hashing in the Zero Shot Framework with Domain Adaptation
authors: Pachori Shubham, Deshpande Ameya, Raman Shanmuganathan
conference: Neurocomputing
year: 2017
bibkey: pachori2017hashing
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.01933'}]
tags: [Tools & Libraries, Hashing Methods]
---
Techniques to learn hash codes which can store and retrieve large dimensional
multimedia data efficiently have attracted broad research interests in the
recent years. With rapid explosion of newly emerged concepts and online data,
existing supervised hashing algorithms suffer from the problem of scarcity of
ground truth annotations due to the high cost of obtaining manual annotations.
Therefore, we propose an algorithm to learn a hash function from training
images belonging to `seen' classes which can efficiently encode images of
`unseen' classes to binary codes. Specifically, we project the image features
from visual space and semantic features from semantic space into a common
Hamming subspace. Earlier works to generate hash codes have tried to relax the
discrete constraints on hash codes and solve the continuous optimization
problem. However, it often leads to quantization errors. In this work, we use
the max-margin classifier to learn an efficient hash function. To address the
concern of domain-shift which may arise due to the introduction of new classes,
we also introduce an unsupervised domain adaptation model in the proposed
hashing framework. Results on the three datasets show the advantage of using
domain adaptation in learning a high-quality hash function and superiority of
our method for the task of image retrieval performance as compared to several
state-of-the-art hashing methods.