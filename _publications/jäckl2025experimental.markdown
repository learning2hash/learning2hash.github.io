---
layout: publication
title: Experimental Evaluation Of Static Image Sub-region-based Search Models Using
  CLIP
authors: "Bastian J\xE4ckl, Vojt\u011Bch Kloda, Daniel A. Keim, Jakub Loko\u010D"
conference: Lecture Notes in Computer Science
year: 2025
bibkey: "j\xE4ckl2025experimental"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.06938'}]
tags: [Evaluation, Datasets]
short_authors: "J\xE4ckl et al."
---
Advances in multimodal text-image models have enabled effective text-based querying in extensive image collections. While these models show convincing performance for everyday life scenes, querying in highly homogeneous, specialized domains remains challenging. The primary problem is that users can often provide only vague textual descriptions as they lack expert knowledge to discriminate between homogenous entities. This work investigates whether adding location-based prompts to complement these vague text queries can enhance retrieval performance. Specifically, we collected a dataset of 741 human annotations, each containing short and long textual descriptions and bounding boxes indicating regions of interest in challenging underwater scenes. Using these annotations, we evaluate the performance of CLIP when queried on various static sub-regions of images compared to the full image. Our results show that both a simple 3-by-3 partitioning and a 5-grid overlap significantly improve retrieval effectiveness and remain robust to perturbations of the annotation box.