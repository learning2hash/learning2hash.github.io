---
layout: publication
title: Hyper-local Deformable Transformers For Text Spotting On Historical Maps
authors: Yijun Lin, Yao-Yi Chiang
conference: Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2024
bibkey: lin2024hyper
citations: 2
additional_links: [{name: Code, url: 'https://github.com/kartta-foundation/mapkurator-palette-doc'},
  {name: Paper, url: 'https://arxiv.org/abs/2506.15010'}]
tags: ["KDD"]
short_authors: Yijun Lin, Yao-Yi Chiang
---
Text on historical maps contains valuable information providing georeferenced historical, political, and cultural contexts. However, text extraction from historical maps is challenging due to the lack of (1) effective methods and (2) training data. Previous approaches use ad-hoc steps tailored to only specific map styles. Recent machine learning-based text spotters (e.g., for scene images) have the potential to solve these challenges because of their flexibility in supporting various types of text instances. However, these methods remain challenges in extracting precise image features for predicting every sub-component (boundary points and characters) in a text instance. This is critical because map text can be lengthy and highly rotated with complex backgrounds, posing difficulties in detecting relevant image features from a rough text region. This paper proposes PALETTE, an end-to-end text spotter for scanned historical maps of a wide variety. PALETTE introduces a novel hyper-local sampling module to explicitly learn localized image features around the target boundary points and characters of a text instance for detection and recognition. PALETTE also enables hyper-local positional embeddings to learn spatial interactions between boundary points and characters within and across text instances. In addition, this paper presents a novel approach to automatically generate synthetic map images, SynthMap+, for training text spotters for historical maps. The experiment shows that PALETTE with SynthMap+ outperforms SOTA text spotters on two new benchmark datasets of historical maps, particularly for long and angled text. We have deployed PALETTE with SynthMap+ to process over 60,000 maps in the David Rumsey Historical Map collection and generated over 100 million text labels to support map searching. The project is released at https://github.com/kartta-foundation/mapkurator-palette-doc.