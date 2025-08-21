---
layout: publication
title: 'SIMCO: Similarity-based Object Counting'
authors: Marco Godi, Christian Joppi, Andrea Giachetti, Marco Cristani
conference: Arxiv
year: 2019
bibkey: godi2019simco
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.07092'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Unsupervised"]
short_authors: Godi et al.
---
We present SIMCO, the first agnostic multi-class object counting approach.
SIMCO starts by detecting foreground objects through a novel Mask RCNN-based
architecture trained beforehand (just once) on a brand-new synthetic 2D shape
dataset, InShape; the idea is to highlight every object resembling a primitive
2D shape (circle, square, rectangle, etc.). Each object detected is described
by a low-dimensional embedding, obtained from a novel similarity-based head
branch; this latter implements a triplet loss, encouraging similar objects
(same 2D shape + color and scale) to map close. Subsequently, SIMCO uses this
embedding for clustering, so that different types of objects can emerge and be
counted, making SIMCO the very first multi-class unsupervised counter.
Experiments show that SIMCO provides state-of-the-art scores on counting
benchmarks and that it can also help in many challenging image understanding
tasks.