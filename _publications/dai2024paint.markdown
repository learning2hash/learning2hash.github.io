---
layout: publication
title: Paint Bucket Colorization Using Anime Character Color Design Sheets
authors: Yuekun Dai, Qinyue Li, Shangchen Zhou, Yihang Luo, Chongyi Li, Chen Change
  Loy
conference: Arxiv
year: 2024
bibkey: dai2024paint
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.19424'}]
tags: []
short_authors: Dai et al.
---
Line art colorization plays a crucial role in hand-drawn animation
production, where digital artists manually colorize segments using a paint
bucket tool, guided by RGB values from character color design sheets. This
process, often called paint bucket colorization, involves two main tasks:
keyframe colorization, where colors are applied according to the character's
color design sheet, and consecutive frame colorization, where these colors are
replicated across adjacent frames. Current automated colorization methods
primarily focus on reference-based and segment-matching approaches. However,
reference-based methods often fail to accurately assign specific colors to each
region, while matching-based methods are limited to consecutive frame
colorization and struggle with issues like significant deformation and
occlusion. In this work, we introduce inclusion matching, which allows the
network to understand the inclusion relationships between segments, rather than
relying solely on direct visual correspondences. By integrating this approach
with segment parsing and color warping modules, our inclusion matching pipeline
significantly improves performance in both keyframe colorization and
consecutive frame colorization. To support our network's training, we have
developed a unique dataset named PaintBucket-Character, which includes rendered
line arts alongside their colorized versions and shading annotations for
various 3D characters. To replicate industry animation data formats, we also
created color design sheets for each character, with semantic information for
each color and standard pose reference images. Experiments highlight the
superiority of our method, demonstrating accurate and consistent colorization
across both our proposed benchmarks and hand-drawn animations.