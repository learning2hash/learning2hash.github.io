---
layout: publication
title: 'Shapey: Measuring Shape Recognition Capacity Using Nearest Neighbor Matching'
authors: Jong Woo Nam, Amanda S. Rios, Bartlett W. Mel
conference: Arxiv
year: 2021
bibkey: nam2021shapey
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.08174'}]
tags: ["Evaluation"]
short_authors: Jong Woo Nam, Amanda S. Rios, Bartlett W. Mel
---
Object recognition in humans depends primarily on shape cues. We have
developed a new approach to measuring the shape recognition performance of a
vision system based on nearest neighbor view matching within the system's
embedding space. Our performance benchmark, ShapeY, allows for precise control
of task difficulty, by enforcing that view matching span a specified degree of
3D viewpoint change and/or appearance change. As a first test case we measured
the performance of ResNet50 pre-trained on ImageNet. Matching error rates were
high. For example, a 27 degree change in object pitch led ResNet50 to match the
incorrect object 45% of the time. Appearance changes were also highly
disruptive. Examination of false matches indicates that ResNet50's embedding
space is severely "tangled". These findings suggest ShapeY can be a useful tool
for charting the progress of artificial vision systems towards human-level
shape recognition capabilities.