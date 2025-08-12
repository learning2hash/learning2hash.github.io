---
layout: publication
title: Unsupervised Scene Sketch To Photo Synthesis
authors: Jiayun Wang, Sangryul Jeon, Stella X. Yu, Xi Zhang, Himanshu Arora, Yu Lou
conference: Lecture Notes in Computer Science
year: 2023
bibkey: wang2022unsupervised
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.02834'}]
tags: ["Unsupervised"]
short_authors: Wang et al.
---
Sketches make an intuitive and powerful visual expression as they are fast
executed freehand drawings. We present a method for synthesizing realistic
photos from scene sketches. Without the need for sketch and photo pairs, our
framework directly learns from readily available large-scale photo datasets in
an unsupervised manner. To this end, we introduce a standardization module that
provides pseudo sketch-photo pairs during training by converting photos and
sketches to a standardized domain, i.e. the edge map. The reduced domain gap
between sketch and photo also allows us to disentangle them into two
components: holistic scene structures and low-level visual styles such as color
and texture. Taking this advantage, we synthesize a photo-realistic image by
combining the structure of a sketch and the visual style of a reference photo.
Extensive experimental results on perceptual similarity metrics and human
perceptual studies show the proposed method could generate realistic photos
with high fidelity from scene sketches and outperform state-of-the-art photo
synthesis baselines. We also demonstrate that our framework facilitates a
controllable manipulation of photo synthesis by editing strokes of
corresponding sketches, delivering more fine-grained details than previous
approaches that rely on region-level editing.