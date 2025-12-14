---
layout: publication
title: Understanding The Effect Of Using Semantically Meaningful Tokens For Visual
  Representation Learning
authors: Neha Kalibhat, Priyatham Kattakinda, Sumit Nawathe, Arman Zarei, Nikita Seleznev,
  Samuel Sharpe, Senthil Kumar, Soheil Feizi
conference: Arxiv
year: 2024
bibkey: kalibhat2024understanding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.16401'}]
tags: [Text Retrieval, Evaluation, Tools & Libraries, Multimodal Retrieval]
short_authors: Kalibhat et al.
---
Vision transformers have established a precedent of patchifying images into uniformly-sized chunks before processing. We hypothesize that this design choice may limit models in learning comprehensive and compositional representations from visual data. This paper explores the notion of providing semantically-meaningful visual tokens to transformer encoders within a vision-language pre-training framework. Leveraging off-the-shelf segmentation and scene-graph models, we extract representations of instance segmentation masks (referred to as tangible tokens) and relationships and actions (referred to as intangible tokens). Subsequently, we pre-train a vision-side transformer by incorporating these newly extracted tokens and aligning the resultant embeddings with caption embeddings from a text-side encoder. To capture the structural and semantic relationships among visual tokens, we introduce additive attention weights, which are used to compute self-attention scores. Our experiments on COCO demonstrate notable improvements over ViTs in learned representation quality across text-to-image (+47%) and image-to-text retrieval (+44%) tasks. Furthermore, we showcase the advantages on compositionality benchmarks such as ARO (+18%) and Winoground (+10%).