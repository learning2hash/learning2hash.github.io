---
layout: publication
title: Designovel's System Description For Fashion-iq Challenge 2019
authors: Jianri Li, Jae-Whan Lee, Woo-Sang Song, Ki-Young Shin, Byung-Hyun Go
conference: Arxiv
year: 2019
bibkey: li2019designovel
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.11119'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation, Datasets]
short_authors: Li et al.
---
This paper describes Designovel's systems which are submitted to the Fashion
IQ Challenge 2019. Goal of the challenge is building an image retrieval system
where input query is a candidate image plus two text phrases describe user's
feedback about visual differences between the candidate image and the search
target. We built the systems by combining methods from recent work on deep
metric learning, multi-modal retrieval and natual language processing. First,
we encode both candidate and target images with CNNs into high-level
representations, and encode text descriptions to a single text vector using
Transformer-based encoder. Then we compose candidate image vector and text
representation into a single vector which is exptected to be biased toward
target image vector. Finally, we compute cosine similarities between composed
vector and encoded vectors of whole dataset, and rank them in desceding order
to get ranked list. We experimented with Fashion IQ 2019 dataset in various
settings of hyperparameters, achieved 39.12% average recall by a single model
and 43.67% average recall by an ensemble of 16 models on test dataset.