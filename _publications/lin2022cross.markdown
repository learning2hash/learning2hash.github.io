---
layout: publication
title: Cross-modal Representation Learning For Zero-shot Action Recognition
authors: Chung-Ching Lin, Kevin Lin, Linjie Li, Lijuan Wang, Zicheng Liu
conference: Arxiv
year: 2022
bibkey: lin2022cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.01657'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Lin et al.
---
We present a cross-modal Transformer-based framework, which jointly encodes
video data and text labels for zero-shot action recognition (ZSAR). Our model
employs a conceptually new pipeline by which visual representations are learned
in conjunction with visual-semantic associations in an end-to-end manner. The
model design provides a natural mechanism for visual and semantic
representations to be learned in a shared knowledge space, whereby it
encourages the learned visual embedding to be discriminative and more
semantically consistent. In zero-shot inference, we devise a simple semantic
transfer scheme that embeds semantic relatedness information between seen and
unseen classes to composite unseen visual prototypes. Accordingly, the
discriminative features in the visual structure could be preserved and
exploited to alleviate the typical zero-shot issues of information loss,
semantic gap, and the hubness problem. Under a rigorous zero-shot setting of
not pre-training on additional datasets, the experiment results show our model
considerably improves upon the state of the arts in ZSAR, reaching encouraging
top-1 accuracy on UCF101, HMDB51, and ActivityNet benchmark datasets. Code will
be made available.