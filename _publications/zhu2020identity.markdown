---
layout: publication
title: Identity-guided Human Semantic Parsing For Person Re-identification
authors: Kuan Zhu, Haiyun Guo, Zhiwei Liu, Ming Tang, Jinqiao Wang
conference: Lecture Notes in Computer Science
year: 2020
bibkey: zhu2020identity
citations: 252
additional_links: [{name: Code, url: 'https://github.com/CASIA-IVA-Lab/ISP-reID'},
  {name: Paper, url: 'https://arxiv.org/abs/2007.13467'}]
tags: []
short_authors: Zhu et al.
---
Existing alignment-based methods have to employ the pretrained human parsing
models to achieve the pixel-level alignment, and cannot identify the personal
belongings (e.g., backpacks and reticule) which are crucial to person re-ID. In
this paper, we propose the identity-guided human semantic parsing approach
(ISP) to locate both the human body parts and personal belongings at
pixel-level for aligned person re-ID only with person identity labels. We
design the cascaded clustering on feature maps to generate the pseudo-labels of
human parts. Specifically, for the pixels of all images of a person, we first
group them to foreground or background and then group the foreground pixels to
human parts. The cluster assignments are subsequently used as pseudo-labels of
human parts to supervise the part estimation and ISP iteratively learns the
feature maps and groups them. Finally, local features of both human body parts
and personal belongings are obtained according to the selflearned part
estimation, and only features of visible parts are utilized for the retrieval.
Extensive experiments on three widely used datasets validate the superiority of
ISP over lots of state-of-the-art methods. Our code is available at
https://github.com/CASIA-IVA-Lab/ISP-reID.