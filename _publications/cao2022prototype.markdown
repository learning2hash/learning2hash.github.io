---
layout: publication
title: Prototype As Query For Few Shot Semantic Segmentation
authors: Leilei Cao, Yibo Guo, Ye Yuan, Qiangguo Jin
conference: Arxiv
year: 2022
bibkey: cao2022prototype
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.14764'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Cao et al.
---
Few-shot Semantic Segmentation (FSS) was proposed to segment unseen classes
in a query image, referring to only a few annotated examples named support
images. One of the characteristics of FSS is spatial inconsistency between
query and support targets, e.g., texture or appearance. This greatly challenges
the generalization ability of methods for FSS, which requires to effectively
exploit the dependency of the query image and the support examples. Most
existing methods abstracted support features into prototype vectors and
implemented the interaction with query features using cosine similarity or
feature concatenation. However, this simple interaction may not capture spatial
details in query features. To alleviate this limitation, a few methods utilized
all pixel-wise support information via computing the pixel-wise correlations
between paired query and support features implemented with the attention
mechanism of Transformer. These approaches suffer from heavy computation on the
dot-product attention between all pixels of support and query features. In this
paper, we propose a simple yet effective framework built upon Transformer
termed as ProtoFormer to fully capture spatial details in query features. It
views the abstracted prototype of the target class in support features as Query
and the query features as Key and Value embeddings, which are input to the
Transformer decoder. In this way, the spatial details can be better captured
and the semantic features of target class in the query image can be focused.
The output of the Transformer-based module can be viewed as semantic-aware
dynamic kernels to filter out the segmentation mask from the enriched query
features. Extensive experiments on PASCAL-\(5^\{i\}\) and COCO-\(20^\{i\}\) show that
our ProtoFormer significantly advances the state-of-the-art methods.