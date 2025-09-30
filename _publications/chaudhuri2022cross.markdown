---
layout: publication
title: Cross-modal Fusion Distillation For Fine-grained Sketch-based Image Retrieval
authors: Abhra Chaudhuri, Massimiliano Mancini, Yanbei Chen, Zeynep Akata, Anjan Dutta
conference: Arxiv
year: 2022
bibkey: chaudhuri2022cross
citations: 2
additional_links: [{name: Code, url: 'https://github.com/abhrac/xmodal-vit'}, {name: Paper,
    url: 'https://arxiv.org/abs/2210.10486'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Chaudhuri et al.
---
Representation learning for sketch-based image retrieval has mostly been
tackled by learning embeddings that discard modality-specific information. As
instances from different modalities can often provide complementary information
describing the underlying concept, we propose a cross-attention framework for
Vision Transformers (XModalViT) that fuses modality-specific information
instead of discarding them. Our framework first maps paired datapoints from the
individual photo and sketch modalities to fused representations that unify
information from both modalities. We then decouple the input space of the
aforementioned modality fusion network into independent encoders of the
individual modalities via contrastive and relational cross-modal knowledge
distillation. Such encoders can then be applied to downstream tasks like
cross-modal retrieval. We demonstrate the expressive capacity of the learned
representations by performing a wide range of experiments and achieving
state-of-the-art results on three fine-grained sketch-based image retrieval
benchmarks: Shoe-V2, Chair-V2 and Sketchy. Implementation is available at
https://github.com/abhrac/xmodal-vit.