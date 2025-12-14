---
layout: publication
title: 'Language-enhanced Rnr-map: Querying Renderable Neural Radiance Field Maps
  With Natural Language'
authors: Francesco Taioli, Federico Cunico, Federico Girella, Riccardo Bologna, Alessandro
  Farinelli, Marco Cristani
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: taioli2023language
citations: 5
additional_links: [{name: Code, url: 'https://intelligolabs.github.io/Le-RNR-Map/'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.08854'}]
tags: [Evaluation, ICCV]
short_authors: Taioli et al.
---
We present Le-RNR-Map, a Language-enhanced Renderable Neural Radiance map for
Visual Navigation with natural language query prompts. The recently proposed
RNR-Map employs a grid structure comprising latent codes positioned at each
pixel. These latent codes, which are derived from image observation, enable: i)
image rendering given a camera pose, since they are converted to Neural
Radiance Field; ii) image navigation and localization with astonishing
accuracy. On top of this, we enhance RNR-Map with CLIP-based embedding latent
codes, allowing natural language search without additional label data. We
evaluate the effectiveness of this map in single and multi-object searches. We
also investigate its compatibility with a Large Language Model as an
"affordance query resolver". Code and videos are available at
https://intelligolabs.github.io/Le-RNR-Map/