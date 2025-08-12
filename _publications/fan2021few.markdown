---
layout: publication
title: Few-shot Video Object Detection
authors: Qi Fan, Chi-keung Tang, Yu-wing Tai
conference: Lecture Notes in Computer Science
year: 2022
bibkey: fan2021few
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14805'}]
tags: []
short_authors: Qi Fan, Chi-keung Tang, Yu-wing Tai
---
We introduce Few-Shot Video Object Detection (FSVOD) with three contributions
to real-world visual learning challenge in our highly diverse and dynamic
world: 1) a large-scale video dataset FSVOD-500 comprising of 500 classes with
class-balanced videos in each category for few-shot learning; 2) a novel Tube
Proposal Network (TPN) to generate high-quality video tube proposals for
aggregating feature representation for the target video object which can be
highly dynamic; 3) a strategically improved Temporal Matching Network (TMN+)
for matching representative query tube features with better discriminative
ability thus achieving higher diversity. Our TPN and TMN+ are jointly and
end-to-end trained. Extensive experiments demonstrate that our method produces
significantly better detection results on two few-shot video object detection
datasets compared to image-based methods and other naive video-based
extensions. Codes and datasets are released at
https://github.com/fanq15/FewX.