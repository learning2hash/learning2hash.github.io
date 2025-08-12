---
layout: publication
title: Transferring Knowledge For Food Image Segmentation Using Transformers And Convolutions
authors: Grant Sinha, Krish Parmar, Hilda Azimi, Amy Tai, Yuhao Chen, Alexander Wong,
  Pengcheng Xi
conference: CVPR 2023 Computer Vision in the Wild workshop
year: 2023
bibkey: sinha2023transferring
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.09203'}]
tags: ["CVPR", "Datasets", "Evaluation"]
short_authors: Sinha et al.
---
Food image segmentation is an important task that has ubiquitous
applications, such as estimating the nutritional value of a plate of food.
Although machine learning models have been used for segmentation in this
domain, food images pose several challenges. One challenge is that food items
can overlap and mix, making them difficult to distinguish. Another challenge is
the degree of inter-class similarity and intra-class variability, which is
caused by the varying preparation methods and dishes a food item may be served
in. Additionally, class imbalance is an inevitable issue in food datasets. To
address these issues, two models are trained and compared, one based on
convolutional neural networks and the other on Bidirectional Encoder
representation for Image Transformers (BEiT). The models are trained and
valuated using the FoodSeg103 dataset, which is identified as a robust
benchmark for food image segmentation. The BEiT model outperforms the previous
state-of-the-art model by achieving a mean intersection over union of 49.4 on
FoodSeg103. This study provides insights into transfering knowledge using
convolution and Transformer-based approaches in the food image domain.