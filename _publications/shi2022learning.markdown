---
    layout: publication
    title: "Learning Similarity Preserving Binary Codes for Recommender Systems"
    authors: Shi Yang, Chung Young-joo
    conference: Arxiv
    year: 2022
    bibkey: shi2022learning
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2204.08569"}
    tags: ['Survey Paper', 'Cross-Modal', 'Arxiv']
    ---
    Hashing-based Recommender Systems (RSs) are widely studied to provide scalable services. The existing methods for the systems combine three modules to achieve efficiency: feature extraction, interaction modeling, and binarization. In this paper, we study an unexplored module combination for the hashing-based recommender systems, namely Compact Cross-Similarity Recommender (CCSR). Inspired by cross-modal retrieval, CCSR utilizes Maximum a Posteriori similarity instead of matrix factorization and rating reconstruction to model interactions between users and items. We conducted experiments on MovieLens1M, Amazon product review, Ichiba purchase dataset and confirmed CCSR outperformed the existing matrix factorization-based methods. On the Movielens1M dataset, the absolute performance improvements are up to 15.69% in NDCG and 4.29% in Recall. In addition, we extensively studied three binarization modules: $sign$, scaled tanh, and sign-scaled tanh. The result demonstrated that although differentiable scaled tanh is popular in recent discrete feature learning literature, a huge performance drop occurs when outputs of scaled $tanh$ are forced to be binary.