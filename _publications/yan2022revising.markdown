---
layout: publication
title: Revising Image-text Retrieval Via Multi-modal Entailment
authors: Xu Yan, Chunhui Ai, Ziqiang Cao, Min Cao, Sujian Li, Wenjie Li, Guohong Fu
conference: Arxiv
year: 2022
bibkey: yan2022revising
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.10126'}]
tags: ["Text Retrieval"]
short_authors: Yan et al.
---
An outstanding image-text retrieval model depends on high-quality labeled
data. While the builders of existing image-text retrieval datasets strive to
ensure that the caption matches the linked image, they cannot prevent a caption
from fitting other images. We observe that such a many-to-many matching
phenomenon is quite common in the widely-used retrieval datasets, where one
caption can describe up to 178 images. These large matching-lost data not only
confuse the model in training but also weaken the evaluation accuracy. Inspired
by visual and textual entailment tasks, we propose a multi-modal entailment
classifier to determine whether a sentence is entailed by an image plus its
linked captions. Subsequently, we revise the image-text retrieval datasets by
adding these entailed captions as additional weak labels of an image and
develop a universal variable learning rate strategy to teach a retrieval model
to distinguish the entailed captions from other negative samples. In
experiments, we manually annotate an entailment-corrected image-text retrieval
dataset for evaluation. The results demonstrate that the proposed entailment
classifier achieves about 78% accuracy and consistently improves the
performance of image-text retrieval baselines.