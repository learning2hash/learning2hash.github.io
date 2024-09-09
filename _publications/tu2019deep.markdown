---
    layout: publication
    title: "Deep Cross-Modal Hashing with Hashing Functions and Unified Hash Codes Jointly Learning"
    authors: Tu Rong-Cheng, Mao Xian-Ling, Ma Bing, Hu Yong, Yan Tan, Wei Wei, Huang Heyan
    conference: Arxiv
    year: 2019
    bibkey: tu2019deep
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1907.12490"}
    tags: ['ARXIV', 'Cross Modal']
    ---
    Due to their high retrieval efficiency and low storage cost, cross-modal hashing methods have attracted considerable attention. Generally, compared with shallow cross-modal hashing methods, deep cross-modal hashing methods can achieve a more satisfactory performance by integrating feature learning and hash codes optimizing into a same framework. However, most existing deep cross-modal hashing methods either cannot learn a unified hash code for the two correlated data-points of different modalities in a database instance or cannot guide the learning of unified hash codes by the feedback of hashing function learning procedure, to enhance the retrieval accuracy. To address the issues above, in this paper, we propose a novel end-to-end Deep Cross-Modal Hashing with Hashing Functions and Unified Hash Codes Jointly Learning (DCHUC). Specifically, by an iterative optimization algorithm, DCHUC jointly learns unified hash codes for image-text pairs in a database and a pair of hash functions for unseen query image-text pairs. With the iterative optimization algorithm, the learned unified hash codes can be used to guide the hashing function learning procedure; Meanwhile, the learned hashing functions can feedback to guide the unified hash codes optimizing procedure. Extensive experiments on three public datasets demonstrate that the proposed method outperforms the state-of-the-art cross-modal hashing methods.