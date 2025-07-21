---
layout: publication
title: The style transformer with common knowledge optimization for image-text retrieval
authors: Li et al.
conference: IEEE Signal Processing Letters
year: 2023
bibkey: li2023style
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.00448'}]
tags: []
---
Image-text retrieval which associates different modalities has drawn broad
attention due to its excellent research value and broad real-world application.
However, most of the existing methods haven't taken the high-level semantic
relationships ("style embedding") and common knowledge from multi-modalities
into full consideration. To this end, we introduce a novel style transformer
network with common knowledge optimization (CKSTN) for image-text retrieval.
The main module is the common knowledge adaptor (CKA) with both the style
embedding extractor (SEE) and the common knowledge optimization (CKO) modules.
Specifically, the SEE uses the sequential update strategy to effectively
connect the features of different stages in SEE. The CKO module is introduced
to dynamically capture the latent concepts of common knowledge from different
modalities. Besides, to get generalized temporal common knowledge, we propose a
sequential update strategy to effectively integrate the features of different
layers in SEE with previous common feature units. CKSTN demonstrates the
superiorities of the state-of-the-art methods in image-text retrieval on MSCOCO
and Flickr30K datasets. Moreover, CKSTN is constructed based on the lightweight
transformer which is more convenient and practical for the application of real
scenes, due to the better performance and lower parameters.