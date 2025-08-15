---
layout: publication
title: Apparel-invariant Feature Learning For Apparel-changed Person Re-identification
authors: Zhengxu Yu, Yilun Zhao, Bin Hong, Zhongming Jin, Jianqiang Huang, Deng Cai,
  Xiaofei He, Xian-Sheng Hua
conference: Arxiv
year: 2020
bibkey: yu2020apparel
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.06181'}]
tags: ["Datasets", "Evaluation", "Unsupervised"]
short_authors: Yu et al.
---
With the rise of deep learning methods, person Re-Identification (ReID)
performance has been improved tremendously in many public datasets. However,
most public ReID datasets are collected in a short time window in which
persons' appearance rarely changes. In real-world applications such as in a
shopping mall, the same person's clothing may change, and different persons may
wearing similar clothes. All these cases can result in an inconsistent ReID
performance, revealing a critical problem that current ReID models heavily rely
on person's apparels. Therefore, it is critical to learn an apparel-invariant
person representation under cases like cloth changing or several persons
wearing similar clothes. In this work, we tackle this problem from the
viewpoint of invariant feature representation learning. The main contributions
of this work are as follows. (1) We propose the semi-supervised
Apparel-invariant Feature Learning (AIFL) framework to learn an
apparel-invariant pedestrian representation using images of the same person
wearing different clothes. (2) To obtain images of the same person wearing
different clothes, we propose an unsupervised apparel-simulation GAN (AS-GAN)
to synthesize cloth changing images according to the target cloth embedding.
It's worth noting that the images used in ReID tasks were cropped from
real-world low-quality CCTV videos, making it more challenging to synthesize
cloth changing images. We conduct extensive experiments on several datasets
comparing with several baselines. Experimental results demonstrate that our
proposal can improve the ReID performance of the baseline models.