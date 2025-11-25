---
layout: publication
title: 'Highlighting What Matters: Promptable Embeddings For Attribute-focused Image
  Retrieval'
authors: Siting Li, Xiang Gao, Simon Shaolei Du
conference: Arxiv
year: 2025
bibkey: li2025highlighting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.15877'}]
tags: ["Efficiency", "Evaluation", "Image Retrieval"]
short_authors: Siting Li, Xiang Gao, Simon Shaolei Du
---
While an image is worth more than a thousand words, only a few provide crucial information for a given task and thus should be focused on. In light of this, ideal text-to-image (T2I) retrievers should prioritize specific visual attributes relevant to queries. To evaluate current retrievers on handling attribute-focused queries, we build COCO-Facet, a COCO-based benchmark with 9,112 queries about diverse attributes of interest. We find that CLIP-like retrievers, which are widely adopted due to their efficiency and zero-shot ability, have poor and imbalanced performance, possibly because their image embeddings focus on global semantics and subjects while leaving out other details. Notably, we reveal that even recent Multimodal Large Language Model (MLLM)-based, stronger retrievers with a larger output dimension struggle with this limitation. Hence, we hypothesize that retrieving with general image embeddings is suboptimal for performing such queries. As a solution, we propose to use promptable image embeddings enabled by these multimodal retrievers, which boost performance by highlighting required attributes. Our pipeline for deriving such embeddings generalizes across query types, image pools, and base retriever architectures. To enhance real-world applicability, we offer two acceleration strategies: Pre-processing promptable embeddings and using linear approximations. We show that the former yields a 15% improvement in Recall@5 when prompts are predefined, while the latter achieves an 8% improvement when prompts are only available during inference.