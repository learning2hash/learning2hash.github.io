---
layout: publication
title: Top-down Saliency Detection Driven By Visual Classification
authors: Francesca Murabito, Concetto Spampinato, Simone Palazzo, Konstantin Pogorelov,
  Michael Riegler
conference: Computer Vision and Image Understanding
year: 2018
bibkey: murabito2017top
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.05307'}]
tags: []
short_authors: Murabito et al.
---
This paper presents an approach for top-down saliency detection guided by
visual classification tasks. We first learn how to compute visual saliency when
a specific visual task has to be accomplished, as opposed to most
state-of-the-art methods which assess saliency merely through bottom-up
principles. Afterwards, we investigate if and to what extent visual saliency
can support visual classification in nontrivial cases. To achieve this, we
propose SalClassNet, a CNN framework consisting of two networks jointly
trained: a) the first one computing top-down saliency maps from input images,
and b) the second one exploiting the computed saliency maps for visual
classification. To test our approach, we collected a dataset of eye-gaze maps,
using a Tobii T60 eye tracker, by asking several subjects to look at images
from the Stanford Dogs dataset, with the objective of distinguishing dog
breeds. Performance analysis on our dataset and other saliency bench-marking
datasets, such as POET, showed that SalClassNet out-performs state-of-the-art
saliency detectors, such as SalNet and SALICON. Finally, we analyzed the
performance of SalClassNet in a fine-grained recognition task and found out
that it generalizes better than existing visual classifiers. The achieved
results, thus, demonstrate that 1) conditioning saliency detectors with object
classes reaches state-of-the-art performance, and 2) providing explicitly
top-down saliency maps to visual classifiers enhances classification accuracy.