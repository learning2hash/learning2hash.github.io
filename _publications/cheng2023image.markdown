---
layout: publication
title: An Image Dataset For Benchmarking Recommender Systems With Raw Pixels
authors: Yu Cheng, Yunzhu Pan, Jiaqi Zhang, Yongxin Ni, Aixin Sun, Fajie Yuan
conference: Proceedings of the 2024 SIAM International Conference on Data Mining (SDM)
year: 2024
bibkey: cheng2023image
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.06789'}]
tags: ["Datasets", "Recommender Systems"]
short_authors: Cheng et al.
---
Recommender systems (RS) have achieved significant success by leveraging
explicit identification (ID) features. However, the full potential of content
features, especially the pure image pixel features, remains relatively
unexplored. The limited availability of large, diverse, and content-driven
image recommendation datasets has hindered the use of raw images as item
representations. In this regard, we present PixelRec, a massive image-centric
recommendation dataset that includes approximately 200 million user-image
interactions, 30 million users, and 400,000 high-quality cover images. By
providing direct access to raw image pixels, PixelRec enables recommendation
models to learn item representation directly from them. To demonstrate its
utility, we begin by presenting the results of several classical pure ID-based
baseline models, termed IDNet, trained on PixelRec. Then, to show the
effectiveness of the dataset's image features, we substitute the itemID
embeddings (from IDNet) with a powerful vision encoder that represents items
using their raw image pixels. This new model is dubbed PixelNet.Our findings
indicate that even in standard, non-cold start recommendation settings where
IDNet is recognized as highly effective, PixelNet can already perform equally
well or even better than IDNet. Moreover, PixelNet has several other notable
advantages over IDNet, such as being more effective in cold-start and
cross-domain recommendation scenarios. These results underscore the importance
of visual features in PixelRec. We believe that PixelRec can serve as a
critical resource and testing ground for research on recommendation models that
emphasize image pixel content. The dataset, code, and leaderboard will be
available at https://github.com/westlake-repl/PixelRec.