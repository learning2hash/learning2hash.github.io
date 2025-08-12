---
layout: publication
title: Domain-agnostic Tuning-encoder For Fast Personalization Of Text-to-image Models
authors: Moab Arar, Rinon Gal, Yuval Atzmon, Gal Chechik, Daniel Cohen-Or, Ariel Shamir,
  Amit H. Bermano
conference: SIGGRAPH Asia 2023 Conference Papers
year: 2023
bibkey: arar2023domain
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.06925'}]
tags: []
short_authors: Arar et al.
---
Text-to-image (T2I) personalization allows users to guide the creative image
generation process by combining their own visual concepts in natural language
prompts. Recently, encoder-based techniques have emerged as a new effective
approach for T2I personalization, reducing the need for multiple images and
long training times. However, most existing encoders are limited to a
single-class domain, which hinders their ability to handle diverse concepts. In
this work, we propose a domain-agnostic method that does not require any
specialized dataset or prior information about the personalized concepts. We
introduce a novel contrastive-based regularization technique to maintain high
fidelity to the target concept characteristics while keeping the predicted
embeddings close to editable regions of the latent space, by pushing the
predicted tokens toward their nearest existing CLIP tokens. Our experimental
results demonstrate the effectiveness of our approach and show how the learned
tokens are more semantic than tokens predicted by unregularized models. This
leads to a better representation that achieves state-of-the-art performance
while being more flexible than previous methods.