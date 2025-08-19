---
layout: publication
title: Multi-spectral Remote Sensing Image Retrieval Using Geospatial Foundation Models
authors: Benedikt Blumenstiel, Viktoria Moor, Romeo Kienzler, Thomas Brunschwiler
conference: IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium
year: 2024
bibkey: blumenstiel2024multi
citations: 2
additional_links: [{name: Code, url: 'https://github.com/IBM/remote-sensing-image-retrieval.'},
  {name: Paper, url: 'https://arxiv.org/abs/2403.02059'}]
tags: [Neural Hashing, Evaluation, RSS, Image Retrieval, Hashing Methods, Datasets]
short_authors: Blumenstiel et al.
---
Image retrieval enables an efficient search through vast amounts of satellite
imagery and returns similar images to a query. Deep learning models can
identify images across various semantic concepts without the need for
annotations. This work proposes to use Geospatial Foundation Models, like
Prithvi, for remote sensing image retrieval with multiple benefits: i) the
models encode multi-spectral satellite data and ii) generalize without further
fine-tuning. We introduce two datasets to the retrieval task and observe a
strong performance: Prithvi processes six bands and achieves a mean Average
Precision of 97.62% on BigEarthNet-43 and 44.51% on ForestNet-12, outperforming
other RGB-based models. Further, we evaluate three compression methods with
binarized embeddings balancing retrieval speed and accuracy. They match the
retrieval speed of much shorter hash codes while maintaining the same accuracy
as floating-point embeddings but with a 32-fold compression. The code is
available at https://github.com/IBM/remote-sensing-image-retrieval.