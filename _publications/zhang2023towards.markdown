---
layout: publication
title: Towards Grouping In Large Scenes With Occlusion-aware Spatio-temporal Transformers
authors: Jinsong Zhang, Lingfeng Gu, Yu-Kun Lai, Xueyang Wang, Kun Li
conference: IEEE T-CSVT 2023
year: 2023
bibkey: zhang2023towards
citations: 0
additional_links: [{name: Code, url: 'http://cic.tju.edu.cn/faculty/likun/projects/GroupTrans'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.19447'}]
tags: []
short_authors: Zhang et al.
---
Group detection, especially for large-scale scenes, has many potential
applications for public safety and smart cities. Existing methods fail to cope
with frequent occlusions in large-scale scenes with multiple people, and are
difficult to effectively utilize spatio-temporal information. In this paper, we
propose an end-to-end framework,GroupTransformer, for group detection in
large-scale scenes. To deal with the frequent occlusions caused by multiple
people, we design an occlusion encoder to detect and suppress severely occluded
person crops. To explore the potential spatio-temporal relationship, we propose
spatio-temporal transformers to simultaneously extract trajectory information
and fuse inter-person features in a hierarchical manner. Experimental results
on both large-scale and small-scale scenes demonstrate that our method achieves
better performance compared with state-of-the-art methods. On large-scale
scenes, our method significantly boosts the performance in terms of precision
and F1 score by more than 10%. On small-scale scenes, our method still improves
the performance of F1 score by more than 5%. The project page with code can be
found at http://cic.tju.edu.cn/faculty/likun/projects/GroupTrans.