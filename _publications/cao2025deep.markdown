---
layout: publication
title: Deep Visual-semantic Hashing For Cross-modal Retrieval
authors: Yue Cao, Long, Wang, Yang, Yu
conference: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge
  Discovery and Data Mining
year: 2016
bibkey: cao2025deep
citations: 264
additional_links: [{name: Paper, url: 'http://www.kdd.org/kdd2016/papers/files/rpp0086-caoA.pdf'}]
tags: ["Compact Codes", "Datasets", "Efficiency", "Hashing Methods", "KDD", "Multimodal Retrieval", "Neural Hashing", "Scalability", "Similarity Search"]
short_authors: Cao et al.
---
Due to the storage and retrieval efficiency, hashing has been
widely applied to approximate nearest neighbor search for
large-scale multimedia retrieval. Cross-modal hashing, which
enables efficient retrieval of images in response to text queries
or vice versa, has received increasing attention recently. Most
existing work on cross-modal hashing does not capture the
spatial dependency of images and temporal dynamics of text
sentences for learning powerful feature representations and
cross-modal embeddings that mitigate the heterogeneity of
different modalities. This paper presents a new Deep Visual Semantic Hashing (DVSH) model that generates compact
hash codes of images and sentences in an end-to-end deep
learning architecture, which capture the intrinsic cross-modal
correspondences between visual data and natural language.
DVSH is a hybrid deep architecture that constitutes a visual semantic fusion network for learning joint embedding space
of images and text sentences, and two modality-specific hashing networks for learning hash functions to generate compact
binary codes. Our architecture effectively unifies joint multimodal embedding and cross-modal hashing, which is based
on a novel combination of Convolutional Neural Networks
over images, Recurrent Neural Networks over sentences, and
a structured max-margin objective that integrates all things
together to enable learning of similarity-preserving and highquality hash codes. Extensive empirical evidence shows that
our DVSH approach yields state of the art results in crossmodal retrieval experiments on image-sentences datasets,
i.e. standard IAPR TC-12 and large-scale Microsoft COCO.