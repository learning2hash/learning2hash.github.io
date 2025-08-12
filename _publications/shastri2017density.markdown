---
layout: publication
title: Density-wise Two Stage Mammogram Classification Using Texture Exploiting Descriptors
authors: Aditya A. Shastri, Deepti Tamrakar, Kapil Ahuja
conference: Expert Systems with Applications
year: 2018
bibkey: shastri2017density
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.04010'}]
tags: ["Image Retrieval"]
short_authors: Aditya A. Shastri, Deepti Tamrakar, Kapil Ahuja
---
Breast cancer is becoming pervasive with each passing day. Hence, its early
detection is a big step in saving the life of any patient. Mammography is a
common tool in breast cancer diagnosis. The most important step here is
classification of mammogram patches as normal-abnormal and benign-malignant.
  Texture of a breast in a mammogram patch plays a significant role in these
classifications. We propose a variation of Histogram of Gradients (HOG) and
Gabor filter combination called Histogram of Oriented Texture (HOT) that
exploits this fact. We also revisit the Pass Band - Discrete Cosine Transform
(PB-DCT) descriptor that captures texture information well. All features of a
mammogram patch may not be useful. Hence, we apply a feature selection
technique called Discrimination Potentiality (DP). Our resulting descriptors,
DP-HOT and DP-PB-DCT, are compared with the standard descriptors.
  Density of a mammogram patch is important for classification, and has not
been studied exhaustively. The Image Retrieval in Medical Application (IRMA)
database from RWTH Aachen, Germany is a standard database that provides
mammogram patches, and most researchers have tested their frameworks only on a
subset of patches from this database. We apply our two new descriptors on all
images of the IRMA database for density wise classification, and compare with
the standard descriptors. We achieve higher accuracy than all of the existing
standard descriptors (more than 92%).