---
layout: publication
title: LLM Meets Vision-language Models For Zero-shot One-class Classification
authors: Yassir Bendou, Giulia Lioi, Bastien Pasdeloup, Lukas Mauch, Ghouthi Boukli
  Hacene, Fabien Cardinaux, Vincent Gripon
conference: Arxiv
year: 2024
bibkey: bendou2024llm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.00675'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Bendou et al.
---
We consider the problem of zero-shot one-class visual classification,
extending traditional one-class classification to scenarios where only the
label of the target class is available. This method aims to discriminate
between positive and negative query samples without requiring examples from the
target class. We propose a two-step solution that first queries large language
models for visually confusing objects and then relies on vision-language
pre-trained models (e.g., CLIP) to perform classification. By adapting
large-scale vision benchmarks, we demonstrate the ability of the proposed
method to outperform adapted off-the-shelf alternatives in this setting.
Namely, we propose a realistic benchmark where negative query samples are drawn
from the same original dataset as positive ones, including a
granularity-controlled version of iNaturalist, where negative samples are at a
fixed distance in the taxonomy tree from the positive ones. To our knowledge,
we are the first to demonstrate the ability to discriminate a single category
from other semantically related ones using only its label.