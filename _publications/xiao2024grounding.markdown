---
layout: publication
title: Grounding Language Models For Visual Entity Recognition
authors: Zilin Xiao, Ming Gong, Paola Cascante-Bonilla, Xingyao Zhang, Jie Wu, Vicente
  Ordonez
conference: Lecture Notes in Computer Science
year: 2024
bibkey: xiao2024grounding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.18695'}]
tags: ["Datasets", "Evaluation"]
short_authors: Xiao et al.
---
We introduce AutoVER, an Autoregressive model for Visual Entity Recognition.
Our model extends an autoregressive Multi-modal Large Language Model by
employing retrieval augmented constrained generation. It mitigates low
performance on out-of-domain entities while excelling in queries that require
visually-situated reasoning. Our method learns to distinguish similar entities
within a vast label space by contrastively training on hard negative pairs in
parallel with a sequence-to-sequence objective without an external retriever.
During inference, a list of retrieved candidate answers explicitly guides
language generation by removing invalid decoding paths. The proposed method
achieves significant improvements across different dataset splits in the
recently proposed Oven-Wiki benchmark. Accuracy on the Entity seen split rises
from 32.7% to 61.5%. It also demonstrates superior performance on the unseen
and query splits by a substantial double-digit margin.