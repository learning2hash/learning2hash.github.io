---
layout: publication
title: 'Mini-splatting: Representing Scenes With A Constrained Number Of Gaussians'
authors: Guangchi Fang, Bing Wang
conference: Lecture Notes in Computer Science
year: 2024
bibkey: fang2024mini
citations: 6
additional_links: [{name: Code, url: 'https://github.com/fatPeter/mini-splatting\}\{Code'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.14166'}]
tags: []
short_authors: Guangchi Fang, Bing Wang
---
In this study, we explore the challenge of efficiently representing scenes
with a constrained number of Gaussians. Our analysis shifts from traditional
graphics and 2D computer vision to the perspective of point clouds,
highlighting the inefficient spatial distribution of Gaussian representation as
a key limitation in model performance. To address this, we introduce strategies
for densification including blur split and depth reinitialization, and
simplification through intersection preserving and sampling. These techniques
reorganize the spatial positions of the Gaussians, resulting in significant
improvements across various datasets and benchmarks in terms of rendering
quality, resource consumption, and storage compression. Our Mini-Splatting
integrates seamlessly with the original rasterization pipeline, providing a
strong baseline for future research in Gaussian-Splatting-based works.
\href\{https://github.com/fatPeter/mini-splatting\}\{Code is available\}.