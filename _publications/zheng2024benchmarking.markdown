---
layout: publication
title: Benchmarking Pathclip For Pathology Image Analysis
authors: Sunyi Zheng, Xiaonan Cui, Yuxuan Sun, Jingxiong Li, Honglin Li, Yunlong Zhang,
  Pingyi Chen, Xueping Jing, Zhaoxiang Ye, Lin Yang
conference: Journal of Imaging Informatics in Medicine
year: 2024
bibkey: zheng2024benchmarking
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.02651'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval", "Robustness"]
short_authors: Zheng et al.
---
Accurate image classification and retrieval are of importance for clinical
diagnosis and treatment decision-making. The recent contrastive language-image
pretraining (CLIP) model has shown remarkable proficiency in understanding
natural images. Drawing inspiration from CLIP, PathCLIP is specifically
designed for pathology image analysis, utilizing over 200,000 image and text
pairs in training. While the performance the PathCLIP is impressive, its
robustness under a wide range of image corruptions remains unknown. Therefore,
we conduct an extensive evaluation to analyze the performance of PathCLIP on
various corrupted images from the datasets of Osteosarcoma and WSSS4LUAD. In
our experiments, we introduce seven corruption types including brightness,
contrast, Gaussian blur, resolution, saturation, hue, and markup at four
severity levels. Through experiments, we find that PathCLIP is relatively
robustness to image corruptions and surpasses OpenAI-CLIP and PLIP in zero-shot
classification. Among the seven corruptions, blur and resolution can cause
server performance degradation of the PathCLIP. This indicates that ensuring
the quality of images is crucial before conducting a clinical test.
Additionally, we assess the robustness of PathCLIP in the task of image-image
retrieval, revealing that PathCLIP performs less effectively than PLIP on
Osteosarcoma but performs better on WSSS4LUAD under diverse corruptions.
Overall, PathCLIP presents impressive zero-shot classification and retrieval
performance for pathology images, but appropriate care needs to be taken when
using it. We hope this study provides a qualitative impression of PathCLIP and
helps understand its differences from other CLIP models.