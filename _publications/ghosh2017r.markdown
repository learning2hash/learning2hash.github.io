---
layout: publication
title: 'R-PHOC: Segmentation-free Word Spotting Using CNN'
authors: Suman Ghosh, Ernest Valveny
conference: 2017 14th IAPR International Conference on Document Analysis and Recognition
  (ICDAR)
year: 2017
bibkey: ghosh2017r
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.01294'}]
tags: ["Datasets", "Similarity Search"]
short_authors: Suman Ghosh, Ernest Valveny
---
This paper proposes a region based convolutional neural network for
segmentation-free word spotting. Our net- work takes as input an image and a
set of word candidate bound- ing boxes and embeds all bounding boxes into an
embedding space, where word spotting can be casted as a simple nearest
neighbour search between the query representation and each of the candidate
bounding boxes. We make use of PHOC embedding as it has previously achieved
significant success in segmentation- based word spotting. Word candidates are
generated using a simple procedure based on grouping connected components using
some spatial constraints. Experiments show that R-PHOC which operates on images
directly can improve the current state-of- the-art in the standard GW dataset
and performs as good as PHOCNET in some cases designed for segmentation based
word spotting.