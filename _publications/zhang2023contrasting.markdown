---
layout: publication
title: Contrasting Intra-modal And Ranking Cross-modal Hard Negatives To Enhance Visio-linguistic
  Compositional Understanding
authors: Le Zhang, Rabiul Awal, Aishwarya Agrawal
conference: Arxiv
year: 2023
bibkey: zhang2023contrasting
citations: 0
additional_links: [{name: Code, url: 'https://github.com/lezhang7/Enhance-FineGrained'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.08832'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Tools & Libraries"]
short_authors: Le Zhang, Rabiul Awal, Aishwarya Agrawal
---
Vision-Language Models (VLMs), such as CLIP, exhibit strong image-text
comprehension abilities, facilitating advances in several downstream tasks such
as zero-shot image classification, image-text retrieval, and text-to-image
generation. However, the compositional reasoning abilities of existing VLMs
remains subpar. The root of this limitation lies in the inadequate alignment
between the images and captions in the pretraining datasets. Additionally, the
current contrastive learning objective fails to focus on fine-grained grounding
components like relations, actions, and attributes, resulting in "bag-of-words"
representations. We introduce a simple and effective method to improve
compositional reasoning in VLMs. Our method better leverages available datasets
by refining and expanding the standard image-text contrastive learning
framework. Our approach does not require specific annotations and does not
incur extra parameters. When integrated with CLIP, our technique yields notable
improvement over state-of-the-art baselines across five vision-language
compositional benchmarks. We open-source our code at
https://github.com/lezhang7/Enhance-FineGrained.