---
layout: publication
title: 'Fashionvil: Fashion-focused Vision-and-language Representation Learning'
authors: Xiao Han, Licheng Yu, Xiatian Zhu, Li Zhang, Yi-Zhe Song, Tao Xiang
conference: Lecture Notes in Computer Science
year: 2022
bibkey: han2022fashionvil
citations: 32
additional_links: [{name: Code, url: 'https://github.com/BrandonHanx/mmf.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.08150'}]
tags: ["Image Retrieval", "Scalability", "Tools & Libraries"]
short_authors: Han et al.
---
Large-scale Vision-and-Language (V+L) pre-training for representation
learning has proven to be effective in boosting various downstream V+L tasks.
However, when it comes to the fashion domain, existing V+L methods are
inadequate as they overlook the unique characteristics of both the fashion V+L
data and downstream tasks. In this work, we propose a novel fashion-focused V+L
representation learning framework, dubbed as FashionViL. It contains two novel
fashion-specific pre-training tasks designed particularly to exploit two
intrinsic attributes with fashion V+L data. First, in contrast to other domains
where a V+L data point contains only a single image-text pair, there could be
multiple images in the fashion domain. We thus propose a Multi-View Contrastive
Learning task for pulling closer the visual representation of one image to the
compositional multimodal representation of another image+text. Second, fashion
text (e.g., product description) often contains rich fine-grained concepts
(attributes/noun phrases). To exploit this, a Pseudo-Attributes Classification
task is introduced to encourage the learned unimodal (visual/textual)
representations of the same concept to be adjacent. Further, fashion V+L tasks
uniquely include ones that do not conform to the common one-stream or
two-stream architectures (e.g., text-guided image retrieval). We thus propose a
flexible, versatile V+L model architecture consisting of a modality-agnostic
Transformer so that it can be flexibly adapted to any downstream tasks.
Extensive experiments show that our FashionViL achieves a new state of the art
across five downstream tasks. Code is available at
https://github.com/BrandonHanx/mmf.