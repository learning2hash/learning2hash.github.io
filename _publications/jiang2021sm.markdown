---
layout: publication
title: 'SM+: Refined Scale Match For Tiny Person Detection'
authors: Nan Jiang, Xuehui Yu, Xiaoke Peng, Yuqi Gong, Zhenjun Han
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: jiang2021sm
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.03558'}]
tags: ["ICASSP"]
short_authors: Jiang et al.
---
Detecting tiny objects ( e.g., less than 20 x 20 pixels) in large-scale
images is an important yet open problem. Modern CNN-based detectors are
challenged by the scale mismatch between the dataset for network pre-training
and the target dataset for detector training. In this paper, we investigate the
scale alignment between pre-training and target datasets, and propose a new
refined Scale Match method (termed SM+) for tiny person detection. SM+ improves
the scale match from image level to instance level, and effectively promotes
the similarity between pre-training and target dataset. Moreover, considering
SM+ possibly destroys the image structure, a new probabilistic structure
inpainting (PSI) method is proposed for the background processing. Experiments
conducted across various detectors show that SM+ noticeably improves the
performance on TinyPerson, and outperforms the state-of-the-art detectors with
a significant margin.