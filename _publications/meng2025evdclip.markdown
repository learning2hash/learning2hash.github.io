---
layout: publication
title: 'Evdclip: Improving Vision-language Retrieval With Entity Visual Descriptions
  From Large Language Models'
authors: Guanghao Meng, Sunan He, Jinpeng Wang, Tao Dai, Letian Zhang, Jieming Zhu,
  Qing Li, Gang Wang, Rui Zhang, Yong Jiang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: meng2025evdclip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.18594'}]
tags: [Text Retrieval, Evaluation, AAAI, Multimodal Retrieval]
short_authors: Meng et al.
---
Vision-language retrieval (VLR) has attracted significant attention in both academia and industry, which involves using text (or images) as queries to retrieve corresponding images (or text). However, existing methods often neglect the rich visual semantics knowledge of entities, thus leading to incorrect retrieval results. To address this problem, we propose the Entity Visual Description enhanced CLIP (EvdCLIP), designed to leverage the visual knowledge of entities to enrich queries. Specifically, since humans recognize entities through visual cues, we employ a large language model (LLM) to generate Entity Visual Descriptions (EVDs) as alignment cues to complement textual data. These EVDs are then integrated into raw queries to create visually-rich, EVD-enhanced queries. Furthermore, recognizing that EVD-enhanced queries may introduce noise or low-quality expansions, we develop a novel, trainable EVD-aware Rewriter (EaRW) for vision-language retrieval tasks. EaRW utilizes EVD knowledge and the generative capabilities of the language model to effectively rewrite queries. With our specialized training strategy, EaRW can generate high-quality and low-noise EVD-enhanced queries. Extensive quantitative and qualitative experiments on image-text retrieval benchmarks validate the superiority of EvdCLIP on vision-language retrieval tasks.