---
layout: publication
title: Learning Deep Sketch Abstraction
authors: Umar Riaz Muhammad, Yongxin Yang, Yi-Zhe Song, Tao Xiang, Timothy M. Hospedales
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: muhammad2018learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04804'}]
tags: ["CVPR", "Image Retrieval"]
short_authors: Muhammad et al.
---
Human free-hand sketches have been studied in various contexts including
sketch recognition, synthesis and fine-grained sketch-based image retrieval
(FG-SBIR). A fundamental challenge for sketch analysis is to deal with
drastically different human drawing styles, particularly in terms of
abstraction level. In this work, we propose the first stroke-level sketch
abstraction model based on the insight of sketch abstraction as a process of
trading off between the recognizability of a sketch and the number of strokes
used to draw it. Concretely, we train a model for abstract sketch generation
through reinforcement learning of a stroke removal policy that learns to
predict which strokes can be safely removed without affecting recognizability.
We show that our abstraction model can be used for various sketch analysis
tasks including: (1) modeling stroke saliency and understanding the decision of
sketch recognition models, (2) synthesizing sketches of variable abstraction
for a given category, or reference object instance in a photo, and (3) training
a FG-SBIR model with photos only, bypassing the expensive photo-sketch pair
collection step.