---
layout: publication
title: Language-guided Hierarchical Fine-grained Image Forgery Detection And Localization
authors: Xiao Guo, Xiaohong Liu, Iacopo Masi, Xiaoming Liu
conference: Arxiv
year: 2024
bibkey: guo2024language
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.23556'}]
tags: []
short_authors: Guo et al.
---
Differences in forgery attributes of images generated in CNN-synthesized and
image-editing domains are large, and such differences make a unified image
forgery detection and localization (IFDL) challenging. To this end, we present
a hierarchical fine-grained formulation for IFDL representation learning.
Specifically, we first represent forgery attributes of a manipulated image with
multiple labels at different levels. Then, we perform fine-grained
classification at these levels using the hierarchical dependency between them.
As a result, the algorithm is encouraged to learn both comprehensive features
and the inherent hierarchical nature of different forgery attributes. In this
work, we propose a Language-guided Hierarchical Fine-grained IFDL, denoted as
HiFi-Net++. Specifically, HiFi-Net++ contains four components: a multi-branch
feature extractor, a language-guided forgery localization enhancer, as well as
classification and localization modules. Each branch of the multi-branch
feature extractor learns to classify forgery attributes at one level, while
localization and classification modules segment pixel-level forgery regions and
detect image-level forgery, respectively. Also, the language-guided forgery
localization enhancer (LFLE), containing image and text encoders learned by
contrastive language-image pre-training (CLIP), is used to further enrich the
IFDL representation. LFLE takes specifically designed texts and the given image
as multi-modal inputs and then generates the visual embedding and manipulation
score maps, which are used to further improve HiFi-Net++ manipulation
localization performance. Lastly, we construct a hierarchical fine-grained
dataset to facilitate our study. We demonstrate the effectiveness of our method
on \(8\) by using different benchmarks for both tasks of IFDL and forgery
attribute classification. Our source code and dataset are available.