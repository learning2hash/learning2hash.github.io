---
    layout: publication
    title: "Unfolded Self-Reconstruction LSH: Towards Machine Unlearning in Approximate Nearest Neighbour Search"
    authors: Tan Kim Yong, Lyu Yueming, Ong Yew Soon, Tsang Ivor W.
    conference: Arxiv
    year: 2023
    bibkey: tan2023unfolded
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2304.02350"}
    tags: ['Arxiv', 'LSH']
    ---
    {% raw %}
    Approximate nearest neighbour (ANN) search is an essential component of search engines, recommendation systems, etc. Many recent works focus on learning-based data-distribution-dependent hashing and achieve good retrieval performance. However, due to increasing demand for users' privacy and security, we often need to remove users' data information from Machine Learning (ML) models to satisfy specific privacy and security requirements. This need requires the ANN search algorithm to support fast online data deletion and insertion. Current learning-based hashing methods need retraining the hash function, which is prohibitable due to the vast time-cost of large-scale data. To address this problem, we propose a novel data-dependent hashing method named unfolded self-reconstruction locality-sensitive hashing (USR-LSH). Our USR-LSH unfolded the optimization update for instance-wise data reconstruction, which is better for preserving data information than data-independent LSH. Moreover, our USR-LSH supports fast online data deletion and insertion without retraining. To the best of our knowledge, we are the first to address the machine unlearning of retrieval problems. Empirically, we demonstrate that USR-LSH outperforms the state-of-the-art data-distribution-independent LSH in ANN tasks in terms of precision and recall. We also show that USR-LSH has significantly faster data deletion and insertion time than learning-based data-dependent hashing.
    {% endraw %}