---
layout: publication
title: 'Dividing And Conquering Cross-modal Recipe Retrieval: From Nearest Neighbours
  Baselines To Sota'
authors: Mikhail Fain, Niall Twomey, Andrey Ponikar, Ryan Fox, Danushka Bollegala
conference: Arxiv
year: 2019
bibkey: fain2019dividing
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.12763'}]
tags: [Multimodal Retrieval, Datasets, Supervised, Distance Metric Learning, Evaluation,
  Self-Supervised]
short_authors: Fain et al.
---
We propose a novel non-parametric method for cross-modal recipe retrieval
which is applied on top of precomputed image and text embeddings. By combining
our method with standard approaches for building image and text encoders,
trained independently with a self-supervised classification objective, we
create a baseline model which outperforms most existing methods on a
challenging image-to-recipe task. We also use our method for comparing image
and text encoders trained using different modern approaches, thus addressing
the issues hindering the development of novel methods for cross-modal recipe
retrieval. We demonstrate how to use the insights from model comparison and
extend our baseline model with standard triplet loss that improves
state-of-the-art on the Recipe1M dataset by a large margin, while using only
precomputed features and with much less complexity than existing methods.
Further, our approach readily generalizes beyond recipe retrieval to other
challenging domains, achieving state-of-the-art performance on Politics and
GoodNews cross-modal retrieval tasks.