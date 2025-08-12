---
layout: publication
title: Improving Transfer Learning With A Dual Image And Video Transformer For Multi-label
  Movie Trailer Genre Classification
authors: Ricardo Montalvo-Lezama, Berenice Montalvo-Lezama, Gibran Fuentes-Pineda
conference: SSRN Electronic Journal
year: 2022
bibkey: montalvolezama2022improving
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.07983'}]
tags: []
short_authors: Ricardo Montalvo-Lezama, Berenice Montalvo-Lezama, Gibran Fuentes-Pineda
---
In this paper, we study the transferability of ImageNet spatial and Kinetics
spatio-temporal representations to multi-label Movie Trailer Genre
Classification (MTGC). In particular, we present an extensive evaluation of the
transferability of ConvNet and Transformer models pretrained on ImageNet and
Kinetics to Trailers12k, a new manually-curated movie trailer dataset composed
of 12,000 videos labeled with 10 different genres and associated metadata. We
analyze different aspects that can influence transferability, such as frame
rate, input video extension, and spatio-temporal modeling. In order to reduce
the spatio-temporal structure gap between ImageNet/Kinetics and Trailers12k, we
propose Dual Image and Video Transformer Architecture (DIViTA), which performs
shot detection so as to segment the trailer into highly correlated clips,
providing a more cohesive input for pretrained backbones and improving
transferability (a 1.83% increase for ImageNet and 3.75% for Kinetics). Our
results demonstrate that representations learned on either ImageNet or Kinetics
are comparatively transferable to Trailers12k. Moreover, both datasets provide
complementary information that can be combined to improve classification
performance (a 2.91% gain compared to the top single pretraining).
Interestingly, using lightweight ConvNets as pretrained backbones resulted in
only a 3.46% drop in classification performance compared with the top
Transformer while requiring only 11.82% of its parameters and 0.81% of its
FLOPS.