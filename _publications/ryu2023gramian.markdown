---
layout: publication
title: Gramian Attention Heads Are Strong Yet Efficient Vision Learners
authors: Jongbin Ryu, Dongyoon Han, Jongwoo Lim
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: ryu2023gramian
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Lab-LVM/imagenet-models'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.16483'}]
tags: ["ICCV"]
short_authors: Jongbin Ryu, Dongyoon Han, Jongwoo Lim
---
We introduce a novel architecture design that enhances expressiveness by
incorporating multiple head classifiers (\ie, classification heads) instead of
relying on channel expansion or additional building blocks. Our approach
employs attention-based aggregation, utilizing pairwise feature similarity to
enhance multiple lightweight heads with minimal resource overhead. We compute
the Gramian matrices to reinforce class tokens in an attention layer for each
head. This enables the heads to learn more discriminative representations,
enhancing their aggregation capabilities. Furthermore, we propose a learning
algorithm that encourages heads to complement each other by reducing
correlation for aggregation. Our models eventually surpass state-of-the-art
CNNs and ViTs regarding the accuracy-throughput trade-off on ImageNet-1K and
deliver remarkable performance across various downstream tasks, such as COCO
object instance segmentation, ADE20k semantic segmentation, and fine-grained
visual classification datasets. The effectiveness of our framework is
substantiated by practical experimental results and further underpinned by
generalization error bound. We release the code publicly at:
https://github.com/Lab-LVM/imagenet-models.