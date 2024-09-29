---
layout: publication
title: Efficient Discrete Supervised Hashing For Large45;scale Cross45;modal Retrieval
authors: Yao Tao, Kong Xiangwei, Yan Lianshan, Tang Wenjing, Tian Qi
conference: "Arxiv"
year: 2019
bibkey: yao2019efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1905.01304"}
tags: ['ARXIV', 'Quantisation', 'Supervised']
---
Supervised cross45;modal hashing has gained increasing research interest on large45;scale retrieval task owning to its satisfactory performance and efficiency. However it still has some challenging issues to be further studied 1) most of them fail to well preserve the semantic correlations in hash codes because of the large heterogenous gap; 2) most of them relax the discrete constraint on hash codes leading to large quantization error and consequent low performance; 3) most of them suffer from relatively high memory cost and computational complexity during training procedure which makes them unscalable. In this paper to address above issues we propose a supervised cross45;modal hashing method based on matrix factorization dubbed Efficient Discrete Supervised Hashing (EDSH). Specifically collective matrix factorization on heterogenous features and semantic embedding with class labels are seamlessly integrated to learn hash codes. Therefore the feature based similarities and semantic correlations can be both preserved in hash codes which makes the learned hash codes more discriminative. Then an efficient discrete optimal algorithm is proposed to handle the scalable issue. Instead of learning hash codes bit45;by45;bit hash codes matrix can be obtained directly which is more efficient. Extensive experimental results on three public real45;world datasets demonstrate that EDSH produces a superior performance in both accuracy and scalability over some existing cross45;modal hashing methods.
