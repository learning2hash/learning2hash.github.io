---
layout: publication
title: Efficient Long Sequential User Data Modeling For Click-through Rate Prediction
authors: Qiwei Chen, Yue Xu, Changhua Pei, Shanshan Lv, Tao Zhuang, Junfeng Ge
conference: DLP-KDD 2022
year: 2022
bibkey: chen2022efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.12212'}]
tags: [Evaluation, Efficiency, Datasets, Hashing Methods, KDD, Recommender Systems]
short_authors: Chen et al.
---
Recent studies on Click-Through Rate (CTR) prediction has reached new levels
by modeling longer user behavior sequences. Among others, the two-stage methods
stand out as the state-of-the-art (SOTA) solution for industrial applications.
The two-stage methods first train a retrieval model to truncate the long
behavior sequence beforehand and then use the truncated sequences to train a
CTR model. However, the retrieval model and the CTR model are trained
separately. So the retrieved subsequences in the CTR model is inaccurate, which
degrades the final performance. In this paper, we propose an end-to-end
paradigm to model long behavior sequences, which is able to achieve superior
performance along with remarkable cost-efficiency compared to existing models.
Our contribution is three-fold: First, we propose a hashing-based efficient
target attention (TA) network named ETA-Net to enable end-to-end user behavior
retrieval based on low-cost bit-wise operations. The proposed ETA-Net can
reduce the complexity of standard TA by orders of magnitude for sequential data
modeling. Second, we propose a general system architecture as one viable
solution to deploy ETA-Net on industrial systems. Particularly, ETA-Net has
been deployed on the recommender system of Taobao, and brought 1.8% lift on CTR
and 3.1% lift on Gross Merchandise Value (GMV) compared to the SOTA two-stage
methods. Third, we conduct extensive experiments on both offline datasets and
online A/B test. The results verify that the proposed model outperforms
existing CTR models considerably, in terms of both CTR prediction performance
and online cost-efficiency. ETA-Net now serves the main traffic of Taobao,
delivering services to hundreds of millions of users towards billions of items
every day.