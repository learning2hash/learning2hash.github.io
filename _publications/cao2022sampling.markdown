---
layout: publication
title: Sampling Is All You Need On Modeling Long-term User Behaviors For CTR Prediction
authors: Yue Cao, Xiaojiang Zhou, Jiaqi Feng, Peihao Huang, Yao Xiao, Dayao Chen,
  Sheng Chen
conference: Proceedings of the 31st ACM International Conference on Information &amp;
  Knowledge Management
year: 2022
bibkey: cao2022sampling
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.10249'}]
tags: ["Efficiency", "Hashing Methods", "Recommender Systems"]
short_authors: Cao et al.
---
Rich user behavior data has been proven to be of great value for
Click-Through Rate (CTR) prediction applications, especially in industrial
recommender, search, or advertising systems. However, it's non-trivial for
real-world systems to make full use of long-term user behaviors due to the
strict requirements of online serving time. Most previous works adopt the
retrieval-based strategy, where a small number of user behaviors are retrieved
first for subsequent attention. However, the retrieval-based methods are
sub-optimal and would cause more or less information losses, and it's difficult
to balance the effectiveness and efficiency of the retrieval algorithm.
  In this paper, we propose SDIM (Sampling-based Deep Interest Modeling), a
simple yet effective sampling-based end-to-end approach for modeling long-term
user behaviors. We sample from multiple hash functions to generate hash
signatures of the candidate item and each item in the user behavior sequence,
and obtain the user interest by directly gathering behavior items associated
with the candidate item with the same hash signature. We show theoretically and
experimentally that the proposed method performs on par with standard
attention-based models on modeling long-term user behaviors, while being
sizable times faster. We also introduce the deployment of SDIM in our system.
Specifically, we decouple the behavior sequence hashing, which is the most
time-consuming part, from the CTR model by designing a separate module named
BSE (behavior Sequence Encoding). BSE is latency-free for the CTR server,
enabling us to model extremely long user behaviors. Both offline and online
experiments are conducted to demonstrate the effectiveness of SDIM. SDIM now
has been deployed online in the search system of Meituan APP.