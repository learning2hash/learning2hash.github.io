---
layout: publication
title: Context-aware Zero-shot Recognition
authors: Ruotian Luo, Ning Zhang, Bohyung Han, Linjie Yang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: luo2019context
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.09320'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Luo et al.
---
We present a novel problem setting in zero-shot learning, zero-shot object
recognition and detection in the context. Contrary to the traditional zero-shot
learning methods, which simply infers unseen categories by transferring
knowledge from the objects belonging to semantically similar seen categories,
we aim to understand the identity of the novel objects in an image surrounded
by the known objects using the inter-object relation prior. Specifically, we
leverage the visual context and the geometric relationships between all pairs
of objects in a single image, and capture the information useful to infer
unseen categories. We integrate our context-aware zero-shot learning framework
into the traditional zero-shot learning techniques seamlessly using a
Conditional Random Field (CRF). The proposed algorithm is evaluated on both
zero-shot region classification and zero-shot detection tasks. The results on
Visual Genome (VG) dataset show that our model significantly boosts performance
with the additional visual context compared to traditional methods.