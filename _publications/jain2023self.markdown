---
layout: publication
title: Self-supervised Multi-view Disentanglement For Expansion Of Visual Collections
authors: Nihal Jain, Praneetha Vaddamanu, Paridhi Maheshwari, Vishwa Vinay, Kuldeep
  Kulkarni
conference: Proceedings of the Sixteenth ACM International Conference on Web Search
  and Data Mining
year: 2023
bibkey: jain2023self
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.02249'}]
tags: [Self-Supervised, Image Retrieval, Supervised]
short_authors: Jain et al.
---
Image search engines enable the retrieval of images relevant to a query
image. In this work, we consider the setting where a query for similar images
is derived from a collection of images. For visual search, the similarity
measurements may be made along multiple axes, or views, such as style and
color. We assume access to a set of feature extractors, each of which computes
representations for a specific view. Our objective is to design a retrieval
algorithm that effectively combines similarities computed over representations
from multiple views. To this end, we propose a self-supervised learning method
for extracting disentangled view-specific representations for images such that
the inter-view overlap is minimized. We show how this allows us to compute the
intent of a collection as a distribution over views. We show how effective
retrieval can be performed by prioritizing candidate expansion images that
match the intent of a query collection. Finally, we present a new querying
mechanism for image search enabled by composing multiple collections and
perform retrieval under this setting using the techniques presented in this
paper.