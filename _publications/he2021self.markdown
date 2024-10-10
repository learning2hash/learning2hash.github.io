---
layout: publication
title: Self-supervised Video Retrieval Transformer Network
authors: He Xiangteng, Pan Yulin, Tang Mingqian, Lv Yiliang
conference: "Arxiv"
year: 2021
bibkey: he2021self
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.07993"}
tags: ['ARXIV', 'Supervised', 'Video Retrieval']
---
Content-based video retrieval aims to find videos from a large video database that are similar to or even near-duplicate of a given query video. Video representation and similarity search algorithms are crucial to any video retrieval system. To derive effective video representation most video retrieval systems require a large amount of manually annotated data for training making it costly inefficient. In addition most retrieval systems are based on frame-level features for video similarity searching making it expensive both storage wise and search wise. We propose a novel video retrieval system termed SVRTN that effectively addresses the above shortcomings. It first applies self-supervised training to effectively learn video representation from unlabeled data to avoid the expensive cost of manual annotation. Then it exploits transformer structure to aggregate frame-level features into clip-level to reduce both storage space and search complexity. It can learn the complementary and discriminative information from the interactions among clip frames as well as acquire the frame permutation and missing invariant ability to support more flexible retrieval manners. Comprehensive experiments on two challenging video retrieval datasets namely FIVR-200K and SVD verify the effectiveness of our proposed SVRTN method which achieves the best performance of video retrieval on accuracy and efficiency.
