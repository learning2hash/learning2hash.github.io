---
layout: publication
title: 'Few-shot VQA With Frozen Llms: A Tale Of Two Approaches'
authors: Igor Sterner, Weizhe Lin, Jinghong Chen, Bill Byrne
conference: Arxiv
year: 2024
bibkey: sterner2024few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.11317'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Sterner et al.
---
Two approaches have emerged to input images into large language models
(LLMs). The first is to caption images into natural language. The second is to
map image feature embeddings into the domain of the LLM and pass the mapped
embeddings directly to the LLM. The majority of recent few-shot multimodal work
reports performance using architectures that employ variations of one of these
two approaches. But they overlook an important comparison between them. We
design a controlled and focused experiment to compare these two approaches to
few-shot visual question answering (VQA) with LLMs. Our findings indicate that
for Flan-T5 XL, a 3B parameter LLM, connecting visual embeddings directly to
the LLM embedding space does not guarantee improved performance over using
image captions. In the zero-shot regime, we find using textual image captions
is better. In the few-shot regimes, how the in-context examples are selected
determines which is better.