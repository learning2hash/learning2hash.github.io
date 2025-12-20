---
layout: publication
title: 'Medclip: Contrastive Learning From Unpaired Medical Images And Text'
authors: Zifeng Wang, Zhenbang Wu, Dinesh Agarwal, Jimeng Sun
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: wang2022medclip
citations: 402
additional_links: [{name: Code, url: 'https://github.com/RyanWangZf/MedCLIP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.10163'}]
tags: ["Datasets", "EMNLP", "Few Shot & Zero Shot", "Supervised", "Text Retrieval"]
short_authors: Wang et al.
---
Existing vision-text contrastive learning like CLIP aims to match the paired
image and caption embeddings while pushing others apart, which improves
representation transferability and supports zero-shot prediction. However,
medical image-text datasets are orders of magnitude below the general images
and captions from the internet. Moreover, previous methods encounter many false
negatives, i.e., images and reports from separate patients probably carry the
same semantics but are wrongly treated as negatives. In this paper, we decouple
images and texts for multimodal contrastive learning thus scaling the usable
training data in a combinatorial magnitude with low cost. We also propose to
replace the InfoNCE loss with semantic matching loss based on medical knowledge
to eliminate false negatives in contrastive learning. We prove that MedCLIP is
a simple yet effective framework: it outperforms state-of-the-art methods on
zero-shot prediction, supervised classification, and image-text retrieval.
Surprisingly, we observe that with only 20K pre-training data, MedCLIP wins
over the state-of-the-art method (using around 200K data). Our code is
available at https://github.com/RyanWangZf/MedCLIP.