---
layout: publication
title: A Note On efficient Task-specific Data Valuation For Nearest Neighbor Algorithms
authors: Wang Jiachen T., Jia Ruoxi
conference: "Arxiv"
year: 2023
bibkey: wang2023note
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2304.04258"}
tags: ['ARXIV', 'LSH', 'Supervised']
---
Data valuation is a growing research field that studies the influence of individual data points for machine learning (ML) models. Data Shapley, inspired by cooperative game theory and economics, is an effective method for data valuation. However, it is well-known that the Shapley value (SV) can be computationally expensive. Fortunately, Jia et al. (2019) showed that for K-Nearest Neighbors (KNN) models, the computation of Data Shapley is surprisingly simple and efficient. In this note, we revisit the work of Jia et al. (2019) and propose a more natural and interpretable utility function that better reflects the performance of KNN models. We derive the corresponding calculation procedure for the Data Shapley of KNN classifiers/regressors with the new utility functions. Our new approach, dubbed soft-label KNN-SV, achieves the same time complexity as the original method. We further provide an efficient approximation algorithm for soft-label KNN-SV based on locality sensitive hashing (LSH). Our experimental results demonstrate that Soft-label KNN-SV outperforms the original method on most datasets in the task of mislabeled data detection, making it a better baseline for future work on data valuation.
