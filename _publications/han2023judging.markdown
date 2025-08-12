---
layout: publication
title: Judging A Video By Its Bitstream Cover
authors: Yuxing Han, Yunan Ding, Jiangtao Wen, Chen Ye Gan
conference: 2024 Data Compression Conference (DCC)
year: 2024
bibkey: han2023judging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.07361'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Han et al.
---
Classifying videos into distinct categories, such as Sport and Music Video,
is crucial for multimedia understanding and retrieval, especially in an age
where an immense volume of video content is constantly being generated.
Traditional methods require video decompression to extract pixel-level features
like color, texture, and motion, thereby increasing computational and storage
demands. Moreover, these methods often suffer from performance degradation in
low-quality videos. We present a novel approach that examines only the
post-compression bitstream of a video to perform classification, eliminating
the need for bitstream. We validate our approach using a custom-built data set
comprising over 29,000 YouTube video clips, totaling 6,000 hours and spanning
11 distinct categories. Our preliminary evaluations indicate precision,
accuracy, and recall rates well over 80%. The algorithm operates approximately
15,000 times faster than real-time for 30fps videos, outperforming traditional
Dynamic Time Warping (DTW) algorithm by six orders of magnitude.