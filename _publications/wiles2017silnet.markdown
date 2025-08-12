---
layout: publication
title: 'Silnet : Single- And Multi-view Reconstruction By Learning From Silhouettes'
authors: Olivia Wiles, Andrew Zisserman
conference: Procedings of the British Machine Vision Conference 2017
year: 2017
bibkey: wiles2017silnet
citations: 93
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.07888'}]
tags: []
short_authors: Olivia Wiles, Andrew Zisserman
---
The objective of this paper is 3D shape understanding from single and
multiple images. To this end, we introduce a new deep-learning architecture and
loss function, SilNet, that can handle multiple views in an order-agnostic
manner. The architecture is fully convolutional, and for training we use a
proxy task of silhouette prediction, rather than directly learning a mapping
from 2D images to 3D shape as has been the target in most recent work.
  We demonstrate that with the SilNet architecture there is generalisation over
the number of views -- for example, SilNet trained on 2 views can be used with
3 or 4 views at test-time; and performance improves with more views.
  We introduce two new synthetics datasets: a blobby object dataset useful for
pre-training, and a challenging and realistic sculpture dataset; and
demonstrate on these datasets that SilNet has indeed learnt 3D shape. Finally,
we show that SilNet exceeds the state of the art on the ShapeNet benchmark
dataset, and use SilNet to generate novel views of the sculpture dataset.