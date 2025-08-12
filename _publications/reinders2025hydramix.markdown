---
layout: publication
title: 'Hydramix: Multi-image Feature Mixing For Small Data Image Classification'
authors: Christoph Reinders, Frederik Schubert, Bodo Rosenhahn
conference: Arxiv
year: 2025
bibkey: reinders2025hydramix
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.09504'}]
tags: []
short_authors: Christoph Reinders, Frederik Schubert, Bodo Rosenhahn
---
Training deep neural networks requires datasets with a large number of
annotated examples. The collection and annotation of these datasets is not only
extremely expensive but also faces legal and privacy problems. These factors
are a significant limitation for many real-world applications. To address this,
we introduce HydraMix, a novel architecture that generates new image
compositions by mixing multiple different images from the same class. HydraMix
learns the fusion of the content of various images guided by a
segmentation-based mixing mask in feature space and is optimized via a
combination of unsupervised and adversarial training. Our data augmentation
scheme allows the creation of models trained from scratch on very small
datasets. We conduct extensive experiments on ciFAIR-10, STL-10, and
ciFAIR-100. Additionally, we introduce a novel text-image metric to assess the
generality of the augmented datasets. Our results show that HydraMix
outperforms existing state-of-the-art methods for image classification on small
datasets.