---
layout: publication
title: Learning Semantic Part-based Models From Google Images
authors: Davide Modolo, Vittorio Ferrari
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: modolo2016learning
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.03140'}]
tags: []
short_authors: Davide Modolo, Vittorio Ferrari
---
We propose a technique to train semantic part-based models of object classes
from Google Images. Our models encompass the appearance of parts and their
spatial arrangement on the object, specific to each viewpoint. We learn these
rich models by collecting training instances for both parts and objects, and
automatically connecting the two levels. Our framework works incrementally, by
learning from easy examples first, and then gradually adapting to harder ones.
A key benefit of this approach is that it requires no manual part location
annotations. We evaluate our models on the challenging PASCAL-Part dataset [1]
and show how their performance increases at every step of the learning, with
the final models more than doubling the performance of directly training from
images retrieved by querying for part names (from 12.9 to 27.2 AP). Moreover,
we show that our part models can help object detection performance by enriching
the R-CNN detector with parts.