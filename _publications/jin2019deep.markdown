---
layout: publication
title: "Deep Semantic Multimodal Hashing Network for Scalable Image-Text and Video-Text
Retrievals"
authors: Jin Lu, Li Zechao, Tang Jinhui
conference: Arxiv
year: 2019
bibkey: jin2019deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1901.02662"}
tags: ['ARXIV', 'CNN', 'Cross Modal', 'Text Retrieval']
---
Hashing has been widely applied to multimodal retrieval on large-scale
multimedia data due to its efficiency in computation and storage. In this
article, we propose a novel deep semantic multimodal hashing network (DSMHN) for
scalable image-text and video-text retrieval. The proposed deep hashing
framework leverages 2-D convolutional neural networks (CNN) as the backbone
network to capture the spatial information for image-text retrieval, while the
3-D CNN as the backbone network to capture the spatial and temporal information
for video-text retrieval. In the DSMHN, two sets of modality-specific hash
functions are jointly learned by explicitly preserving both intermodality
similarities and intramodality semantic labels. Specifically, with the
assumption that the learned hash codes should be optimal for the classification
task, two stream networks are jointly trained to learn the hash functions by
embedding the semantic labels on the resultant hash codes. Moreover, a unified
deep multimodal hashing framework is proposed to learn compact and high-quality
hash codes by exploiting the feature representation learning, intermodality
similarity-preserving learning, semantic label-preserving learning, and hash
function learning with different types of loss functions simultaneously. The
proposed DSMHN method is a generic and scalable deep hashing framework for both
image-text and video-text retrievals, which can be flexibly integrated with
different types of loss functions. We conduct extensive experiments for both
single modal- and cross-modal-retrieval tasks on four widely used multimodal-
retrieval data sets. Experimental results on both image-text- and video-text-
retrieval tasks demonstrate that the DSMHN significantly outperforms the state-
of-the-art methods.
