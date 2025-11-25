---
layout: publication
title: 'PDV: Prompt Directional Vectors For Zero-shot Composed Image Retrieval'
authors: Osman Tursun, Sinan Kalkan, Simon Denman, Clinton Fookes
conference: Arxiv
year: 2025
bibkey: tursun2025pdv
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.07215'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Tursun et al.
---
Zero-shot composed image retrieval (ZS-CIR) enables image search using a
reference image and text prompt without requiring specialized text-image
composition networks trained on large-scale paired data. However, current
ZS-CIR approaches face three critical limitations in their reliance on composed
text embeddings: static query embedding representations, insufficient
utilization of image embeddings, and suboptimal performance when fusing text
and image embeddings. To address these challenges, we introduce the Prompt
Directional Vector (PDV), a simple yet effective training-free enhancement that
captures semantic modifications induced by user prompts. PDV enables three key
improvements: (1) dynamic composed text embeddings where prompt adjustments are
controllable via a scaling factor, (2) composed image embeddings through
semantic transfer from text prompts to image features, and (3) weighted fusion
of composed text and image embeddings that enhances retrieval by balancing
visual and semantic similarity. Our approach serves as a plug-and-play
enhancement for existing ZS-CIR methods with minimal computational overhead.
Extensive experiments across multiple benchmarks demonstrate that PDV
consistently improves retrieval performance when integrated with
state-of-the-art ZS-CIR approaches, particularly for methods that generate
accurate compositional embeddings. The code will be publicly available.