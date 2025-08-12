---
layout: publication
title: Text-based Person Search Without Parallel Image-text Data
authors: Yang Bai, Jingyao Wang, Min Cao, Chen Chen, Ziqiang Cao, Liqiang Nie, Min
  Zhang
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: bai2023text
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.12964'}]
tags: []
short_authors: Bai et al.
---
Text-based person search (TBPS) aims to retrieve the images of the target
person from a large image gallery based on a given natural language
description. Existing methods are dominated by training models with parallel
image-text pairs, which are very costly to collect. In this paper, we make the
first attempt to explore TBPS without parallel image-text data (\(\mu\)-TBPS), in
which only non-parallel images and texts, or even image-only data, can be
adopted. Towards this end, we propose a two-stage framework,
generation-then-retrieval (GTR), to first generate the corresponding pseudo
text for each image and then perform the retrieval in a supervised manner. In
the generation stage, we propose a fine-grained image captioning strategy to
obtain an enriched description of the person image, which firstly utilizes a
set of instruction prompts to activate the off-the-shelf pretrained
vision-language model to capture and generate fine-grained person attributes,
and then converts the extracted attributes into a textual description via the
finetuned large language model or the hand-crafted template. In the retrieval
stage, considering the noise interference of the generated texts for training
model, we develop a confidence score-based training scheme by enabling more
reliable texts to contribute more during the training. Experimental results on
multiple TBPS benchmarks (i.e., CUHK-PEDES, ICFG-PEDES and RSTPReid) show that
the proposed GTR can achieve a promising performance without relying on
parallel image-text data.