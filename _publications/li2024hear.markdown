---
layout: publication
title: 'Hear The Scene: Audio-enhanced Text Spotting'
authors: Jing Li, Bo Wang
conference: Arxiv
year: 2024
bibkey: li2024hear
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.19504'}]
tags: []
short_authors: Jing Li, Bo Wang
---
Recent advancements in scene text spotting have focused on end-to-end
methodologies that heavily rely on precise location annotations, which are
often costly and labor-intensive to procure. In this study, we introduce an
innovative approach that leverages only transcription annotations for training
text spotting models, substantially reducing the dependency on elaborate
annotation processes. Our methodology employs a query-based paradigm that
facilitates the learning of implicit location features through the interaction
between text queries and image embeddings. These features are later refined
during the text recognition phase using an attention activation map. Addressing
the challenges associated with training a weakly-supervised model from scratch,
we implement a circular curriculum learning strategy to enhance model
convergence. Additionally, we introduce a coarse-to-fine cross-attention
localization mechanism for more accurate text instance localization. Notably,
our framework supports audio-based annotation, which significantly diminishes
annotation time and provides an inclusive alternative for individuals with
disabilities. Our approach achieves competitive performance against existing
benchmarks, demonstrating that high accuracy in text spotting can be attained
without extensive location annotations.