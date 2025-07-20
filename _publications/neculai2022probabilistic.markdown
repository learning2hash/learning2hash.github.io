---
layout: publication
title: Probabilistic Compositional Embeddings for Multimodal Image Retrieval
authors: Neculai Andrei, Chen Yanbei, Akata Zeynep
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: neculai2022probabilistic
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.05845'}]
tags: [CVPR, Image Retrieval]
---
Existing works in image retrieval often consider retrieving images with one
or two query inputs, which do not generalize to multiple queries. In this work,
we investigate a more challenging scenario for composing multiple multimodal
queries in image retrieval. Given an arbitrary number of query images and (or)
texts, our goal is to retrieve target images containing the semantic concepts
specified in multiple multimodal queries. To learn an informative embedding
that can flexibly encode the semantics of various queries, we propose a novel
multimodal probabilistic composer (MPC). Specifically, we model input images
and texts as probabilistic embeddings, which can be further composed by a
probabilistic composition rule to facilitate image retrieval with multiple
multimodal queries. We propose a new benchmark based on the MS-COCO dataset and
evaluate our model on various setups that compose multiple images and (or) text
queries for multimodal image retrieval. Without bells and whistles, we show
that our probabilistic model formulation significantly outperforms existing
related methods on multimodal image retrieval while generalizing well to query
with different amounts of inputs given in arbitrary visual and (or) textual
modalities. Code is available here: https://github.com/andreineculai/MPC.