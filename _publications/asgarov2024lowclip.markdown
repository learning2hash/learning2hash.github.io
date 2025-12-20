---
layout: publication
title: 'Lowclip: Adapting The CLIP Model Architecture For Low-resource Languages In
  Multimodal Image Retrieval Task'
authors: Ali Asgarov, Samir Rustamov
conference: Arxiv
year: 2024
bibkey: asgarov2024lowclip
citations: 0
additional_links: [{name: Code, url: 'https://github.com/aliasgerovs/azclip'}, {name: Paper,
    url: 'https://arxiv.org/abs/2408.13909'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Ali Asgarov, Samir Rustamov
---
This research explores the development of multimodal vision-language models
for image retrieval in low-resource languages, specifically Azerbaijani.
Existing vision-language models primarily support high-resource languages, and
fine-tuning them remains computationally demanding. To address challenges in
vision-language retrieval for low-resource languages, we integrated the CLIP
model architecture and employed several techniques to balance computational
efficiency with performance. These techniques include synthetic data generation
through machine translation, image augmentation, and further training the
attention mechanisms of transformer-based models with domain-specific data. We
integrated Multilingual BERT as a text encoder with image encoders like
ResNet50, EfficientNet0, Vision Transformer (ViT), and Tiny Swin Transformer.
Our study found that models like EfficientNet0 and Tiny Swin Transformer
perform best on the datasets they were trained on, such as COCO, Flickr30k, and
Flickr8k. Augmentation techniques boosted EfficientNet0 MAP on Flickr30k from
0.84 to 0.87 and ResNet50 MAP on MSCOCO from 0.70 to 0.80, contributing to a
new state of the art in vision-language retrieval. We share our configurations
and results to support further research. Code and pre-trained models are
available at https://github.com/aliasgerovs/azclip.