---
layout: publication
title: Multimodal Contrastive Training For Visual Representation Learning
authors: Xin Yuan, Zhe Lin, Jason Kuen, Jianming Zhang, Yilin Wang, Michael Maire,
  Ajinkya Kale, Baldo Faieta
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: yuan2021multimodal
citations: 125
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.12836'}]
tags: ["CVPR", "Datasets", "Multimodal Retrieval"]
short_authors: Yuan et al.
---
We develop an approach to learning visual representations that embraces
multimodal data, driven by a combination of intra- and inter-modal similarity
preservation objectives. Unlike existing visual pre-training methods, which
solve a proxy prediction task in a single domain, our method exploits intrinsic
data properties within each modality and semantic information from cross-modal
correlation simultaneously, hence improving the quality of learned visual
representations. By including multimodal training in a unified framework with
different types of contrastive losses, our method can learn more powerful and
generic visual features. We first train our model on COCO and evaluate the
learned visual representations on various downstream tasks including image
classification, object detection, and instance segmentation. For example, the
visual representations pre-trained on COCO by our method achieve
state-of-the-art top-1 validation accuracy of \(55.3%\) on ImageNet
classification, under the common transfer protocol. We also evaluate our method
on the large-scale Stock images dataset and show its effectiveness on
multi-label image tagging, and cross-modal retrieval tasks.