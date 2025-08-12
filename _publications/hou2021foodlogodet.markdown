---
layout: publication
title: 'Foodlogodet-1500: A Dataset For Large-scale Food Logo Detection Via Multi-scale
  Feature Decoupling Network'
authors: Qiang Hou, Weiqing Min, Jing Wang, Sujuan Hou, Yuanjie Zheng, Shuqiang Jiang
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: hou2021foodlogodet
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04644'}]
tags: ["Datasets"]
short_authors: Hou et al.
---
Food logo detection plays an important role in the multimedia for its wide
real-world applications, such as food recommendation of the self-service shop
and infringement detection on e-commerce platforms. A large-scale food logo
dataset is urgently needed for developing advanced food logo detection
algorithms. However, there are no available food logo datasets with food brand
information. To support efforts towards food logo detection, we introduce the
dataset FoodLogoDet-1500, a new large-scale publicly available food logo
dataset, which has 1,500 categories, about 100,000 images and about 150,000
manually annotated food logo objects. We describe the collection and annotation
process of FoodLogoDet-1500, analyze its scale and diversity, and compare it
with other logo datasets. To the best of our knowledge, FoodLogoDet-1500 is the
first largest publicly available high-quality dataset for food logo detection.
The challenge of food logo detection lies in the large-scale categories and
similarities between food logo categories. For that, we propose a novel food
logo detection method Multi-scale Feature Decoupling Network (MFDNet), which
decouples classification and regression into two branches and focuses on the
classification branch to solve the problem of distinguishing multiple food logo
categories. Specifically, we introduce the feature offset module, which
utilizes the deformation-learning for optimal classification offset and can
effectively obtain the most representative features of classification in
detection. In addition, we adopt a balanced feature pyramid in MFDNet, which
pays attention to global information, balances the multi-scale feature maps,
and enhances feature extraction capability. Comprehensive experiments on
FoodLogoDet-1500 and other two benchmark logo datasets demonstrate the
effectiveness of the proposed method. The FoodLogoDet-1500 can be found at this
https URL.