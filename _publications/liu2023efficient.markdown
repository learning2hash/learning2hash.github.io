---
layout: publication
title: Efficient Token-guided Image-text Retrieval With Consistent Multimodal Contrastive
  Training
authors: Liu et al.
conference: IEEE Transactions on Image Processing
year: 2023
bibkey: liu2023efficient
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08789'}]
tags: [Text Retrieval]
---
Image-text retrieval is a central problem for understanding the semantic
relationship between vision and language, and serves as the basis for various
visual and language tasks. Most previous works either simply learn
coarse-grained representations of the overall image and text, or elaborately
establish the correspondence between image regions or pixels and text words.
However, the close relations between coarse- and fine-grained representations
for each modality are important for image-text retrieval but almost neglected.
As a result, such previous works inevitably suffer from low retrieval accuracy
or heavy computational cost. In this work, we address image-text retrieval from
a novel perspective by combining coarse- and fine-grained representation
learning into a unified framework. This framework is consistent with human
cognition, as humans simultaneously pay attention to the entire sample and
regional elements to understand the semantic content. To this end, a
Token-Guided Dual Transformer (TGDT) architecture which consists of two
homogeneous branches for image and text modalities, respectively, is proposed
for image-text retrieval. The TGDT incorporates both coarse- and fine-grained
retrievals into a unified framework and beneficially leverages the advantages
of both retrieval approaches. A novel training objective called Consistent
Multimodal Contrastive (CMC) loss is proposed accordingly to ensure the intra-
and inter-modal semantic consistencies between images and texts in the common
embedding space. Equipped with a two-stage inference method based on the mixed
global and local cross-modal similarity, the proposed method achieves
state-of-the-art retrieval performances with extremely low inference time when
compared with representative recent approaches.