---
layout: publication
title: 'It''s Not A Modality Gap: Characterizing And Addressing The Contrastive Gap'
authors: Abrar Fahim, Alex Murphy, Alona Fyshe
conference: Arxiv
year: 2024
bibkey: fahim2024it
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.18570'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Abrar Fahim, Alex Murphy, Alona Fyshe
---
Multi-modal contrastive models such as CLIP achieve state-of-the-art
performance in zero-shot classification by embedding input images and texts on
a joint representational space. Recently, a modality gap has been reported in
two-encoder contrastive models like CLIP, meaning that the image and text
embeddings reside in disjoint areas of the latent space. Previous studies
suggest that this gap exists due to 1) the cone effect, 2) mismatched pairs in
the dataset, and 3) insufficient training. We show that, even when accounting
for all these factors, and even when using the same modality, the contrastive
loss actually creates a gap during training. As a result, We propose that the
modality gap is inherent to the two-encoder contrastive loss and rename it the
contrastive gap. We present evidence that attributes this contrastive gap to
low uniformity in CLIP space, resulting in embeddings that occupy only a small
portion of the latent space. To close the gap, we adapt the uniformity and
alignment properties of unimodal contrastive loss to the multi-modal setting
and show that simply adding these terms to the CLIP loss distributes the
embeddings more uniformly in the representational space, closing the gap. In
our experiments, we show that the modified representational space achieves
better performance than default CLIP loss in downstream tasks such as zero-shot
image classification and multi-modal arithmetic.