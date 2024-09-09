---
    layout: publication
    title: "Hyperbolic Hierarchical Contrastive Hashing"
    authors: Wei Rukai, Liu Yu, Song Jingkuan, Xie Yanzhao, Zhou Ke
    conference: Transaction on Image Processing
    year: 2022
    bibkey: wei2022hyperbolic
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2212.08904"}
    tags: ['Supervised', 'Unsupervised']
    ---
    Hierarchical semantic structures, naturally existing in real-world datasets, can assist in capturing the latent distribution of data to learn robust hash codes for retrieval systems. Although hierarchical semantic structures can be simply expressed by integrating semantically relevant data into a high-level taxon with coarser-grained semantics, the construction, embedding, and exploitation of the structures remain tricky for unsupervised hash learning. To tackle these problems, we propose a novel unsupervised hashing method named Hyperbolic Hierarchical Contrastive Hashing (HHCH). We propose to embed continuous hash codes into hyperbolic space for accurate semantic expression since embedding hierarchies in hyperbolic space generates less distortion than in hyper-sphere space and Euclidean space. In addition, we extend the K-Means algorithm to hyperbolic space and perform the proposed hierarchical hyperbolic K-Means algorithm to construct hierarchical semantic structures adaptively. To exploit the hierarchical semantic structures in hyperbolic space, we designed the hierarchical contrastive learning algorithm, including hierarchical instance-wise and hierarchical prototype-wise contrastive learning. Extensive experiments on four benchmark datasets demonstrate that the proposed method outperforms the state-of-the-art unsupervised hashing methods. Codes will be released.