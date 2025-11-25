---
layout: publication
title: Forward Compatible Training For Large-scale Embedding Retrieval Systems
authors: Vivek Ramanujan, Pavan Kumar Anasosalu Vasu, Ali Farhadi, Oncel Tuzel, Hadi
  Pouransari
conference: Arxiv
year: 2021
bibkey: ramanujan2021forward
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.02805'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Scalability"]
short_authors: Ramanujan et al.
---
In visual retrieval systems, updating the embedding model requires
recomputing features for every piece of data. This expensive process is
referred to as backfilling. Recently, the idea of backward compatible training
(BCT) was proposed. To avoid the cost of backfilling, BCT modifies training of
the new model to make its representations compatible with those of the old
model. However, BCT can significantly hinder the performance of the new model.
In this work, we propose a new learning paradigm for representation learning:
forward compatible training (FCT). In FCT, when the old model is trained, we
also prepare for a future unknown version of the model. We propose learning
side-information, an auxiliary feature for each sample which facilitates future
updates of the model. To develop a powerful and flexible framework for model
compatibility, we combine side-information with a forward transformation from
old to new embeddings. Training of the new model is not modified, hence, its
accuracy is not degraded. We demonstrate significant retrieval accuracy
improvement compared to BCT for various datasets: ImageNet-1k (+18.1%),
Places-365 (+5.4%), and VGG-Face2 (+8.3%). FCT obtains model compatibility when
the new and old models are trained across different datasets, losses, and
architectures.