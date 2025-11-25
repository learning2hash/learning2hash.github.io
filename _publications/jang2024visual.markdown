---
layout: publication
title: Visual Delta Generator With Large Multi-modal Models For Semi-supervised Composed
  Image Retrieval
authors: Young Kyun Jang, Donghyun Kim, Zihang Meng, Dat Huynh, Ser-Nam Lim
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: jang2024visual
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.15516'}]
tags: ["CVPR", "Few Shot & Zero Shot", "Image Retrieval", "Scalability", "Supervised"]
short_authors: Jang et al.
---
Composed Image Retrieval (CIR) is a task that retrieves images similar to a
query, based on a provided textual modification. Current techniques rely on
supervised learning for CIR models using labeled triplets of the reference
image, text, target image. These specific triplets are not as commonly
available as simple image-text pairs, limiting the widespread use of CIR and
its scalability. On the other hand, zero-shot CIR can be relatively easily
trained with image-caption pairs without considering the image-to-image
relation, but this approach tends to yield lower accuracy. We propose a new
semi-supervised CIR approach where we search for a reference and its related
target images in auxiliary data and learn our large language model-based Visual
Delta Generator (VDG) to generate text describing the visual difference (i.e.,
visual delta) between the two. VDG, equipped with fluent language knowledge and
being model agnostic, can generate pseudo triplets to boost the performance of
CIR models. Our approach significantly improves the existing supervised
learning approaches and achieves state-of-the-art results on the CIR
benchmarks.