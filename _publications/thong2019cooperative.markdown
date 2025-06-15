---
layout: publication
title: 'Cooperative Embeddings For Instance, Attribute And Category Retrieval'
authors: William Thong, Cees G. M. Snoek, Arnold W. M. Smeulders
conference: "Arxiv"
year: 2019
citations: 1
bibkey: thong2019cooperative
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1904.01421'}
tags: ['Tools and Libraries', 'Applications']
---
The goal of this paper is to retrieve an image based on instance, attribute
and category similarity notions. Different from existing works, which usually
address only one of these entities in isolation, we introduce a cooperative
embedding to integrate them while preserving their specific level of semantic
representation. An algebraic structure defines a superspace filled with
instances. Attributes are axis-aligned to form subspaces, while categories
influence the arrangement of similar instances. These relationships enable them
to cooperate for their mutual benefits for image retrieval. We derive a
proxy-based softmax embedding loss to learn simultaneously all similarity
measures in both superspace and subspaces. We evaluate our model on datasets
from two different domains. Experiments on image retrieval tasks show the
benefits of the cooperative embeddings for modeling multiple image
similarities, and for discovering style evolution of instances between- and
within-categories.
