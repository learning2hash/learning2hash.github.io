---
layout: publication
title: 'Match Cutting: Finding Cuts With Smooth Visual Transitions'
authors: Boris Chen, Amir Ziai, Rebecca Tucker, Yuchen Xie
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: chen2022match
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.05766'}]
tags: []
short_authors: Chen et al.
---
A match cut is a transition between a pair of shots that uses similar
framing, composition, or action to fluidly bring the viewer from one scene to
the next. Match cuts are frequently used in film, television, and advertising.
However, finding shots that work together is a highly manual and time-consuming
process that can take days. We propose a modular and flexible system to
efficiently find high-quality match cut candidates starting from millions of
shot pairs. We annotate and release a dataset of approximately 20k labeled
pairs that we use to evaluate our system, using both classification and metric
learning approaches that leverage a variety of image, video, audio, and
audio-visual feature extractors. In addition, we release code and embeddings
for reproducing our experiments at github.com/netflix/matchcut.