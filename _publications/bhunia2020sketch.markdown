---
layout: publication
title: 'Sketch Less For More: On-the-fly Fine-grained Sketch Based Image Retrieval'
authors: Ayan Kumar Bhunia, Yongxin Yang, Timothy M. Hospedales, Tao Xiang, Yi-Zhe
  Song
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: bhunia2020sketch
citations: 108
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.10310'}]
tags: ["CVPR", "Datasets", "Efficiency", "Image Retrieval", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Bhunia et al.
---
Fine-grained sketch-based image retrieval (FG-SBIR) addresses the problem of
retrieving a particular photo instance given a user's query sketch. Its
widespread applicability is however hindered by the fact that drawing a sketch
takes time, and most people struggle to draw a complete and faithful sketch. In
this paper, we reformulate the conventional FG-SBIR framework to tackle these
challenges, with the ultimate goal of retrieving the target photo with the
least number of strokes possible. We further propose an on-the-fly design that
starts retrieving as soon as the user starts drawing. To accomplish this, we
devise a reinforcement learning-based cross-modal retrieval framework that
directly optimizes rank of the ground-truth photo over a complete sketch
drawing episode. Additionally, we introduce a novel reward scheme that
circumvents the problems related to irrelevant sketch strokes, and thus
provides us with a more consistent rank list during the retrieval. We achieve
superior early-retrieval efficiency over state-of-the-art methods and
alternative baselines on two publicly available fine-grained sketch retrieval
datasets.