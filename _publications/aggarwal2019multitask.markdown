---
layout: publication
title: Multitask Text-to-Visual Embedding with Titles and Clickthrough Data
authors: Aggarwal et al.
conference: Proceedings of the 25th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2019
bibkey: aggarwal2019multitask
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.13339'}]
tags: ["KDD"]
---
Text-visual (or called semantic-visual) embedding is a central problem in
vision-language research. It typically involves mapping of an image and a text
description to a common feature space through a CNN image encoder and a RNN
language encoder. In this paper, we propose a new method for learning
text-visual embedding using both image titles and click-through data from an
image search engine. We also propose a new triplet loss function by modeling
positive awareness of the embedding, and introduce a novel mini-batch-based
hard negative sampling approach for better data efficiency in the learning
process. Experimental results show that our proposed method outperforms
existing methods, and is also effective for real-world text-to-visual
retrieval.