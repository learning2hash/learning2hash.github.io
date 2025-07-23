---
layout: publication
title: Embedding Arithmetic Of Multimodal Queries For Image Retrieval
authors: Couairon Guillaume, Cord Matthieu, Douze Matthijs, Schwenk Holger
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: couairon2021embedding
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03162'}]
tags: ["CVPR", "Datasets", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Couairon et al.
---
Latent text representations exhibit geometric regularities, such as the
famous analogy: queen is to king what woman is to man. Such structured semantic
relations were not demonstrated on image representations. Recent works aiming
at bridging this semantic gap embed images and text into a multimodal space,
enabling the transfer of text-defined transformations to the image modality. We
introduce the SIMAT dataset to evaluate the task of Image Retrieval with
Multimodal queries. SIMAT contains 6k images and 18k textual transformation
queries that aim at either replacing scene elements or changing pairwise
relationships between scene elements. The goal is to retrieve an image
consistent with the (source image, text transformation) query. We use an
image/text matching oracle (OSCAR) to assess whether the image transformation
is successful. The SIMAT dataset will be publicly available. We use SIMAT to
evaluate the geometric properties of multimodal embedding spaces trained with
an image/text matching objective, like CLIP. We show that vanilla CLIP
embeddings are not very well suited to transform images with delta vectors, but
that a simple finetuning on the COCO dataset can bring dramatic improvements.
We also study whether it is beneficial to leverage pretrained universal
sentence encoders (FastText, LASER and LaBSE).