---
layout: publication
title: 'CEIA: Clip-based Event-image Alignment For Open-world Event-based Understanding'
authors: Wenhao Xu, Wenming Weng, Yueyi Zhang, Zhiwei Xiong
conference: Arxiv
year: 2024
bibkey: xu2024ceia
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.06611'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Xu et al.
---
We present CEIA, an effective framework for open-world event-based
understanding. Currently training a large event-text model still poses a huge
challenge due to the shortage of paired event-text data. In response to this
challenge, CEIA learns to align event and image data as an alternative instead
of directly aligning event and text data. Specifically, we leverage the rich
event-image datasets to learn an event embedding space aligned with the image
space of CLIP through contrastive learning. In this way, event and text data
are naturally aligned via using image data as a bridge. Particularly, CEIA
offers two distinct advantages. First, it allows us to take full advantage of
the existing event-image datasets to make up the shortage of large-scale
event-text datasets. Second, leveraging more training data, it also exhibits
the flexibility to boost performance, ensuring scalable capability. In
highlighting the versatility of our framework, we make extensive evaluations
through a diverse range of event-based multi-modal applications, such as object
recognition, event-image retrieval, event-text retrieval, and domain
adaptation. The outcomes demonstrate CEIA's distinct zero-shot superiority over
existing methods on these applications.