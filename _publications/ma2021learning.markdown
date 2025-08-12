---
layout: publication
title: Learning Instance And Task-aware Dynamic Kernels For Few Shot Learning
authors: Rongkai Ma, Pengfei Fang, Gil Avraham, Yan Zuo, Tianyu Zhu, Tom Drummond,
  Mehrtash Harandi
conference: Lecture Notes in Computer Science
year: 2022
bibkey: ma2021learning
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03494'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ma et al.
---
Learning and generalizing to novel concepts with few samples (Few-Shot
Learning) is still an essential challenge to real-world applications. A
principle way of achieving few-shot learning is to realize a model that can
rapidly adapt to the context of a given task. Dynamic networks have been shown
capable of learning content-adaptive parameters efficiently, making them
suitable for few-shot learning. In this paper, we propose to learn the dynamic
kernels of a convolution network as a function of the task at hand, enabling
faster generalization. To this end, we obtain our dynamic kernels based on the
entire task and each sample and develop a mechanism further conditioning on
each individual channel and position independently. This results in dynamic
kernels that simultaneously attend to the global information whilst also
considering minuscule details available. We empirically show that our model
improves performance on few-shot classification and detection tasks, achieving
a tangible improvement over several baseline models. This includes
state-of-the-art results on 4 few-shot classification benchmarks:
mini-ImageNet, tiered-ImageNet, CUB and FC100 and competitive results on a
few-shot detection dataset: MS COCO-PASCAL-VOC.