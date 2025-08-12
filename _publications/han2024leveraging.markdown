---
layout: publication
title: Leveraging Compressed Frame Sizes For Ultra-fast Video Classification
authors: Yuxing Han, Yunan Ding, Chen Ye Gan, Jiangtao Wen
conference: Arxiv
year: 2024
bibkey: han2024leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.08580'}]
tags: ["Efficiency"]
short_authors: Han et al.
---
Classifying videos into distinct categories, such as Sport and Music Video,
is crucial for multimedia understanding and retrieval, especially when an
immense volume of video content is being constantly generated. Traditional
methods require video decompression to extract pixel-level features like color,
texture, and motion, thereby increasing computational and storage demands.
Moreover, these methods often suffer from performance degradation in
low-quality videos. We present a novel approach that examines only the
post-compression bitstream of a video to perform classification, eliminating
the need for bitstream decoding. To validate our approach, we built a
comprehensive data set comprising over 29,000 YouTube video clips, totaling
6,000 hours and spanning 11 distinct categories. Our evaluations indicate
precision, accuracy, and recall rates consistently above 80%, many exceeding
90%, and some reaching 99%. The algorithm operates approximately 15,000 times
faster than real-time for 30fps videos, outperforming traditional Dynamic Time
Warping (DTW) algorithm by seven orders of magnitude.