---
layout: publication
title: Training CLIP Models On Data From Scientific Papers
authors: Calvin Metzger
conference: Arxiv
year: 2023
bibkey: metzger2023training
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.04711'}]
tags: [Scalability, Evaluation, Image Retrieval, Datasets]
short_authors: Calvin Metzger
---
Contrastive Language-Image Pretraining (CLIP) models are able to capture the
semantic relationship of images and texts and have enabled a wide range of
applications, from image retrieval to classification. These models are trained
with datasets extracted from web crawls, which are of large quantity but
limited quality. This paper explores whether limited amounts higher quality
data in a specific domain improve the general performance of CLIP models. To
this purpose, we extract text-image data from scientific papers hosted in the
arXiv and PubMed Central repositories. Experiments on small-scale CLIP models
(ViT B/32) show that model performance increases on average, but only
moderately. This result indicates that using the data sources considered in the
paper to train large-scale CLIP models is a worthwile research direction.