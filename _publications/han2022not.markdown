---
layout: publication
title: 'Not All Instances Contribute Equally: Instance-adaptive Class Representation
  Learning For Few-shot Visual Recognition'
authors: Mengya Han, Yibing Zhan, Yong Luo, Bo Du, Han Hu, Yonggang Wen, Dacheng Tao
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2022
bibkey: han2022not
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.03034'}]
tags: []
short_authors: Han et al.
---
Few-shot visual recognition refers to recognize novel visual concepts from a
few labeled instances. Many few-shot visual recognition methods adopt the
metric-based meta-learning paradigm by comparing the query representation with
class representations to predict the category of query instance. However,
current metric-based methods generally treat all instances equally and
consequently often obtain biased class representation, considering not all
instances are equally significant when summarizing the instance-level
representations for the class-level representation. For example, some instances
may contain unrepresentative information, such as too much background and
information of unrelated concepts, which skew the results. To address the above
issues, we propose a novel metric-based meta-learning framework termed
instance-adaptive class representation learning network (ICRL-Net) for few-shot
visual recognition. Specifically, we develop an adaptive instance revaluing
network with the capability to address the biased representation issue when
generating the class representation, by learning and assigning adaptive weights
for different instances according to their relative significance in the support
set of corresponding class. Additionally, we design an improved bilinear
instance representation and incorporate two novel structural losses, i.e.,
intra-class instance clustering loss and inter-class representation
distinguishing loss, to further regulate the instance revaluation process and
refine the class representation. We conduct extensive experiments on four
commonly adopted few-shot benchmarks: miniImageNet, tieredImageNet, CIFAR-FS,
and FC100 datasets. The experimental results compared with the state-of-the-art
approaches demonstrate the superiority of our ICRL-Net.