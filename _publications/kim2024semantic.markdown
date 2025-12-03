---
layout: publication
title: Semantic Token Reweighting For Interpretable And Controllable Text Embeddings
  In CLIP
authors: Eunji Kim, Kyuhong Shim, Simyung Chang, Sungroh Yoon
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2024'
year: 2024
bibkey: kim2024semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.08469'}]
tags: ["EMNLP", "Few Shot & Zero Shot", "Image Retrieval", "Tools & Libraries"]
short_authors: Kim et al.
---
A text encoder within Vision-Language Models (VLMs) like CLIP plays a crucial
role in translating textual input into an embedding space shared with images,
thereby facilitating the interpretative analysis of vision tasks through
natural language. Despite the varying significance of different textual
elements within a sentence depending on the context, efforts to account for
variation of importance in constructing text embeddings have been lacking. We
propose a framework of Semantic Token Reweighting to build Interpretable text
embeddings (SToRI), which incorporates controllability as well. SToRI refines
the text encoding process in CLIP by differentially weighting semantic elements
based on contextual importance, enabling finer control over emphasis responsive
to data-driven insights and user preferences. The efficacy of SToRI is
demonstrated through comprehensive experiments on few-shot image classification
and image retrieval tailored to user preferences.