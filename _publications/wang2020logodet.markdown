---
layout: publication
title: 'Logodet-3k: A Large-scale Image Dataset For Logo Detection'
authors: Jing Wang, Weiqing Min, Sujuan Hou, Shengnan Ma, Yuanjie Zheng, Shuqiang
  Jiang
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2022
bibkey: wang2020logodet
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.05359'}]
tags: ["Datasets"]
short_authors: Wang et al.
---
Logo detection has been gaining considerable attention because of its wide
range of applications in the multimedia field, such as copyright infringement
detection, brand visibility monitoring, and product brand management on social
media. In this paper, we introduce LogoDet-3K, the largest logo detection
dataset with full annotation, which has 3,000 logo categories, about 200,000
manually annotated logo objects and 158,652 images. LogoDet-3K creates a more
challenging benchmark for logo detection, for its higher comprehensive coverage
and wider variety in both logo categories and annotated objects compared with
existing datasets. We describe the collection and annotation process of our
dataset, analyze its scale and diversity in comparison to other datasets for
logo detection. We further propose a strong baseline method Logo-Yolo, which
incorporates Focal loss and CIoU loss into the state-of-the-art YOLOv3
framework for large-scale logo detection. Logo-Yolo can solve the problems of
multi-scale objects, logo sample imbalance and inconsistent bounding-box
regression. It obtains about 4% improvement on the average performance compared
with YOLOv3, and greater improvements compared with reported several deep
detection models on LogoDet-3K. The evaluations on other three existing
datasets further verify the effectiveness of our method, and demonstrate better
generalization ability of LogoDet-3K on logo detection and retrieval tasks. The
LogoDet-3K dataset is used to promote large-scale logo-related research and it
can be found at https://github.com/Wangjing1551/LogoDet-3K-Dataset.