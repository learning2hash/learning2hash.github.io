---
layout: publication
title: A Feature-space Multimodal Data Augmentation Technique For Text-video Retrieval
authors: Alex Falcon, Giuseppe Serra, Oswald Lanz
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: falcon2022a
citations: 23
additional_links: [{name: Code, url: 'https://github.com/aranciokov/FSMMDA_VideoRetrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2208.02080'}]
tags: [Video Retrieval, Evaluation, Scalability, Datasets]
short_authors: Alex Falcon, Giuseppe Serra, Oswald Lanz
---
Every hour, huge amounts of visual contents are posted on social media and
user-generated content platforms. To find relevant videos by means of a natural
language query, text-video retrieval methods have received increased attention
over the past few years. Data augmentation techniques were introduced to
increase the performance on unseen test examples by creating new training
samples with the application of semantics-preserving techniques, such as color
space or geometric transformations on images. Yet, these techniques are usually
applied on raw data, leading to more resource-demanding solutions and also
requiring the shareability of the raw data, which may not always be true, e.g.
copyright issues with clips from movies or TV series. To address this
shortcoming, we propose a multimodal data augmentation technique which works in
the feature space and creates new videos and captions by mixing semantically
similar samples. We experiment our solution on a large scale public dataset,
EPIC-Kitchens-100, and achieve considerable improvements over a baseline
method, improved state-of-the-art performance, while at the same time
performing multiple ablation studies. We release code and pretrained models on
Github at https://github.com/aranciokov/FSMMDA_VideoRetrieval.