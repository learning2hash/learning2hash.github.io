---
layout: publication
title: Image Retrieval Outperforms Diffusion Models On Data Augmentation
authors: Max F. Burg, Florian Wenzel, Dominik Zietlow, Max Horn, Osama Makansi, Francesco
  Locatello, Chris Russell
conference: Arxiv
year: 2023
bibkey: burg2023image
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.10253'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Burg et al.
---
Many approaches have been proposed to use diffusion models to augment
training datasets for downstream tasks, such as classification. However,
diffusion models are themselves trained on large datasets, often with noisy
annotations, and it remains an open question to which extent these models
contribute to downstream classification performance. In particular, it remains
unclear if they generalize enough to improve over directly using the additional
data of their pre-training process for augmentation. We systematically evaluate
a range of existing methods to generate images from diffusion models and study
new extensions to assess their benefit for data augmentation. Personalizing
diffusion models towards the target data outperforms simpler prompting
strategies. However, using the pre-training data of the diffusion model alone,
via a simple nearest-neighbor retrieval procedure, leads to even stronger
downstream performance. Our study explores the potential of diffusion models in
generating new training data, and surprisingly finds that these sophisticated
models are not yet able to beat a simple and strong image retrieval baseline on
simple downstream vision tasks.