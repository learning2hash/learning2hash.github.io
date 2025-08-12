---
layout: publication
title: 'EDN: Salient Object Detection Via Extremely-downsampled Network'
authors: Yu-huan Wu, Yun Liu, Le Zhang, Ming-ming Cheng, Bo Ren
conference: IEEE Transactions on Image Processing
year: 2022
bibkey: wu2020edn
citations: 164
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.13093'}]
tags: []
short_authors: Wu et al.
---
Recent progress on salient object detection (SOD) mainly benefits from
multi-scale learning, where the high-level and low-level features collaborate
in locating salient objects and discovering fine details, respectively.
However, most efforts are devoted to low-level feature learning by fusing
multi-scale features or enhancing boundary representations. High-level
features, which although have long proven effective for many other tasks, yet
have been barely studied for SOD. In this paper, we tap into this gap and show
that enhancing high- level features is essential for SOD as well. To this end,
we introduce an Extremely-Downsampled Network (EDN), which employs an extreme
downsampling technique to effectively learn a global view of the whole image,
leading to accurate salient object localization. To accomplish better
multi-level feature fusion, we construct the Scale-Correlated Pyramid
Convolution (SCPC) to build an elegant decoder for recovering object details
from the above extreme downsampling. Extensive experiments demonstrate that EDN
achieves state-of-the-art performance with real-time speed. Our efficient
EDN-Lite also achieves competitive performance with a speed of 316fps. Hence,
this work is expected to spark some new thinking in SOD. Code is available at
https://github.com/yuhuan-wu/EDN.