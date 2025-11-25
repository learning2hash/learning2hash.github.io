---
layout: publication
title: Self-supervised Auxiliary Loss For Metric Learning In Music Similarity-based
  Retrieval And Auto-tagging
authors: Taketo Akama, Hiroaki Kitano, Katsuhiro Takematsu, Yasushi Miyajima, Natalia
  Polouliakh
conference: Arxiv
year: 2023
bibkey: akama2023self
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.07449'}]
tags: ["Distance Metric Learning", "Scalability", "Self-Supervised"]
short_authors: Akama et al.
---
In the realm of music information retrieval, similarity-based retrieval and
auto-tagging serve as essential components. Given the limitations and
non-scalability of human supervision signals, it becomes crucial for models to
learn from alternative sources to enhance their performance. Self-supervised
learning, which exclusively relies on learning signals derived from music audio
data, has demonstrated its efficacy in the context of auto-tagging. In this
study, we propose a model that builds on the self-supervised learning approach
to address the similarity-based retrieval challenge by introducing our method
of metric learning with a self-supervised auxiliary loss. Furthermore,
diverging from conventional self-supervised learning methodologies, we
discovered the advantages of concurrently training the model with both
self-supervision and supervision signals, without freezing pre-trained models.
We also found that refraining from employing augmentation during the
fine-tuning phase yields better results. Our experimental results confirm that
the proposed methodology enhances retrieval and tagging performance metrics in
two distinct scenarios: one where human-annotated tags are consistently
available for all music tracks, and another where such tags are accessible only
for a subset of tracks.