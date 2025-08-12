---
layout: publication
title: Robust Saliency-aware Distillation For Few-shot Fine-grained Visual Recognition
authors: Haiqi Liu, C. L. Philip Chen, Xinrong Gong, Tong Zhang
conference: IEEE Transactions on Multimedia
year: 2024
bibkey: liu2023robust
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.07180'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Recognizing novel sub-categories with scarce samples is an essential and
challenging research topic in computer vision. Existing literature addresses
this challenge by employing local-based representation approaches, which may
not sufficiently facilitate meaningful object-specific semantic understanding,
leading to a reliance on apparent background correlations. Moreover, they
primarily rely on high-dimensional local descriptors to construct complex
embedding space, potentially limiting the generalization. To address the above
challenges, this article proposes a novel model, Robust Saliency-aware
Distillation (RSaD), for few-shot fine-grained visual recognition. RSaD
introduces additional saliency-aware supervision via saliency detection to
guide the model toward focusing on the intrinsic discriminative regions.
Specifically, RSaD utilizes the saliency detection model to emphasize the
critical regions of each sub-category, providing additional object-specific
information for fine-grained prediction. RSaD transfers such information with
two symmetric branches in a mutual learning paradigm. Furthermore, RSaD
exploits inter-regional relationships to enhance the informativeness of the
representation and subsequently summarize the highlighted details into
contextual embeddings to facilitate the effective transfer, enabling quick
generalization to novel sub-categories. The proposed approach is empirically
evaluated on three widely used benchmarks, demonstrating its superior
performance.