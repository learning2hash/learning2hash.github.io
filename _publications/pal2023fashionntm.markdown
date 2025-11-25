---
layout: publication
title: 'Fashionntm: Multi-turn Fashion Image Retrieval Via Cascaded Memory'
authors: Anwesan Pal, Sahil Wadhwa, Ayush Jaiswal, Xu Zhang, Yue Wu, Rakesh Chada,
  Pradeep Natarajan, Henrik I. Christensen
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: pal2023fashionntm
citations: 3
additional_links: [{name: Other, url: 'https://sites.google.com/eng.ucsd.edu/fashionntm'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.10170'}]
tags: ["ICCV", "Image Retrieval"]
short_authors: Pal et al.
---
Multi-turn textual feedback-based fashion image retrieval focuses on a
real-world setting, where users can iteratively provide information to refine
retrieval results until they find an item that fits all their requirements. In
this work, we present a novel memory-based method, called FashionNTM, for such
a multi-turn system. Our framework incorporates a new Cascaded Memory Neural
Turing Machine (CM-NTM) approach for implicit state management, thereby
learning to integrate information across all past turns to retrieve new images,
for a given turn. Unlike vanilla Neural Turing Machine (NTM), our CM-NTM
operates on multiple inputs, which interact with their respective memories via
individual read and write heads, to learn complex relationships. Extensive
evaluation results show that our proposed method outperforms the previous
state-of-the-art algorithm by 50.5%, on Multi-turn FashionIQ -- the only
existing multi-turn fashion dataset currently, in addition to having a relative
improvement of 12.6% on Multi-turn Shoes -- an extension of the single-turn
Shoes dataset that we created in this work. Further analysis of the model in a
real-world interactive setting demonstrates two important capabilities of our
model -- memory retention across turns, and agnosticity to turn order for
non-contradictory feedback. Finally, user study results show that images
retrieved by FashionNTM were favored by 83.1% over other multi-turn models.
Project page: https://sites.google.com/eng.ucsd.edu/fashionntm