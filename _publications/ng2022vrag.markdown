---
layout: publication
title: 'VRAG: Region Attention Graphs For Content-based Video Retrieval'
authors: Kennard Ng, Ser-Nam Lim, Gim Hee Lee
conference: Arxiv
year: 2022
bibkey: ng2022vrag
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.09068'}]
tags: ["Efficiency", "Video Retrieval"]
short_authors: Kennard Ng, Ser-Nam Lim, Gim Hee Lee
---
Content-based Video Retrieval (CBVR) is used on media-sharing platforms for
applications such as video recommendation and filtering. To manage databases
that scale to billions of videos, video-level approaches that use fixed-size
embeddings are preferred due to their efficiency. In this paper, we introduce
Video Region Attention Graph Networks (VRAG) that improves the state-of-the-art
of video-level methods. We represent videos at a finer granularity via
region-level features and encode video spatio-temporal dynamics through
region-level relations. Our VRAG captures the relationships between regions
based on their semantic content via self-attention and the permutation
invariant aggregation of Graph Convolution. In addition, we show that the
performance gap between video-level and frame-level methods can be reduced by
segmenting videos into shots and using shot embeddings for video retrieval. We
evaluate our VRAG over several video retrieval tasks and achieve a new
state-of-the-art for video-level retrieval. Furthermore, our shot-level VRAG
shows higher retrieval precision than other existing video-level methods, and
closer performance to frame-level methods at faster evaluation speeds. Finally,
our code will be made publicly available.