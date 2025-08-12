---
layout: publication
title: Deep Shape Matching
authors: "Filip Radenovi\u0107, Giorgos Tolias, Ond\u0159ej Chum"
conference: Lecture Notes in Computer Science
year: 2018
bibkey: "radenovi\u01072017deep"
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.03409'}]
tags: ["Distance Metric Learning"]
short_authors: "Filip Radenovi\u0107, Giorgos Tolias, Ond\u0159ej Chum"
---
We cast shape matching as metric learning with convolutional networks. We
break the end-to-end process of image representation into two parts. Firstly,
well established efficient methods are chosen to turn the images into edge
maps. Secondly, the network is trained with edge maps of landmark images, which
are automatically obtained by a structure-from-motion pipeline. The learned
representation is evaluated on a range of different tasks, providing
improvements on challenging cases of domain generalization, generic
sketch-based image retrieval or its fine-grained counterpart. In contrast to
other methods that learn a different model per task, object category, or
domain, we use the same network throughout all our experiments, achieving
state-of-the-art results in multiple benchmarks.