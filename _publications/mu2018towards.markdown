---
layout: publication
title: Towards Practical Visual Search Engine within Elasticsearch
authors: Mu et al.
conference: Arxiv
year: 2018
bibkey: mu2018towards
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.08896'}]
tags: ["Image-Retrieval"]
---
In this paper, we describe our end-to-end content-based image retrieval
system built upon Elasticsearch, a well-known and popular textual search
engine. As far as we know, this is the first time such a system has been
implemented in eCommerce, and our efforts have turned out to be highly
worthwhile. We end up with a novel and exciting visual search solution that is
extremely easy to be deployed, distributed, scaled and monitored in a
cost-friendly manner. Moreover, our platform is intrinsically flexible in
supporting multimodal searches, where visual and textual information can be
jointly leveraged in retrieval.
  The core idea is to encode image feature vectors into a collection of string
tokens in a way such that closer vectors will share more string tokens in
common. By doing that, we can utilize Elasticsearch to efficiently retrieve
similar images based on similarities within encoded sting tokens. As part of
the development, we propose a novel vector to string encoding method, which is
shown to substantially outperform the previous ones in terms of both precision
and latency.
  First-hand experiences in implementing this Elasticsearch-based platform are
extensively addressed, which should be valuable to practitioners also
interested in building visual search engine on top of Elasticsearch.