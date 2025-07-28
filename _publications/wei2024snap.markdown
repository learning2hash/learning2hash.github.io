---
layout: publication
title: 'Snap And Diagnose: An Advanced Multimodal Retrieval System For Identifying
  Plant Diseases In The Wild'
authors: Tianqi Wei, Zhi Chen, Xin Yu
conference: Arxiv
year: 2024
bibkey: wei2024snap
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.14723'}]
tags: ["Multimodal Retrieval"]
short_authors: Tianqi Wei, Zhi Chen, Xin Yu
---
Plant disease recognition is a critical task that ensures crop health and
mitigates the damage caused by diseases. A handy tool that enables farmers to
receive a diagnosis based on query pictures or the text description of
suspicious plants is in high demand for initiating treatment before potential
diseases spread further. In this paper, we develop a multimodal plant disease
image retrieval system to support disease search based on either image or text
prompts. Specifically, we utilize the largest in-the-wild plant disease dataset
PlantWild, which includes over 18,000 images across 89 categories, to provide a
comprehensive view of potential diseases relating to the query. Furthermore,
cross-modal retrieval is achieved in the developed system, facilitated by a
novel CLIP-based vision-language model that encodes both disease descriptions
and disease images into the same latent space. Built on top of the retriever,
our retrieval system allows users to upload either plant disease images or
disease descriptions to retrieve the corresponding images with similar
characteristics from the disease dataset to suggest candidate diseases for end
users' consideration.