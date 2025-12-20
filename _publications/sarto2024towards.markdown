---
layout: publication
title: Towards Retrieval-augmented Architectures For Image Captioning
authors: Sara Sarto, Marcella Cornia, Lorenzo Baraldi, Alessandro Nicolosi, Rita Cucchiara
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2024
bibkey: sarto2024towards
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.13127'}]
tags: ["Datasets", "Neural Hashing"]
short_authors: Sarto et al.
---
The objective of image captioning models is to bridge the gap between the
visual and linguistic modalities by generating natural language descriptions
that accurately reflect the content of input images. In recent years,
researchers have leveraged deep learning-based models and made advances in the
extraction of visual features and the design of multimodal connections to
tackle this task. This work presents a novel approach towards developing image
captioning models that utilize an external kNN memory to improve the generation
process. Specifically, we propose two model variants that incorporate a
knowledge retriever component that is based on visual similarities, a
differentiable encoder to represent input images, and a kNN-augmented language
model to predict tokens based on contextual cues and text retrieved from the
external memory. We experimentally validate our approach on COCO and nocaps
datasets and demonstrate that incorporating an explicit external memory can
significantly enhance the quality of captions, especially with a larger
retrieval corpus. This work provides valuable insights into retrieval-augmented
captioning models and opens up new avenues for improving image captioning at a
larger scale.