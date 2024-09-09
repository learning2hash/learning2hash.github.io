---
layout: publication
title: "Efficient image retrieval using multi neural hash codes and bloom filters"
authors: Chakrabarti Sourin
conference: Arxiv
year: 2020
bibkey: chakrabarti2020efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.03234"}
tags: ['ARXIV', 'Image Retrieval', 'TIP']
---
This paper aims to deliver an efficient and modified approach for image
retrieval using multiple neural hash codes and limiting the number of queries
using bloom filters by identifying false positives beforehand. Traditional
approaches involving neural networks for image retrieval tasks tend to use
higher layers for feature extraction. But it has been seen that the activations
of lower layers have proven to be more effective in a number of scenarios. In
our approach, we have leveraged the use of local deep convolutional neural
networks which combines the powers of both the features of lower and higher
layers for creating feature maps which are then compressed using PCA and fed to
a bloom filter after binary sequencing using a modified multi k-means approach.
The feature maps obtained are further used in the image retrieval process in a
hierarchical coarse-to-fine manner by first comparing the images in the higher
layers for semantically similar images and then gradually moving towards the
lower layers searching for structural similarities. While searching, the neural
hashes for the query image are again calculated and queried in the bloom filter
which tells us whether the query image is absent in the set or maybe present. If
the bloom filter doesn't necessarily rule out the query, then it goes into the
image retrieval process. This approach can be particularly helpful in cases
where the image store is distributed since the approach supports parallel
querying.
