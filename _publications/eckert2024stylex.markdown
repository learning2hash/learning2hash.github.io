---
layout: publication
title: 'Stylex: A Trainable Metric For X-ray Style Distances'
authors: "Dominik Eckert, Christopher Syben, Christian H\xFCmmer, Ludwig Ritschl,\
  \ Steffen Kappler, Sebastian Stober"
conference: Arxiv
year: 2024
bibkey: eckert2024stylex
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.14718'}]
tags: ["Distance Metric Learning"]
short_authors: Eckert et al.
---
The progression of X-ray technology introduces diverse image styles that need
to be adapted to the preferences of radiologists. To support this task, we
introduce a novel deep learning-based metric that quantifies style differences
of non-matching image pairs. At the heart of our metric is an encoder capable
of generating X-ray image style representations. This encoder is trained
without any explicit knowledge of style distances by exploiting Simple Siamese
learning. During inference, the style representations produced by the encoder
are used to calculate a distance metric for non-matching image pairs. Our
experiments investigate the proposed concept for a disclosed reproducible and a
proprietary image processing pipeline along two dimensions: First, we use a
t-distributed stochastic neighbor embedding (t-SNE) analysis to illustrate that
the encoder outputs provide meaningful and discriminative style
representations. Second, the proposed metric calculated from the encoder
outputs is shown to quantify style distances for non-matching pairs in good
alignment with the human perception. These results confirm that our proposed
method is a promising technique to quantify style differences, which can be
used for guided style selection as well as automatic optimization of image
pipeline parameters.