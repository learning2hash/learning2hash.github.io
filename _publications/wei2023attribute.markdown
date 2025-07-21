---
layout: publication
title: Attribute-Aware Deep Hashing with Self-Consistency for Large-Scale Fine-Grained
  Image Retrieval
authors: Wei et al.
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: wei2023attribute
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.12894'}]
tags: ["Hashing-Methods", "Neural-Hashing", "Image-Retrieval", "Scalability"]
---
Our work focuses on tackling large-scale fine-grained image retrieval as
ranking the images depicting the concept of interests (i.e., the same
sub-category labels) highest based on the fine-grained details in the query. It
is desirable to alleviate the challenges of both fine-grained nature of small
inter-class variations with large intra-class variations and explosive growth
of fine-grained data for such a practical task. In this paper, we propose
attribute-aware hashing networks with self-consistency for generating
attribute-aware hash codes to not only make the retrieval process efficient,
but also establish explicit correspondences between hash codes and visual
attributes. Specifically, based on the captured visual representations by
attention, we develop an encoder-decoder structure network of a reconstruction
task to unsupervisedly distill high-level attribute-specific vectors from the
appearance-specific visual representations without attribute annotations. Our
models are also equipped with a feature decorrelation constraint upon these
attribute vectors to strengthen their representative abilities. Then, driven by
preserving original entities' similarity, the required hash codes can be
generated from these attribute-specific vectors and thus become
attribute-aware. Furthermore, to combat simplicity bias in deep hashing, we
consider the model design from the perspective of the self-consistency
principle and propose to further enhance models' self-consistency by equipping
an additional image reconstruction path. Comprehensive quantitative experiments
under diverse empirical settings on six fine-grained retrieval datasets and two
generic retrieval datasets show the superiority of our models over competing
methods.