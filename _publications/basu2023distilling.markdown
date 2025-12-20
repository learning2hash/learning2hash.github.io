---
layout: publication
title: Distilling Knowledge From Text-to-image Generative Models Improves Visio-linguistic
  Reasoning In CLIP
authors: Samyadeep Basu, Shell Xu Hu, Maziar Sanjabi, Daniela Massiceti, Soheil Feizi
conference: Arxiv
year: 2023
bibkey: basu2023distilling
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.09233'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Text Retrieval"]
short_authors: Basu et al.
---
Image-text contrastive models like CLIP have wide applications in zero-shot
classification, image-text retrieval, and transfer learning. However, they
often struggle on compositional visio-linguistic tasks (e.g., attribute-binding
or object-relationships) where their performance is no better than random
chance. To address this, we introduce SDS-CLIP, a lightweight and
sample-efficient distillation method to enhance CLIP's compositional
visio-linguistic reasoning. Our approach fine-tunes CLIP using a distillation
objective borrowed from large text-to-image generative models like
Stable-Diffusion, which are known for their strong visio-linguistic reasoning
abilities. On the challenging Winoground benchmark, SDS-CLIP improves the
visio-linguistic performance of various CLIP models by up to 7%, while on the
ARO dataset, it boosts performance by up to 3%. This work underscores the
potential of well-designed distillation objectives from generative models to
enhance contrastive image-text models with improved visio-linguistic reasoning
capabilities.