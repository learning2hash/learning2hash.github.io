---
    layout: publication
    title: "Twitter100k: A Real-world Dataset for Weakly Supervised Cross-Media Retrieval"
    authors: Hu Yuting, Zheng Liang, Yang Yi, Huang Yongfeng
    conference: Arxiv
    year: 2017
    bibkey: hu2017twitter100k
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1703.06618"}
    tags: ['ARXIV', 'GAN', 'Supervised', 'Weakly Supervised']
    ---
    This paper contributes a new large-scale dataset for weakly supervised cross-media retrieval, named Twitter100k. Current datasets, such as Wikipedia, NUS Wide and Flickr30k, have two major limitations. First, these datasets are lacking in content diversity, i.e., only some pre-defined classes are covered. Second, texts in these datasets are written in well-organized language, leading to inconsistency with realistic applications. To overcome these drawbacks, the proposed Twitter100k dataset is characterized by two aspects: 1) it has 100,000 image-text pairs randomly crawled from Twitter and thus has no constraint in the image categories; 2) text in Twitter100k is written in informal language by the users. Since strongly supervised methods leverage the class labels that may be missing in practice, this paper focuses on weakly supervised learning for cross-media retrieval, in which only text-image pairs are exploited during training. We extensively benchmark the performance of four subspace learning methods and three variants of the Correspondence AutoEncoder, along with various text features on Wikipedia, Flickr30k and Twitter100k. Novel insights are provided. As a minor contribution, inspired by the characteristic of Twitter100k, we propose an OCR-based cross-media retrieval method. In experiment, we show that the proposed OCR-based method improves the baseline performance.