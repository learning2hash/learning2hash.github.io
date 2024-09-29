---
layout: publication
title: Learning Hash Codes Via Hamming Distance Targets
authors: Loncaric Martin, Liu Bowei, Weber Ryan
conference: "Arxiv"
year: 2018
bibkey: loncaric2018learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1810.01008"}
tags: ['ARXIV', 'Independent']
---
We present a powerful new loss function and training scheme for learning binary hash codes with any differentiable model and similarity function. Our loss function improves over prior methods by using log likelihood loss on top of an accurate approximation for the probability that two inputs fall within a Hamming distance target. Our novel training scheme obtains a good estimate of the true gradient by better sampling inputs and evaluating loss terms between all pairs of inputs in each minibatch. To fully leverage the resulting hashes we use multi45;indexing. We demonstrate that these techniques provide large improvements to a similarity search tasks. We report the best results to date on competitive information retrieval tasks for ImageNet and SIFT 1M improving MAP from 7337; to 8437; and reducing query cost by a factor of 245;8 respectively.
