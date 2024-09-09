---
    layout: publication
    title: "On the Evaluation Metric for Hashing"
    authors: Jiang Qing-Yuan, Li Ming-Wei, Li Wu-Jun
    conference: Arxiv
    year: 2019
    bibkey: jiang2019on
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1905.10951"}
    tags: ['ARXIV']
    ---
    Due to its low storage cost and fast query speed, hashing has been widely used for large-scale approximate nearest neighbor (ANN) search. Bucket search, also called hash lookup, can achieve fast query speed with a sub-linear time cost based on the inverted index table constructed from hash codes. Many metrics have been adopted to evaluate hashing algorithms. However, all existing metrics are improper to evaluate the hash codes for bucket search. On one hand, all existing metrics ignore the retrieval time cost which is an important factor reflecting the performance of search. On the other hand, some of them, such as mean average precision (MAP), suffer from the uncertainty problem as the ranked list is based on integer-valued Hamming distance, and are insensitive to Hamming radius as these metrics only depend on relative Hamming distance. Other metrics, such as precision at Hamming radius R, fail to evaluate global performance as these metrics only depend on one specific Hamming radius. In this paper, we first point out the problems of existing metrics which have been ignored by the hashing community, and then propose a novel evaluation metric called radius aware mean average precision (RAMAP) to evaluate hash codes for bucket search. Furthermore, two coding strategies are also proposed to qualitatively show the problems of existing metrics. Experiments demonstrate that our proposed RAMAP can provide more proper evaluation than existing metrics.