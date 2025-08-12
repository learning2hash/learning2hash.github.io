---
layout: publication
title: Efficient Full Image Interactive Segmentation By Leveraging Within-image Appearance
  Similarity
authors: Mykhaylo Andriluka, Stefano Pellegrini, Stefan Popov, Vittorio Ferrari
conference: Arxiv
year: 2020
bibkey: andriluka2020efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08173'}]
tags: []
short_authors: Andriluka et al.
---
We propose a new approach to interactive full-image semantic segmentation
which enables quickly collecting training data for new datasets with previously
unseen semantic classes (A demo is available at https://youtu.be/yUk8D5gEX-o).
We leverage a key observation: propagation from labeled to unlabeled pixels
does not necessarily require class-specific knowledge, but can be done purely
based on appearance similarity within an image. We build on this observation
and propose an approach capable of jointly propagating pixel labels from
multiple classes without having explicit class-specific appearance models. To
enable long-range propagation, our approach first globally measures appearance
similarity between labeled and unlabeled pixels across the entire image. Then
it locally integrates per-pixel measurements which improves the accuracy at
boundaries and removes noisy label switches in homogeneous regions. We also
design an efficient manual annotation interface that extends the traditional
polygon drawing tools with a suite of additional convenient features (and add
automatic propagation to it). Experiments with human annotators on the COCO
Panoptic Challenge dataset show that the combination of our better manual
interface and our novel automatic propagation mechanism leads to reducing
annotation time by more than factor of 2x compared to polygon drawing. We also
test our method on the ADE-20k and Fashionista datasets without making any
dataset-specific adaptation nor retraining our model, demonstrating that it can
generalize to new datasets and visual classes.