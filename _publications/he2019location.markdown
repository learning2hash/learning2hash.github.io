---
layout: publication
title: Location-aware Upsampling For Semantic Segmentation
authors: Xiangyu He, Zitao Mo, Qiang Chen, Anda Cheng, Peisong Wang, Jian Cheng
conference: Arxiv
year: 2019
bibkey: he2019location
citations: 2
additional_links: [{name: Code, url: 'https://github.com/HolmesShuan/Location-aware-Upsampling-for-Semantic-Segmentation'},
  {name: Paper, url: 'https://arxiv.org/abs/1911.05250'}]
tags: []
short_authors: He et al.
---
Many successful learning targets such as minimizing dice loss and
cross-entropy loss have enabled unprecedented breakthroughs in segmentation
tasks. Beyond these semantic metrics, this paper aims to introduce location
supervision into semantic segmentation. Based on this idea, we present a
Location-aware Upsampling (LaU) that adaptively refines the interpolating
coordinates with trainable offsets. Then, location-aware losses are established
by encouraging pixels to move towards well-classified locations. An LaU is
offset prediction coupled with interpolation, which is trained end-to-end to
generate confidence score at each position from coarse to fine. Guided by
location-aware losses, the new module can replace its plain counterpart
(\textit\{e.g.\}, bilinear upsampling) in a plug-and-play manner to further boost
the leading encoder-decoder approaches. Extensive experiments validate the
consistent improvement over the state-of-the-art methods on benchmark datasets.
Our code is available at
https://github.com/HolmesShuan/Location-aware-Upsampling-for-Semantic-Segmentation