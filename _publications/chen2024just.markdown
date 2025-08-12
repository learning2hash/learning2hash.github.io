---
layout: publication
title: 'Just A Hint: Point-supervised Camouflaged Object Detection'
authors: Huafeng Chen, Dian Shao, Guangqian Guo, Shan Gao
conference: Arxiv
year: 2024
bibkey: chen2024just
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.10777'}]
tags: ["Supervised"]
short_authors: Chen et al.
---
Camouflaged Object Detection (COD) demands models to expeditiously and
accurately distinguish objects which conceal themselves seamlessly in the
environment. Owing to the subtle differences and ambiguous boundaries, COD is
not only a remarkably challenging task for models but also for human
annotators, requiring huge efforts to provide pixel-wise annotations. To
alleviate the heavy annotation burden, we propose to fulfill this task with the
help of only one point supervision. Specifically, by swiftly clicking on each
object, we first adaptively expand the original point-based annotation to a
reasonable hint area. Then, to avoid partial localization around discriminative
parts, we propose an attention regulator to scatter model attention to the
whole object through partially masking labeled regions. Moreover, to solve the
unstable feature representation of camouflaged objects under only point-based
annotation, we perform unsupervised contrastive learning based on differently
augmented image pairs (e.g. changing color or doing translation). On three
mainstream COD benchmarks, experimental results show that our model outperforms
several weakly-supervised methods by a large margin across various metrics.