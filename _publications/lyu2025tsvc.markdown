---
layout: publication
title: Tsvc:tripartite Learning With Semantic Variation Consistency For Robust Image-text
  Retrieval
authors: Shuai Lyu, Zijing Tian, Zhonghong Ou, Yifan Zhu, Xiao Zhang, Qiankun Ha,
  Haoran Luo, Meina Song
conference: Proceedings of the AAAI Conference on Artificial Intelligence Vol. 39
  No. 18 pp. 19269-19277 2025
year: 2025
bibkey: lyu2025tsvc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.10935'}]
tags: ["AAAI", "Multimodal Retrieval", "Robustness"]
short_authors: Lyu et al.
---
Cross-modal retrieval maps data under different modality via semantic relevance. Existing approaches implicitly assume that data pairs are well-aligned and ignore the widely existing annotation noise, i.e., noisy correspondence (NC). Consequently, it inevitably causes performance degradation. Despite attempts that employ the co-teaching paradigm with identical architectures to provide distinct data perspectives, the differences between these architectures are primarily stemmed from random initialization. Thus, the model becomes increasingly homogeneous along with the training process. Consequently, the additional information brought by this paradigm is severely limited. In order to resolve this problem, we introduce a Tripartite learning with Semantic Variation Consistency (TSVC) for robust image-text retrieval. We design a tripartite cooperative learning mechanism comprising a Coordinator, a Master, and an Assistant model. The Coordinator distributes data, and the Assistant model supports the Master model's noisy label prediction with diverse data. Moreover, we introduce a soft label estimation method based on mutual information variation, which quantifies the noise in new samples and assigns corresponding soft labels. We also present a new loss function to enhance robustness and optimize training effectiveness. Extensive experiments on three widely used datasets demonstrate that, even at increasing noise ratios, TSVC exhibits significant advantages in retrieval accuracy and maintains stable training performance.