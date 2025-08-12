---
layout: publication
title: Sketch-based Video Object Localization
authors: Sangmin Woo, So-yeong Jeon, Jinyoung Park, Minji Son, Sumin Lee, Changick
  Kim
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: woo2023sketch
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.00450'}]
tags: []
short_authors: Woo et al.
---
We introduce Sketch-based Video Object Localization (SVOL), a new task aimed
at localizing spatio-temporal object boxes in video queried by the input
sketch. We first outline the challenges in the SVOL task and build the
Sketch-Video Attention Network (SVANet) with the following design principles:
(i) to consider temporal information of video and bridge the domain gap between
sketch and video; (ii) to accurately identify and localize multiple objects
simultaneously; (iii) to handle various styles of sketches; (iv) to be
classification-free. In particular, SVANet is equipped with a Cross-modal
Transformer that models the interaction between learnable object tokens, query
sketch, and video through attention operations, and learns upon a per-frame set
matching strategy that enables frame-wise prediction while utilizing global
video context. We evaluate SVANet on a newly curated SVOL dataset. By design,
SVANet successfully learns the mapping between the query sketches and video
objects, achieving state-of-the-art results on the SVOL benchmark. We further
confirm the effectiveness of SVANet via extensive ablation studies and
visualizations. Lastly, we demonstrate its transfer capability on unseen
datasets and novel categories, suggesting its high scalability in real-world
applications.