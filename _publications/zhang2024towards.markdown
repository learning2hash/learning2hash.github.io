---
layout: publication
title: Towards Scalable Semantic Representation For Recommendation
authors: Taolin Zhang, Junwei Pan, Jinpeng Wang, Yaohua Zha, Tao Dai, Bin Chen, Ruisheng
  Luo, Xiaoxiang Deng, Yuan Wang, Ming Yue, Jie Jiang, Shu-tao Xia
conference: Arxiv
year: 2024
bibkey: zhang2024towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.09560'}]
tags: ["Recommender Systems", "Scalability"]
short_authors: Zhang et al.
---
With recent advances in large language models (LLMs), there has been emerging
numbers of research in developing Semantic IDs based on LLMs to enhance the
performance of recommendation systems. However, the dimension of these
embeddings needs to match that of the ID embedding in recommendation, which is
usually much smaller than the original length. Such dimension compression
results in inevitable losses in discriminability and dimension robustness of
the LLM embeddings, which motivates us to scale up the semantic representation.
In this paper, we propose Mixture-of-Codes, which first constructs multiple
independent codebooks for LLM representation in the indexing stage, and then
utilizes the Semantic Representation along with a fusion module for the
downstream recommendation stage. Extensive analysis and experiments demonstrate
that our method achieves superior discriminability and dimension robustness
scalability, leading to the best scale-up performance in recommendations.