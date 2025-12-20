---
layout: publication
title: 'Omni-attribute: Open-vocabulary Attribute Encoder For Visual Concept Personalization'
authors: Tsai-Shien Chen, Aliaksandr Siarohin, Guocheng Gordon Qian, Kuan-Chieh Jackson
  Wang, Egor Nemchinov, Moayed Haji-Ali, Riza Alp Guler, Willi Menapace, Ivan Skorokhodov,
  Anil Kag, Jun-Yan Zhu, Sergey Tulyakov
conference: Arxiv
year: 2025
bibkey: chen2025omni
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2512.10955'}]
tags: ["Evaluation"]
short_authors: Chen et al.
---
Visual concept personalization aims to transfer only specific image attributes, such as identity, expression, lighting, and style, into unseen contexts. However, existing methods rely on holistic embeddings from general-purpose image encoders, which entangle multiple visual factors and make it difficult to isolate a single attribute. This often leads to information leakage and incoherent synthesis. To address this limitation, we introduce Omni-Attribute, the first open-vocabulary image attribute encoder designed to learn high-fidelity, attribute-specific representations. Our approach jointly designs the data and model: (i) we curate semantically linked image pairs annotated with positive and negative attributes to explicitly teach the encoder what to preserve or suppress; and (ii) we adopt a dual-objective training paradigm that balances generative fidelity with contrastive disentanglement. The resulting embeddings prove effective for open-vocabulary attribute retrieval, personalization, and compositional generation, achieving state-of-the-art performance across multiple benchmarks.