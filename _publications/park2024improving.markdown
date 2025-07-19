---
layout: publication
title: Improving Text-based Person Search via Part-level Cross-modal Correspondence
authors: Park et al.
conference: Pattern Recognition
year: 2024
bibkey: park2024improving
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.00318'}]
tags: [CVPR]
---
Text-based person search is the task of finding person images that are the
most relevant to the natural language text description given as query. The main
challenge of this task is a large gap between the target images and text
queries, which makes it difficult to establish correspondence and distinguish
subtle differences across people. To address this challenge, we introduce an
efficient encoder-decoder model that extracts coarse-to-fine embedding vectors
which are semantically aligned across the two modalities without supervision
for the alignment. There is another challenge of learning to capture
fine-grained information with only person IDs as supervision, where similar
body parts of different individuals are considered different due to the lack of
part-level supervision. To tackle this, we propose a novel ranking loss, dubbed
commonality-based margin ranking loss, which quantifies the degree of
commonality of each body part and reflects it during the learning of
fine-grained body part details. As a consequence, it enables our method to
achieve the best records on three public benchmarks.