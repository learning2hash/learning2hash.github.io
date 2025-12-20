---
layout: publication
title: 'Ernie-vil 2.0: Multi-view Contrastive Learning For Image-text Pre-training'
authors: Bin Shan, Weichong Yin, Yu Sun, Hao Tian, Hua Wu, Haifeng Wang
conference: Arxiv
year: 2022
bibkey: shan2022ernie
citations: 10
additional_links: [{name: Code, url: 'https://github.com/PaddlePaddle/ERNIE'}, {name: Paper,
    url: 'https://arxiv.org/abs/2209.15270'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Shan et al.
---
Recent Vision-Language Pre-trained (VLP) models based on dual encoder have
attracted extensive attention from academia and industry due to their superior
performance on various cross-modal tasks and high computational efficiency.
They attempt to learn cross-modal representation using contrastive learning on
image-text pairs, however, the built inter-modal correlations only rely on a
single view for each modality. Actually, an image or a text contains various
potential views, just as humans could capture a real-world scene via diverse
descriptions or photos. In this paper, we propose ERNIE-ViL 2.0, a Multi-View
Contrastive learning framework to build intra-modal and inter-modal
correlations between diverse views simultaneously, aiming at learning a more
robust cross-modal representation. Specifically, we construct multiple views
within each modality to learn the intra-modal correlation for enhancing the
single-modal representation. Besides the inherent visual/textual views, we
construct sequences of object tags as a special textual view to narrow the
cross-modal semantic gap on noisy image-text pairs. Pre-trained with 29M
publicly available datasets, ERNIE-ViL 2.0 achieves competitive results on
English cross-modal retrieval. Additionally, to generalize our method to
Chinese cross-modal tasks, we train ERNIE-ViL 2.0 through scaling up the
pre-training datasets to 1.5B Chinese image-text pairs, resulting in
significant improvements compared to previous SOTA results on Chinese
cross-modal retrieval. We release our pre-trained models in
https://github.com/PaddlePaddle/ERNIE.