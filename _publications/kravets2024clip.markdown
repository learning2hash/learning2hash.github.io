---
layout: publication
title: CLIP Adaptation By Intra-modal Overlap Reduction
authors: Alexey Kravets, Vinay Namboodiri
conference: Arxiv
year: 2024
bibkey: kravets2024clip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.11338'}]
tags: []
short_authors: Alexey Kravets, Vinay Namboodiri
---
Numerous methods have been proposed to adapt a pre-trained foundational CLIP
model for few-shot classification. As CLIP is trained on a large corpus, it
generalises well through adaptation to few-shot classification. In this work,
we analyse the intra-modal overlap in image space in terms of embedding
representation. Our analysis shows that, due to contrastive learning,
embeddings from CLIP model exhibit high cosine similarity distribution overlap
in the image space between paired and unpaired examples affecting the
performance of few-shot training-free classification methods which rely on
similarity in the image space for their predictions. To tackle intra-modal
overlap we propose to train a lightweight adapter on a generic set of samples
from the Google Open Images dataset demonstrating that this improves accuracy
for few-shot training-free classification. We validate our contribution through
extensive empirical analysis and demonstrate that reducing the intra-modal
overlap leads to a) improved performance on a number of standard datasets, b)
increased robustness to distribution shift and c) higher feature variance
rendering the features more discriminative for downstream tasks.