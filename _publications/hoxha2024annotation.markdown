---
layout: publication
title: Annotation Cost-efficient Active Learning For Deep Metric Learning Driven Remote
  Sensing Image Retrieval
authors: "Genc Hoxha, Gencer Sumbul, Julia Henkel, Lars M\xF6llenbrok, Beg\xFCm Demir"
conference: Arxiv
year: 2024
bibkey: hoxha2024annotation
citations: 0
additional_links: [{name: Code, url: 'https://git.tu-berlin.de/rsim/anneal_tgrs'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.10107'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval"]
short_authors: Hoxha et al.
---
Deep metric learning (DML) has shown to be effective for content-based image
retrieval (CBIR) in remote sensing (RS). Most of DML methods for CBIR rely on a
high number of annotated images to accurately learn model parameters of deep
neural networks (DNNs). However, gathering such data is time-consuming and
costly. To address this, we propose an annotation cost-efficient active
learning (ANNEAL) method tailored to DML-driven CBIR in RS. ANNEAL aims to
create a small but informative training set made up of similar and dissimilar
image pairs to be utilized for accurately learning a metric space. The
informativeness of image pairs is evaluated by combining uncertainty and
diversity criteria. To assess the uncertainty of image pairs, we introduce two
algorithms: 1) metric-guided uncertainty estimation (MGUE); and 2) binary
classifier guided uncertainty estimation (BCGUE). MGUE algorithm automatically
estimates a threshold value that acts as a boundary between similar and
dissimilar image pairs based on the distances in the metric space. The closer
the similarity between image pairs is to the estimated threshold value the
higher their uncertainty. BCGUE algorithm estimates the uncertainty of the
image pairs based on the confidence of the classifier in assigning correct
similarity labels. The diversity criterion is assessed through a
clustering-based strategy. ANNEAL combines either MGUE or BCGUE algorithm with
the clustering-based strategy to select the most informative image pairs, which
are then labelled by expert annotators as similar or dissimilar. This way of
annotating images significantly reduces the annotation cost compared to
annotating images with land-use land-cover class labels. Experimental results
on two RS benchmark datasets demonstrate the effectiveness of our method. The
code of this work is publicly available at
https://git.tu-berlin.de/rsim/anneal_tgrs.