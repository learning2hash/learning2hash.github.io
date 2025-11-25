---
layout: publication
title: 'CSA: Data-efficient Mapping Of Unimodal Features To Multimodal Features'
authors: Po-Han Li, Sandeep P. Chinchali, Ufuk Topcu
conference: Published at ICLR 2025
year: 2024
bibkey: li2024csa
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.07610'}]
tags: ["Few Shot & Zero Shot", "Multimodal Retrieval"]
short_authors: Po-Han Li, Sandeep P. Chinchali, Ufuk Topcu
---
Multimodal encoders like CLIP excel in tasks such as zero-shot image
classification and cross-modal retrieval. However, they require excessive
training data. We propose canonical similarity analysis (CSA), which uses two
unimodal encoders to replicate multimodal encoders using limited data. CSA maps
unimodal features into a multimodal space, using a new similarity score to
retain only the multimodal information. CSA only involves the inference of
unimodal encoders and a cubic-complexity matrix decomposition, eliminating the
need for extensive GPU-based model training. Experiments show that CSA
outperforms CLIP while requiring \(50,000\times\) fewer multimodal data pairs to
bridge the modalities given pre-trained unimodal encoders on ImageNet
classification and misinformative news caption detection. CSA surpasses the
state-of-the-art method to map unimodal features to multimodal features. We
also demonstrate the ability of CSA with modalities beyond image and text,
paving the way for future modality pairs with limited paired multimodal data
but abundant unpaired unimodal data, such as lidar and text.