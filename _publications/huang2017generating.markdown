---
layout: publication
title: Generating Music Medleys Via Playing Music Puzzle Games
authors: Yu-siang Huang, Szu-yu Chou, Yi-hsuan Yang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2018
bibkey: huang2017generating
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.04384'}]
tags: ["AAAI"]
short_authors: Yu-siang Huang, Szu-yu Chou, Yi-hsuan Yang
---
Generating music medleys is about finding an optimal permutation of a given
set of music clips. Toward this goal, we propose a self-supervised learning
task, called the music puzzle game, to train neural network models to learn the
sequential patterns in music. In essence, such a game requires machines to
correctly sort a few multisecond music fragments. In the training stage, we
learn the model by sampling multiple non-overlapping fragment pairs from the
same songs and seeking to predict whether a given pair is consecutive and is in
the correct chronological order. For testing, we design a number of puzzle
games with different difficulty levels, the most difficult one being music
medley, which requiring sorting fragments from different songs. On the basis of
state-of-the-art Siamese convolutional network, we propose an improved
architecture that learns to embed frame-level similarity scores computed from
the input fragment pairs to a common space, where fragment pairs in the correct
order can be more easily identified. Our result shows that the resulting model,
dubbed as the similarity embedding network (SEN), performs better than
competing models across different games, including music jigsaw puzzle, music
sequencing, and music medley. Example results can be found at our project
website, https://remyhuang.github.io/DJnet.