---
layout: publication
title: 'COBRA: Contrastive Bi-modal Representation Algorithm'
authors: Vishaal Udandarao, Abhishek Maiti, Deepak Srivatsav, Suryatej Reddy Vyalla,
  Yifang Yin, Rajiv Ratn Shah
conference: Arxiv
year: 2020
bibkey: udandarao2020cobra
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.03687'}]
tags: ["Evaluation", "Multimodal Retrieval"]
short_authors: Udandarao et al.
---
There are a wide range of applications that involve multi-modal data, such as
cross-modal retrieval, visual question-answering, and image captioning. Such
applications are primarily dependent on aligned distributions of the different
constituent modalities. Existing approaches generate latent embeddings for each
modality in a joint fashion by representing them in a common manifold. However
these joint embedding spaces fail to sufficiently reduce the modality gap,
which affects the performance in downstream tasks. We hypothesize that these
embeddings retain the intra-class relationships but are unable to preserve the
inter-class dynamics. In this paper, we present a novel framework COBRA that
aims to train two modalities (image and text) in a joint fashion inspired by
the Contrastive Predictive Coding (CPC) and Noise Contrastive Estimation (NCE)
paradigms which preserve both inter and intra-class relationships. We
empirically show that this framework reduces the modality gap significantly and
generates a robust and task agnostic joint-embedding space. We outperform
existing work on four diverse downstream tasks spanning across seven benchmark
cross-modal datasets.