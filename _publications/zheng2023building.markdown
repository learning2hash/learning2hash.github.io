---
layout: publication
title: Building K-anonymous User Cohorts With\\ Consecutive Consistent Weighted Sampling
  (CCWS)
authors: Xinyi Zheng, Weijie Zhao, Xiaoyun Li, Ping Li
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: zheng2023building
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.13677'}]
tags: ["Datasets", "Hashing Methods", "SIGIR"]
short_authors: Zheng et al.
---
To retrieve personalized campaigns and creatives while protecting user
privacy, digital advertising is shifting from member-based identity to
cohort-based identity. Under such identity regime, an accurate and efficient
cohort building algorithm is desired to group users with similar
characteristics. In this paper, we propose a scalable \(K\)-anonymous cohort
building algorithm called \{\em consecutive consistent weighted sampling\}
(CCWS). The proposed method combines the spirit of the (\(p\)-powered) consistent
weighted sampling and hierarchical clustering, so that the \(K\)-anonymity is
ensured by enforcing a lower bound on the size of cohorts. Evaluations on a
LinkedIn dataset consisting of \(>70\)M users and ads campaigns demonstrate that
CCWS achieves substantial improvements over several hashing-based methods
including sign random projections (SignRP), minwise hashing (MinHash), as well
as the vanilla CWS.