---
layout: publication
title: 'All The Attention You Need: Global-local, Spatial-channel Attention For Image
  Retrieval'
authors: Chull Hwan Song, Hye Joo Han, Yannis Avrithis
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: song2021all
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.08000'}]
tags: [Scalability, Evaluation, Image Retrieval]
short_authors: Chull Hwan Song, Hye Joo Han, Yannis Avrithis
---
We address representation learning for large-scale instance-level image
retrieval. Apart from backbone, training pipelines and loss functions, popular
approaches have focused on different spatial pooling and attention mechanisms,
which are at the core of learning a powerful global image representation. There
are different forms of attention according to the interaction of elements of
the feature tensor (local and global) and the dimensions where it is applied
(spatial and channel). Unfortunately, each study addresses only one or two
forms of attention and applies it to different problems like classification,
detection or retrieval.
  We present global-local attention module (GLAM), which is attached at the end
of a backbone network and incorporates all four forms of attention: local and
global, spatial and channel. We obtain a new feature tensor and, by spatial
pooling, we learn a powerful embedding for image retrieval. Focusing on global
descriptors, we provide empirical evidence of the interaction of all forms of
attention and improve the state of the art on standard benchmarks.