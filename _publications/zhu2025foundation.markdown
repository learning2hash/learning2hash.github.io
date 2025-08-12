---
layout: publication
title: Foundation Model-based Apple Ripeness And Size Estimation For Selective Harvesting
authors: Keyi Zhu, Jiajia Li, Kaixiang Zhang, Chaaran Arunachalam, Siddhartha Bhattacharya,
  Renfu Lu, Zhaojian Li
conference: Arxiv
year: 2025
bibkey: zhu2025foundation
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.01850'}]
tags: ["Tools & Libraries"]
short_authors: Zhu et al.
---
Harvesting is a critical task in the tree fruit industry, demanding extensive manual labor and substantial costs, and exposing workers to potential hazards. Recent advances in automated harvesting offer a promising solution by enabling efficient, cost-effective, and ergonomic fruit picking within tight harvesting windows. However, existing harvesting technologies often indiscriminately harvest all visible and accessible fruits, including those that are unripe or undersized. This study introduces a novel foundation model-based framework for efficient apple ripeness and size estimation. Specifically, we curated two public RGBD-based Fuji apple image datasets, integrating expanded annotations for ripeness ("Ripe" vs. "Unripe") based on fruit color and image capture dates. The resulting comprehensive dataset, Fuji-Ripeness-Size Dataset, includes 4,027 images and 16,257 annotated apples with ripeness and size labels. Using Grounding-DINO, a language-model-based object detector, we achieved robust apple detection and ripeness classification, outperforming other state-of-the-art models. Additionally, we developed and evaluated six size estimation algorithms, selecting the one with the lowest error and variation for optimal performance. The Fuji-Ripeness-Size Dataset and the apple detection and size estimation algorithms are made publicly available, which provides valuable benchmarks for future studies in automated and selective harvesting.