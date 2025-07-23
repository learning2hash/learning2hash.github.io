---
layout: publication
title: 'Grafit: Learning Fine-grained Image Representations With Coarse Labels'
authors: "Touvron Hugo, Sablayrolles Alexandre, Douze Matthijs, Cord Matthieu, J\xE9\
  gou Herv\xE9"
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: touvron2020grafit
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.12982'}]
tags: ["ICCV", "Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Touvron et al.
---
This paper tackles the problem of learning a finer representation than the
one provided by training labels. This enables fine-grained category retrieval
of images in a collection annotated with coarse labels only.
  Our network is learned with a nearest-neighbor classifier objective, and an
instance loss inspired by self-supervised learning. By jointly leveraging the
coarse labels and the underlying fine-grained latent space, it significantly
improves the accuracy of category-level retrieval methods.
  Our strategy outperforms all competing methods for retrieving or classifying
images at a finer granularity than that available at train time. It also
improves the accuracy for transfer learning tasks to fine-grained datasets,
thereby establishing the new state of the art on five public benchmarks, like
iNaturalist-2018.