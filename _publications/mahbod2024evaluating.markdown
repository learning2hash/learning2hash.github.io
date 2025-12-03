---
layout: publication
title: Evaluating Pre-trained Convolutional Neural Networks And Foundation Models
  As Feature Extractors For Content-based Medical Image Retrieval
authors: Amirreza Mahbod, Nematollah Saeidi, Sepideh Hatamikia, Ramona Woitek
conference: Arxiv
year: 2024
bibkey: mahbod2024evaluating
citations: 1
additional_links: [{name: Code, url: 'https://github.com/masih4/MedImageRetrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.09430'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Mahbod et al.
---
Medical image retrieval refers to the task of finding similar images for
given query images in a database, with applications such as diagnosis support.
While traditional medical image retrieval relied on clinical metadata,
content-based medical image retrieval (CBMIR) depends on image features, which
can be extracted automatically or semi-automatically. Many approaches have been
proposed for CBMIR, and among them, using pre-trained convolutional neural
networks (CNNs) is a widely utilized approach. However, considering the recent
advances in the development of foundation models for various computer vision
tasks, their application for CBMIR can also be investigated.
  In this study, we used several pre-trained feature extractors from well-known
pre-trained CNNs and pre-trained foundation models and investigated the CBMIR
performance on eight types of two-dimensional (2D) and three-dimensional (3D)
medical images. Furthermore, we investigated the effect of image size on the
CBMIR performance.
  Our results show that, overall, for the 2D datasets, foundation models
deliver superior performance by a large margin compared to CNNs, with the
general-purpose self-supervised model for computational pathology (UNI)
providing the best overall performance across all datasets and image sizes. For
3D datasets, CNNs and foundation models deliver more competitive performance,
with contrastive learning from captions for histopathology model (CONCH)
achieving the best overall performance. Moreover, our findings confirm that
while using larger image sizes (especially for 2D datasets) yields slightly
better performance, competitive CBMIR performance can still be achieved even
with smaller image sizes. Our codes to reproduce the results are available at:
https://github.com/masih4/MedImageRetrieval.