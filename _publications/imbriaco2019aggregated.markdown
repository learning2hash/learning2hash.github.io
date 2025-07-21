---
layout: publication
title: Aggregated Deep Local Features for Remote Sensing Image Retrieval
authors: Imbriaco et al.
conference: Remote Sensing
year: 2019
bibkey: imbriaco2019aggregated
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.09469'}]
tags: ["Image-Retrieval"]
---
Remote Sensing Image Retrieval remains a challenging topic due to the special
nature of Remote Sensing Imagery. Such images contain various different
semantic objects, which clearly complicates the retrieval task. In this paper,
we present an image retrieval pipeline that uses attentive, local convolutional
features and aggregates them using the Vector of Locally Aggregated Descriptors
(VLAD) to produce a global descriptor. We study various system parameters such
as the multiplicative and additive attention mechanisms and descriptor
dimensionality. We propose a query expansion method that requires no external
inputs. Experiments demonstrate that even without training, the local
convolutional features and global representation outperform other systems.
After system tuning, we can achieve state-of-the-art or competitive results.
Furthermore, we observe that our query expansion method increases overall
system performance by about 3%, using only the top-three retrieved images.
Finally, we show how dimensionality reduction produces compact descriptors with
increased retrieval performance and fast retrieval computation times, e.g. 50%
faster than the current systems.