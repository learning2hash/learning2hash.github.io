---
layout: publication
title: 'Learning Hash Codes Via Hamming Distance Targets'
authors: Martin Loncaric, Bowei Liu, Ryan Weber
conference: "Arxiv"
year: 2018
citations: 4
bibkey: loncaric2018learning
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1810.01008'}
tags: ['Cross-Modal', 'Independent', 'Retrieval Models', 'Evaluation', 'Shallow', 'Datasets', 'Training Strategy', 'Hashing']
---
We present a powerful new loss function and training scheme for learning
binary hash codes with any differentiable model and similarity function. Our
loss function improves over prior methods by using log likelihood loss on top
of an accurate approximation for the probability that two inputs fall within a
Hamming distance target. Our novel training scheme obtains a good estimate of
the true gradient by better sampling inputs and evaluating loss terms between
all pairs of inputs in each minibatch. To fully leverage the resulting hashes,
we use multi-indexing. We demonstrate that these techniques provide large
improvements to a similarity search tasks. We report the best results to date
on competitive information retrieval tasks for ImageNet and SIFT 1M, improving
MAP from 73% to 84% and reducing query cost by a factor of 2-8, respectively.
