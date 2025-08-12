---
layout: publication
title: Towards Data-efficient Detection Transformers
authors: Wen Wang, Jing Zhang, Yang Cao, Yongliang Shen, Dacheng Tao
conference: Lecture Notes in Computer Science
year: 2022
bibkey: wang2022towards
citations: 55
additional_links: [{name: Code, url: 'https://github.com/encounter1997/DE-DETRs'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.09507'}]
tags: ["Efficiency"]
short_authors: Wang et al.
---
Detection Transformers have achieved competitive performance on the
sample-rich COCO dataset. However, we show most of them suffer from significant
performance drops on small-size datasets, like Cityscapes. In other words, the
detection transformers are generally data-hungry. To tackle this problem, we
empirically analyze the factors that affect data efficiency, through a
step-by-step transition from a data-efficient RCNN variant to the
representative DETR. The empirical results suggest that sparse feature sampling
from local image areas holds the key. Based on this observation, we alleviate
the data-hungry issue of existing detection transformers by simply alternating
how key and value sequences are constructed in the cross-attention layer, with
minimum modifications to the original models. Besides, we introduce a simple
yet effective label augmentation method to provide richer supervision and
improve data efficiency. Experiments show that our method can be readily
applied to different detection transformers and improve their performance on
both small-size and sample-rich datasets. Code will be made publicly available
at https://github.com/encounter1997/DE-DETRs.