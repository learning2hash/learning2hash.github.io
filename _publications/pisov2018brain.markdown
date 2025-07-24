---
layout: publication
title: Brain Tumor Image Retrieval Via Multitask Learning
authors: Maxim Pisov, Gleb Makarchuk, Valery Kostjuchenko, Alexandra Dalechina, Andrey
  Golanov, Mikhail Belyaev
conference: Arxiv
year: 2018
bibkey: pisov2018brain
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09369'}]
tags: ["Distance Metric Learning", "Image Retrieval"]
short_authors: Pisov et al.
---
Classification-based image retrieval systems are built by training
convolutional neural networks (CNNs) on a relevant classification problem and
using the distance in the resulting feature space as a similarity metric.
However, in practical applications, it is often desirable to have
representations which take into account several aspects of the data (e.g.,
brain tumor type and its localization). In our work, we extend the
classification-based approach with multitask learning: we train a CNN on brain
MRI scans with heterogeneous labels and implement a corresponding tumor image
retrieval system. We validate our approach on brain tumor data which contains
information about tumor types, shapes and localization. We show that our method
allows us to build representations that contain more relevant information about
tumors than single-task classification-based approaches.