---
layout: publication
title: Semantic Enhanced Few-shot Object Detection
authors: Zheng Wang, Yingjie Gao, Qingjie Liu, Yunhong Wang
conference: 2024 IEEE International Conference on Image Processing (ICIP)
year: 2024
bibkey: wang2024semantic
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.13498'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Few-shot object detection~(FSOD), which aims to detect novel objects with
limited annotated instances, has made significant progress in recent years.
However, existing methods still suffer from biased representations, especially
for novel classes in extremely low-shot scenarios. During fine-tuning, a novel
class may exploit knowledge from similar base classes to construct its own
feature distribution, leading to classification confusion and performance
degradation. To address these challenges, we propose a fine-tuning based FSOD
framework that utilizes semantic embeddings for better detection. In our
proposed method, we align the visual features with class name embeddings and
replace the linear classifier with our semantic similarity classifier. Our
method trains each region proposal to converge to the corresponding class
embedding. Furthermore, we introduce a multimodal feature fusion to augment the
vision-language communication, enabling a novel class to draw support
explicitly from well-trained similar base classes. To prevent class confusion,
we propose a semantic-aware max-margin loss, which adaptively applies a margin
beyond similar classes. As a result, our method allows each novel class to
construct a compact feature space without being confused with similar base
classes. Extensive experiments on Pascal VOC and MS COCO demonstrate the
superiority of our method.