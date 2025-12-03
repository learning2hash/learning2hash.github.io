---
layout: publication
title: Enhancing Sample Utilization In Noise-robust Deep Metric Learning With Subgroup-based
  Positive-pair Selection
authors: Zhipeng Yu, Qianqian Xu, Yangbangyan Jiang, Yingfei Sun, Qingming Huang
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: yu2025enhancing
citations: 1
additional_links: [{name: Code, url: 'https://github.com/smuelpeng/SGPS-NoiseFreeDML'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.11063'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Image Retrieval", "Robustness"]
short_authors: Yu et al.
---
The existence of noisy labels in real-world data negatively impacts the
performance of deep learning models. Although much research effort has been
devoted to improving the robustness towards noisy labels in classification
tasks, the problem of noisy labels in deep metric learning (DML) remains
under-explored. Existing noisy label learning methods designed for DML mainly
discard suspicious noisy samples, resulting in a waste of the training data. To
address this issue, we propose a noise-robust DML framework with SubGroup-based
Positive-pair Selection (SGPS), which constructs reliable positive pairs for
noisy samples to enhance the sample utilization. Specifically, SGPS first
effectively identifies clean and noisy samples by a probability-based clean
sample selectionstrategy. To further utilize the remaining noisy samples, we
discover their potential similar samples based on the subgroup information
given by a subgroup generation module and then aggregate them into informative
positive prototypes for each noisy sample via a positive prototype generation
module. Afterward, a new contrastive loss is tailored for the noisy samples
with their selected positive pairs. SGPS can be easily integrated into the
training process of existing pair-wise DML tasks, like image retrieval and face
recognition. Extensive experiments on multiple synthetic and real-world
large-scale label noise datasets demonstrate the effectiveness of our proposed
method. Without any bells and whistles, our SGPS framework outperforms the
state-of-the-art noisy label DML methods. Code is available at
https://github.com/smuelpeng/SGPS-NoiseFreeDML.