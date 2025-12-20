---
layout: publication
title: Optimizing Rank-based Metrics With Blackbox Differentiation
authors: "Michal Rol\xEDnek, V\xEDt Musil, Anselm Paulus, Marin Vlastelica, Claudio\
  \ Michaelis, Georg Martius"
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: "rol\xEDnek2019optimizing"
citations: 11
additional_links: [{name: Code, url: 'https://github.com/martius-lab/blackbox-backprop'},
  {name: Paper, url: 'https://arxiv.org/abs/1912.03500'}]
tags: ["CVPR", "Datasets", "Evaluation", "Image Retrieval"]
short_authors: "Rol\xEDnek et al."
---
Rank-based metrics are some of the most widely used criteria for performance
evaluation of computer vision models. Despite years of effort, direct
optimization for these metrics remains a challenge due to their
non-differentiable and non-decomposable nature. We present an efficient,
theoretically sound, and general method for differentiating rank-based metrics
with mini-batch gradient descent. In addition, we address optimization
instability and sparsity of the supervision signal that both arise from using
rank-based metrics as optimization targets. Resulting losses based on recall
and Average Precision are applied to image retrieval and object detection
tasks. We obtain performance that is competitive with state-of-the-art on
standard image retrieval datasets and consistently improve performance of near
state-of-the-art object detectors. The code is available at
https://github.com/martius-lab/blackbox-backprop