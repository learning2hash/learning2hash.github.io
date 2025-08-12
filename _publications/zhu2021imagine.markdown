---
layout: publication
title: 'Imagine: An Imagination-based Automatic Evaluation Metric For Natural Language
  Generation'
authors: Wanrong Zhu, Xin Eric Wang, An Yan, Miguel Eckstein, William Yang Wang
conference: 'Findings of the Association for Computational Linguistics: EACL 2023'
year: 2023
bibkey: zhu2021imagine
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.05970'}]
tags: ["Evaluation"]
short_authors: Zhu et al.
---
Automatic evaluations for natural language generation (NLG) conventionally
rely on token-level or embedding-level comparisons with text references. This
differs from human language processing, for which visual imagination often
improves comprehension. In this work, we propose ImaginE, an imagination-based
automatic evaluation metric for natural language generation. With the help of
StableDiffusion, a state-of-the-art text-to-image generator, we automatically
generate an image as the embodied imagination for the text snippet and compute
the imagination similarity using contextual embeddings. Experiments spanning
several text generation tasks demonstrate that adding machine-generated images
with our ImaginE displays great potential in introducing multi-modal
information into NLG evaluation, and improves existing automatic metrics'
correlations with human similarity judgments in both reference-based and
reference-free evaluation scenarios.