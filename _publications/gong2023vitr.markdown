---
layout: publication
title: 'VITR: Augmenting Vision Transformers With Relation-focused Learning For Cross-modal
  Information Retrieval'
authors: Yan Gong, Georgina Cosma, Axel Finke
conference: ACM Transactions on Knowledge Discovery from Data
year: 2023
bibkey: gong2023vitr
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06350'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Yan Gong, Georgina Cosma, Axel Finke
---
The relations expressed in user queries are vital for cross-modal information
retrieval. Relation-focused cross-modal retrieval aims to retrieve information
that corresponds to these relations, enabling effective retrieval across
different modalities. Pre-trained networks, such as Contrastive Language-Image
Pre-training (CLIP), have gained significant attention and acclaim for their
exceptional performance in various cross-modal learning tasks. However, the
Vision Transformer (ViT) used in these networks is limited in its ability to
focus on image region relations. Specifically, ViT is trained to match images
with relevant descriptions at the global level, without considering the
alignment between image regions and descriptions. This paper introduces VITR, a
novel network that enhances ViT by extracting and reasoning about image region
relations based on a local encoder. VITR is comprised of two key components.
Firstly, it extends the capabilities of ViT-based cross-modal networks by
enabling them to extract and reason with region relations present in images.
Secondly, VITR incorporates a fusion module that combines the reasoned results
with global knowledge to predict similarity scores between images and
descriptions. The proposed VITR network was evaluated through experiments on
the tasks of relation-focused cross-modal information retrieval. The results
derived from the analysis of the RefCOCOg, CLEVR, and Flickr30K datasets
demonstrated that the proposed VITR network consistently outperforms
state-of-the-art networks in image-to-text and text-to-image retrieval.