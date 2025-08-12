---
layout: publication
title: Video Scene Parsing With Predictive Feature Learning
authors: Xiaojie Jin, Xin Li, Huaxin Xiao, Xiaohui Shen, Zhe Lin, Jimei Yang, Yunpeng
  Chen, Jian Dong, Luoqi Liu, Zequn Jie, Jiashi Feng, Shuicheng Yan
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: jin2016video
citations: 107
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.00119'}]
tags: ["ICCV"]
short_authors: Jin et al.
---
In this work, we address the challenging video scene parsing problem by
developing effective representation learning methods given limited parsing
annotations. In particular, we contribute two novel methods that constitute a
unified parsing framework. (1) \textbf\{Predictive feature learning\}\} from
nearly unlimited unlabeled video data. Different from existing methods learning
features from single frame parsing, we learn spatiotemporal discriminative
features by enforcing a parsing network to predict future frames and their
parsing maps (if available) given only historical frames. In this way, the
network can effectively learn to capture video dynamics and temporal context,
which are critical clues for video scene parsing, without requiring extra
manual annotations. (2) \textbf\{Prediction steering parsing\}\} architecture that
effectively adapts the learned spatiotemporal features to scene parsing tasks
and provides strong guidance for any off-the-shelf parsing model to achieve
better video scene parsing performance. Extensive experiments over two
challenging datasets, Cityscapes and Camvid, have demonstrated the
effectiveness of our methods by showing significant improvement over
well-established baselines.