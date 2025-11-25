---
layout: publication
title: 'Feature Activation Map: Visual Explanation Of Deep Learning Models For Image
  Classification'
authors: Yi Liao, Yongsheng Gao, Weichuan Zhang
conference: Arxiv
year: 2023
bibkey: liao2023feature
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.05017'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval", "Self-Supervised"]
short_authors: Yi Liao, Yongsheng Gao, Weichuan Zhang
---
Decisions made by convolutional neural networks(CNN) can be understood and
explained by visualizing discriminative regions on images. To this end, Class
Activation Map (CAM) based methods were proposed as powerful interpretation
tools, making the prediction of deep learning models more explainable,
transparent, and trustworthy. However, all the CAM-based methods (e.g., CAM,
Grad-CAM, and Relevance-CAM) can only be used for interpreting CNN models with
fully-connected (FC) layers as a classifier. It is worth noting that many deep
learning models classify images without FC layers, e.g., few-shot learning
image classification, contrastive learning image classification, and image
retrieval tasks. In this work, a post-hoc interpretation tool named feature
activation map (FAM) is proposed, which can interpret deep learning models
without FC layers as a classifier. In the proposed FAM algorithm, the
channel-wise contribution weights are derived from the similarity scores
between two image embeddings. The activation maps are linearly combined with
the corresponding normalized contribution weights, forming the explanation map
for visualization. The quantitative and qualitative experiments conducted on
ten deep learning models for few-shot image classification, contrastive
learning image classification and image retrieval tasks demonstrate the
effectiveness of the proposed FAM algorithm.