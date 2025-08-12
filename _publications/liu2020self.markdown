---
layout: publication
title: 'Self-emd: Self-supervised Object Detection Without Imagenet'
authors: Songtao Liu, Zeming Li, Jian Sun
conference: Arxiv
year: 2020
bibkey: liu2020self
citations: 66
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.13677'}]
tags: ["Self-Supervised"]
short_authors: Songtao Liu, Zeming Li, Jian Sun
---
In this paper, we propose a novel self-supervised representation learning
method, Self-EMD, for object detection. Our method directly trained on
unlabeled non-iconic image dataset like COCO, instead of commonly used
iconic-object image dataset like ImageNet. We keep the convolutional feature
maps as the image embedding to preserve spatial structures and adopt Earth
Mover's Distance (EMD) to compute the similarity between two embeddings. Our
Faster R-CNN (ResNet50-FPN) baseline achieves 39.8% mAP on COCO, which is on
par with the state of the art self-supervised methods pre-trained on ImageNet.
More importantly, it can be further improved to 40.4% mAP with more unlabeled
images, showing its great potential for leveraging more easily obtained
unlabeled data. Code will be made available.