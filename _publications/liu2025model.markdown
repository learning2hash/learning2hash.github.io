---
layout: publication
title: Model Optimization Boosting Framework For Linear Model Hash Learning
authors: Xingbo Liu, Nie, Zhou, Nie, Yin
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: liu2025model
citations: 23
additional_links: [{name: Paper, url: 'https://www.ncbi.nlm.nih.gov/pubmed/32031939'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Tools & Libraries"]
short_authors: Liu et al.
---
Efficient hashing techniques have attracted extensive research interests in both storage and retrieval of high dimensional data, such as images and videos. In existing hashing methods, a linear model is commonly utilized owing to its efficiency. To obtain better accuracy, linear-based hashing methods focus on designing a generalized linear objective function with different constraints or penalty terms that consider the inherent characteristics and neighborhood information of samples. Differing from existing hashing methods, in this study, we propose a self-improvement framework called Model Boost (MoBoost) to improve model parameter optimization for linear-based hashing methods without adding new constraints or penalty terms. In the proposed MoBoost, for a linear-based hashing method, we first repeatedly execute the hashing method to obtain several hash codes to training samples. Then, utilizing two novel fusion strategies, these codes are fused into a single set. We also propose two new criteria to evaluate the goodness of hash bits during the fusion process. Based on the fused set of hash codes, we learn new parameters for the linear hash function that can significantly improve the accuracy. In general, the proposed MoBoost can be adopted by existing linear-based hashing methods, achieving more precise and stable performance compared to the original methods, and adopting the proposed MoBoost will incur negligible time and space costs. To evaluate the proposed MoBoost, we performed extensive experiments on four benchmark datasets, and the results demonstrate superior performance.