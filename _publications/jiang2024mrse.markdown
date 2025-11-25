---
layout: publication
title: 'MRSE: An Efficient Multi-modality Retrieval System For Large Scale E-commerce'
authors: Hao Jiang, Haoxiang Zhang, Qingshan Hou, Chaofeng Chen, Weisi Lin, Jingchang
  Zhang, Annan Wang
conference: Arxiv
year: 2024
bibkey: jiang2024mrse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.14968'}]
tags: ["Multimodal Retrieval", "Robustness", "Scalability"]
short_authors: Jiang et al.
---
Providing high-quality item recall for text queries is crucial in large-scale
e-commerce search systems. Current Embedding-based Retrieval Systems (ERS)
embed queries and items into a shared low-dimensional space, but uni-modality
ERS rely too heavily on textual features, making them unreliable in complex
contexts. While multi-modality ERS incorporate various data sources, they often
overlook individual preferences for different modalities, leading to suboptimal
results. To address these issues, we propose MRSE, a Multi-modality Retrieval
System that integrates text, item images, and user preferences through
lightweight mixture-of-expert (LMoE) modules to better align features across
and within modalities. MRSE also builds user profiles at a multi-modality level
and introduces a novel hybrid loss function that enhances consistency and
robustness using hard negative sampling. Experiments on a large-scale dataset
from Shopee and online A/B testing show that MRSE achieves an 18.9% improvement
in offline relevance and a 3.7% gain in online core metrics compared to
Shopee's state-of-the-art uni-modality system.