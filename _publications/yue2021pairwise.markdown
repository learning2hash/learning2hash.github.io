---
layout: publication
title: Pairwise Comparison Network For Remote Sensing Scene Classification
authors: Zhang Yue, Zheng Xiangtao, Lu Xiaoqiang
conference: IEEE Geoscience and Remote Sensing Letters
year: 2021
bibkey: yue2021pairwise
citations: 13
additional_links: [{name: Code, url: 'https://github.com/spectralpublic/PCNet.git'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.08147'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zhang Yue, Zheng Xiangtao, Lu Xiaoqiang
---
Remote sensing scene classification aims to assign a specific semantic label
to a remote sensing image. Recently, convolutional neural networks have greatly
improved the performance of remote sensing scene classification. However, some
confused images may be easily recognized as the incorrect category, which
generally degrade the performance. The differences between image pairs can be
used to distinguish image categories. This paper proposed a pairwise comparison
network, which contains two main steps: pairwise selection and pairwise
representation. The proposed network first selects similar image pairs, and
then represents the image pairs with pairwise representations. The
self-representation is introduced to highlight the informative parts of each
image itself, while the mutual-representation is proposed to capture the subtle
differences between image pairs. Comprehensive experimental results on two
challenging datasets (AID, NWPU-RESISC45) demonstrate the effectiveness of the
proposed network. The codes are provided in
https://github.com/spectralpublic/PCNet.git.