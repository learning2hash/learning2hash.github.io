---
layout: publication
title: Data-efficient Language-supervised Zero-shot Learning With Self-distillation
authors: Ruizhe Cheng, Bichen Wu, Peizhao Zhang, Peter Vajda, Joseph E. Gonzalez
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: cheng2021data
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08945'}]
tags: ["CVPR", "Few Shot & Zero Shot", "Supervised"]
short_authors: Cheng et al.
---
Traditional computer vision models are trained to predict a fixed set of
predefined categories. Recently, natural language has been shown to be a
broader and richer source of supervision that provides finer descriptions to
visual concepts than supervised "gold" labels. Previous works, such as CLIP,
use a simple pretraining task of predicting the pairings between images and
text captions. CLIP, however, is data hungry and requires more than 400M image
text pairs for training. We propose a data-efficient contrastive distillation
method that uses soft labels to learn from noisy image-text pairs. Our model
transfers knowledge from pretrained image and sentence encoders and achieves
strong performance with only 3M image text pairs, 133x smaller than CLIP. Our
method exceeds the previous SoTA of general zero-shot learning on ImageNet
21k+1k by 73% relatively with a ResNet50 image encoder and DeCLUTR text
encoder. We also beat CLIP by 10.5% relatively on zero-shot evaluation on
Google Open Images (19,958 classes).