---
layout: publication
title: Part-based R-cnns For Fine-grained Category Detection
authors: Ning Zhang, Jeff Donahue, Ross Girshick, Trevor Darrell
conference: Lecture Notes in Computer Science
year: 2014
bibkey: zhang2014part
citations: 1116
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.3867'}]
tags: []
short_authors: Zhang et al.
---
Semantic part localization can facilitate fine-grained categorization by
explicitly isolating subtle appearance differences associated with specific
object parts. Methods for pose-normalized representations have been proposed,
but generally presume bounding box annotations at test time due to the
difficulty of object detection. We propose a model for fine-grained
categorization that overcomes these limitations by leveraging deep
convolutional features computed on bottom-up region proposals. Our method
learns whole-object and part detectors, enforces learned geometric constraints
between them, and predicts a fine-grained category from a pose-normalized
representation. Experiments on the Caltech-UCSD bird dataset confirm that our
method outperforms state-of-the-art fine-grained categorization methods in an
end-to-end evaluation without requiring a bounding box at test time.