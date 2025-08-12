---
layout: publication
title: 'Ovfoodseg: Elevating Open-vocabulary Food Image Segmentation Via Image-informed
  Textual Representation'
authors: Xiongwei Wu, Sicheng Yu, Ee-Peng Lim, Chong-Wah Ngo
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: wu2024ovfoodseg
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01409'}]
tags: ["CVPR"]
short_authors: Wu et al.
---
In the realm of food computing, segmenting ingredients from images poses
substantial challenges due to the large intra-class variance among the same
ingredients, the emergence of new ingredients, and the high annotation costs
associated with large food segmentation datasets. Existing approaches primarily
utilize a closed-vocabulary and static text embeddings setting. These methods
often fall short in effectively handling the ingredients, particularly new and
diverse ones. In response to these limitations, we introduce OVFoodSeg, a
framework that adopts an open-vocabulary setting and enhances text embeddings
with visual context. By integrating vision-language models (VLMs), our approach
enriches text embedding with image-specific information through two innovative
modules, eg, an image-to-text learner FoodLearner and an Image-Informed Text
Encoder. The training process of OVFoodSeg is divided into two stages: the
pre-training of FoodLearner and the subsequent learning phase for segmentation.
The pre-training phase equips FoodLearner with the capability to align visual
information with corresponding textual representations that are specifically
related to food, while the second phase adapts both the FoodLearner and the
Image-Informed Text Encoder for the segmentation task. By addressing the
deficiencies of previous models, OVFoodSeg demonstrates a significant
improvement, achieving an 4.9% increase in mean Intersection over Union (mIoU)
on the FoodSeg103 dataset, setting a new milestone for food image segmentation.