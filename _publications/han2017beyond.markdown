---
layout: publication
title: Beyond SIFT Using Binary Features For Loop Closure Detection
authors: Han et al.
conference: 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2017
bibkey: han2017beyond
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.05833'}]
tags: [IROS]
---
In this paper a binary feature based Loop Closure Detection (LCD) method is
proposed, which for the first time achieves higher precision-recall (PR)
performance compared with state-of-the-art SIFT feature based approaches. The
proposed system originates from our previous work Multi-Index hashing for Loop
closure Detection (MILD), which employs Multi-Index Hashing
(MIH)~\cite\{greene1994multi\} for Approximate Nearest Neighbor (ANN) search of
binary features. As the accuracy of MILD is limited by repeating textures and
inaccurate image similarity measurement, burstiness handling is introduced to
solve this problem and achieves considerable accuracy improvement.
Additionally, a comprehensive theoretical analysis on MIH used in MILD is
conducted to further explore the potentials of hashing methods for ANN search
of binary features from probabilistic perspective. This analysis provides more
freedom on best parameter choosing in MIH for different application scenarios.
Experiments on popular public datasets show that the proposed approach achieved
the highest accuracy compared with state-of-the-art while running at 30Hz for
databases containing thousands of images.