---
layout: publication
title: Asymmetric Image Retrieval With Cross Model Compatible Ensembles
authors: Ori Linial, Alon Shoshan, Nadav Bhonker, Elad Hirsch, Lior Zamir, Igor Kviatkovsky,
  Gerard Medioni
conference: Arxiv
year: 2023
bibkey: linial2023asymmetric
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.17531'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Linial et al.
---
The asymmetrical retrieval setting is a well suited solution for resource
constrained applications such as face recognition and image retrieval. In this
setting, a large model is used for indexing the gallery while a lightweight
model is used for querying. The key principle in such systems is ensuring that
both models share the same embedding space. Most methods in this domain are
based on knowledge distillation. While useful, they suffer from several
drawbacks: they are upper-bounded by the performance of the single best model
found and cannot be extended to use an ensemble of models in a straightforward
manner. In this paper we present an approach that does not rely on knowledge
distillation, rather it utilizes embedding transformation models. This allows
the use of N independently trained and diverse gallery models (e.g., trained on
different datasets or having a different architecture) and a single query
model. As a result, we improve the overall accuracy beyond that of any single
model while maintaining a low computational budget for querying. Additionally,
we propose a gallery image rejection method that utilizes the diversity between
multiple transformed embeddings to estimate the uncertainty of gallery images.