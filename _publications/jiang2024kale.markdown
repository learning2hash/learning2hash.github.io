---
layout: publication
title: 'KALE: An Artwork Image Captioning System Augmented With Heterogeneous Graph'
authors: Yanbei Jiang, Krista A. Ehinger, Jey Han Lau
conference: Proceedings of the Thirty-ThirdInternational Joint Conference on Artificial
  Intelligence
year: 2024
bibkey: jiang2024kale
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Yanbei-Jiang/Artwork-Interpretation'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.10921'}]
tags: []
short_authors: Yanbei Jiang, Krista A. Ehinger, Jey Han Lau
---
Exploring the narratives conveyed by fine-art paintings is a challenge in
image captioning, where the goal is to generate descriptions that not only
precisely represent the visual content but also offer a in-depth interpretation
of the artwork's meaning. The task is particularly complex for artwork images
due to their diverse interpretations and varied aesthetic principles across
different artistic schools and styles. In response to this, we present KALE
Knowledge-Augmented vision-Language model for artwork Elaborations), a novel
approach that enhances existing vision-language models by integrating artwork
metadata as additional knowledge. KALE incorporates the metadata in two ways:
firstly as direct textual input, and secondly through a multimodal
heterogeneous knowledge graph. To optimize the learning of graph
representations, we introduce a new cross-modal alignment loss that maximizes
the similarity between the image and its corresponding metadata. Experimental
results demonstrate that KALE achieves strong performance (when evaluated with
CIDEr, in particular) over existing state-of-the-art work across several
artwork datasets. Source code of the project is available at
https://github.com/Yanbei-Jiang/Artwork-Interpretation.