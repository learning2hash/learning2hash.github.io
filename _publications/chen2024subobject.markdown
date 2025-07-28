---
layout: publication
title: Subobject-level Image Tokenization
authors: Delong Chen, Samuel Cahyawijaya, Jianfeng Liu, Baoyuan Wang, Pascale Fung
conference: Arxiv
year: 2024
bibkey: chen2024subobject
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.14327'}]
tags: []
short_authors: Chen et al.
---
Patch-based image tokenization ignores the morphology of the visual world,
limiting effective and efficient learning of image understanding. Inspired by
subword tokenization, we introduce subobject-level adaptive token segmentation
and explore several approaches, including superpixel, SAM, and a proposed
Efficient and PanOptiC (EPOC) image tokenizer. Our EPOC combines boundary
detection -- a simple task that can be handled well by a compact model -- with
watershed segmentation, which inherently guarantees no pixels are left
unsegmented. Intrinsic evaluations across 5 datasets demonstrate that EPOC's
segmentation aligns well with human annotations of both object- and part-level
visual morphology, producing more monosemantic tokens and offering substantial
efficiency advantages. For extrinsic evaluation, we designed a token embedding
that handles arbitrary-shaped tokens, and trained VLMs with different
tokenizers on 4 datasets of object recognition and detailed captioning. The
results reveal that subobject tokenization enables faster convergence and
better generalization while using fewer visual tokens.