---
layout: publication
title: Fine-grained Few-shot Recognition By Deep Object Parsing
authors: Ruizhao Zhu, Pengkai Zhu, Samarth Mishra, Venkatesh Saligrama
conference: Arxiv
year: 2022
bibkey: zhu2022fine
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.07110'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhu et al.
---
We propose a new method for fine-grained few-shot recognition via deep object
parsing. In our framework, an object is made up of K distinct parts and for
each part, we learn a dictionary of templates, which is shared across all
instances and categories. An object is parsed by estimating the locations of
these K parts and a set of active templates that can reconstruct the part
features. We recognize test instances by comparing its active templates and the
relative geometry of its part locations against those of the presented few-shot
instances. Our method is end-to-end trainable to learn part templates on-top of
a convolutional backbone. To combat visual distortions such as orientation,
pose and size, we learn templates at multiple scales, and at test-time parse
and match instances across these scales. We show that our method is competitive
with the state-of-the-art, and by virtue of parsing enjoys interpretability as
well.