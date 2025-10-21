---
layout: publication
title: Efficient Discriminative Joint Encoders For Large Scale Vision-language Reranking
authors: Mitchell Keren Taraday, Shahaf Wagner, Chaim Baskin
conference: Arxiv
year: 2025
bibkey: taraday2025efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2510.06820'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Mitchell Keren Taraday, Shahaf Wagner, Chaim Baskin
---
Multimodal retrieval still leans on embedding-based models like CLIP for fast vector search over pre-computed image embeddings. Yet, unlike text retrieval, where joint-encoder rerankers are standard, comparable vision--language rerankers are largely absent. We find that seminal joint encoders such as BLIP are severely bottlenecked by an expensive visual feature-extraction stage, preventing practical deployment at scale. Motivated by this bottleneck, we introduce EDJE, an Efficient Discriminative Joint Encoder that precomputes vision tokens offline and compresses them via a lightweight attention-based adapter, so online inference runs only a compact joint encoder over a small set of visual tokens plus the text. EDJE preserves strong retrieval performance while drastically reducing storage and online compute, enabling high-throughput inference. Specifically, EDJE processes 50k image--text pairs/second while requiring 49kB of disk storage per image, matching prior art on Flickr (zero-shot) and COCO (fine-tuned) retrieval. The implementation and checkpoints will be made publicly available shortly.