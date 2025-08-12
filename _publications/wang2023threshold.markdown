---
layout: publication
title: 'Threshold Knn-shapley: A Linear-time And Privacy-friendly Approach To Data
  Valuation'
authors: Jiachen T. Wang, Yuqing Zhu, Yu-Xiang Wang, Ruoxi Jia, Prateek Mittal
conference: Arxiv
year: 2023
bibkey: wang2023threshold
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15709'}]
tags: ["Privacy & Security"]
short_authors: Wang et al.
---
Data valuation aims to quantify the usefulness of individual data sources in
training machine learning (ML) models, and is a critical aspect of data-centric
ML research. However, data valuation faces significant yet frequently
overlooked privacy challenges despite its importance. This paper studies these
challenges with a focus on KNN-Shapley, one of the most practical data
valuation methods nowadays. We first emphasize the inherent privacy risks of
KNN-Shapley, and demonstrate the significant technical difficulties in adapting
KNN-Shapley to accommodate differential privacy (DP). To overcome these
challenges, we introduce TKNN-Shapley, a refined variant of KNN-Shapley that is
privacy-friendly, allowing for straightforward modifications to incorporate DP
guarantee (DP-TKNN-Shapley). We show that DP-TKNN-Shapley has several
advantages and offers a superior privacy-utility tradeoff compared to naively
privatized KNN-Shapley in discerning data quality. Moreover, even non-private
TKNN-Shapley achieves comparable performance as KNN-Shapley. Overall, our
findings suggest that TKNN-Shapley is a promising alternative to KNN-Shapley,
particularly for real-world applications involving sensitive data.