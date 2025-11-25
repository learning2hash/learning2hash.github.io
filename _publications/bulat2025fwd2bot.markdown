---
layout: publication
title: 'Fwd2bot: LVLM Visual Token Compression With Double Forward Bottleneck'
authors: Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
conference: Arxiv
year: 2025
bibkey: bulat2025fwd2bot
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.21757'}]
tags: ["Compact Codes", "Image Retrieval"]
short_authors: Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
---
In this work, we aim to compress the vision tokens of a Large Vision Language
Model (LVLM) into a representation that is simultaneously suitable for (a)
generative and (b) discriminative tasks, (c) is nearly lossless, and (d) is
storage-efficient. We propose a novel compression approach, called Fwd2Bot,
that uses the LVLM itself to compress the visual information in a task-agnostic
manner. At the core of Fwd2bot there exists a "double-forward pass" training
strategy, whereby, during the first forward pass, the LLM (of the LVLM) creates
a bottleneck by condensing the visual information into a small number of
summary tokens. Then, using the same LLM, the second forward pass processes the
language instruction(s) alongside the summary tokens, used as a direct
replacement for the image ones. The training signal is provided by two losses:
an autoregressive one applied after the second pass that provides a direct
optimization objective for compression, and a contrastive loss, applied after
the first pass, that further boosts the representation strength, especially for
discriminative tasks. The training is further enhanced by stage-specific
adapters. We accompany the proposed method by an in-depth ablation study.
Overall, Fwd2Bot results in highly-informative compressed representations
suitable for both generative and discriminative tasks. For generative tasks, we
offer a 2x higher compression rate without compromising the generative
capabilities, setting a new state-of-the-art result. For discriminative tasks,
we set a new state-of-the-art on image retrieval and compositionality.