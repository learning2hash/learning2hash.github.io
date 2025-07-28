---
layout: publication
title: Improving Hateful Meme Detection Through Retrieval-guided Contrastive Learning
authors: Jingbiao Mei, Jinghong Chen, Weizhe Lin, Bill Byrne, Marcus Tomalin
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: mei2023improving
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.08110'}]
tags: []
short_authors: Mei et al.
---
Hateful memes have emerged as a significant concern on the Internet.
Detecting hateful memes requires the system to jointly understand the visual
and textual modalities. Our investigation reveals that the embedding space of
existing CLIP-based systems lacks sensitivity to subtle differences in memes
that are vital for correct hatefulness classification. We propose constructing
a hatefulness-aware embedding space through retrieval-guided contrastive
training. Our approach achieves state-of-the-art performance on the
HatefulMemes dataset with an AUROC of 87.0, outperforming much larger
fine-tuned large multimodal models. We demonstrate a retrieval-based hateful
memes detection system, which is capable of identifying hatefulness based on
data unseen in training. This allows developers to update the hateful memes
detection system by simply adding new examples without retraining, a desirable
feature for real services in the constantly evolving landscape of hateful memes
on the Internet.