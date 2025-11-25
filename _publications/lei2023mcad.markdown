---
layout: publication
title: 'MCAD: Multi-teacher Cross-modal Alignment Distillation For Efficient Image-text
  Retrieval'
authors: Youbo Lei, Feifei He, Chen Chen, Yingbin Mo, Si Jia Li, Defeng Xie, Haonan
  Lu
conference: Arxiv
year: 2023
bibkey: lei2023mcad
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.19654'}]
tags: ["Efficiency", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Lei et al.
---
Due to the success of large-scale visual-language pretraining (VLP) models
and the widespread use of image-text retrieval in industry areas, it is now
critically necessary to reduce the model size and streamline their
mobile-device deployment. Single- and dual-stream model structures are commonly
used in image-text retrieval with the goal of closing the semantic gap between
textual and visual modalities. While single-stream models use deep feature
fusion to achieve more accurate cross-model alignment, dual-stream models are
better at offline indexing and fast inference.We propose a Multi-teacher
Cross-modality Alignment Distillation (MCAD) technique to integrate the
advantages of single- and dual-stream models. By incorporating the fused
single-stream features into the image and text features of the dual-stream
model, we formulate new modified teacher similarity distributions and features.
Then, we conduct both distribution and feature distillation to boost the
capability of the student dual-stream model, achieving high retrieval
performance without increasing inference complexity.Extensive experiments
demonstrate the remarkable performance and high efficiency of MCAD on
image-text retrieval tasks. Furthermore, we implement a lightweight CLIP model
on Snapdragon/Dimensity chips with only \(\sim\)100M running memory and
\(\sim\)8.0ms search latency, achieving the mobile-device application of VLP
models.