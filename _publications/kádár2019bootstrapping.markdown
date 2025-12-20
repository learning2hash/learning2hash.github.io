---
layout: publication
title: Bootstrapping Disjoint Datasets For Multilingual Multimodal Representation
  Learning
authors: "\xC1kos K\xE1d\xE1r, Grzegorz Chrupa\u0142a, Afra Alishahi, Desmond Elliott"
conference: Arxiv
year: 2019
bibkey: "k\xE1d\xE1r2019bootstrapping"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.03678'}]
tags: ["Datasets", "Evaluation"]
short_authors: "K\xE1d\xE1r et al."
---
Recent work has highlighted the advantage of jointly learning grounded
sentence representations from multiple languages. However, the data used in
these studies has been limited to an aligned scenario: the same images
annotated with sentences in multiple languages. We focus on the more realistic
disjoint scenario in which there is no overlap between the images in
multilingual image--caption datasets. We confirm that training with aligned
data results in better grounded sentence representations than training with
disjoint data, as measured by image--sentence retrieval performance. In order
to close this gap in performance, we propose a pseudopairing method to generate
synthetically aligned English--German--image triplets from the disjoint sets.
The method works by first training a model on the disjoint data, and then
creating new triples across datasets using sentence similarity under the
learned model. Experiments show that pseudopairs improve image--sentence
retrieval performance compared to disjoint training, despite requiring no
external data or models. However, we do find that using an external machine
translation model to generate the synthetic data sets results in better
performance.