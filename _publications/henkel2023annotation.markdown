---
layout: publication
title: Annotation Cost Efficient Active Learning For Content Based Image Retrieval
authors: "Julia Henkel, Genc Hoxha, Gencer Sumbul, Lars M\xF6llenbrok, Beg\xFCm Demir"
conference: IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium
year: 2023
bibkey: henkel2023annotation
citations: 1
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/ANNEAL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2306.11605'}]
tags: ["Image Retrieval"]
short_authors: Henkel et al.
---
Deep metric learning (DML) based methods have been found very effective for
content-based image retrieval (CBIR) in remote sensing (RS). For accurately
learning the model parameters of deep neural networks, most of the DML methods
require a high number of annotated training images, which can be costly to
gather. To address this problem, in this paper we present an annotation cost
efficient active learning (AL) method (denoted as ANNEAL). The proposed method
aims to iteratively enrich the training set by annotating the most informative
image pairs as similar or dissimilar, while accurately modelling a deep metric
space. This is achieved by two consecutive steps. In the first step the
pairwise image similarity is modelled based on the available training set.
Then, in the second step the most uncertain and diverse (i.e., informative)
image pairs are selected to be annotated. Unlike the existing AL methods for
CBIR, at each AL iteration of ANNEAL a human expert is asked to annotate the
most informative image pairs as similar/dissimilar. This significantly reduces
the annotation cost compared to annotating images with land-use/land cover
class labels. Experimental results show the effectiveness of our method. The
code of ANNEAL is publicly available at https://git.tu-berlin.de/rsim/ANNEAL.