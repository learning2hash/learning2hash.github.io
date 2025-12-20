---
layout: publication
title: Self-supervised Video Similarity Learning
authors: Giorgos Kordopatis-Zilos, Giorgos Tolias, Christos Tzelepis, Ioannis Kompatsiaris,
  Ioannis Patras, Symeon Papadopoulos
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2023
bibkey: kordopatiszilos2023self
citations: 16
additional_links: [{name: Code, url: 'https://github.com/gkordo/s2vs'}, {name: Paper,
    url: 'https://arxiv.org/abs/2304.03378'}]
tags: ["CVPR", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Kordopatis-Zilos et al.
---
We introduce S\(^2\)VS, a video similarity learning approach with
self-supervision. Self-Supervised Learning (SSL) is typically used to train
deep models on a proxy task so as to have strong transferability on target
tasks after fine-tuning. Here, in contrast to prior work, SSL is used to
perform video similarity learning and address multiple retrieval and detection
tasks at once with no use of labeled data. This is achieved by learning via
instance-discrimination with task-tailored augmentations and the widely used
InfoNCE loss together with an additional loss operating jointly on
self-similarity and hard-negative similarity. We benchmark our method on tasks
where video relevance is defined with varying granularity, ranging from video
copies to videos depicting the same incident or event. We learn a single
universal model that achieves state-of-the-art performance on all tasks,
surpassing previously proposed methods that use labeled data. The code and
pretrained models are publicly available at: https://github.com/gkordo/s2vs