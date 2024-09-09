---
    layout: publication
    title: "Instance-weighted Central Similarity for Multi-label Image Retrieval"
    authors: Zhang Zhiwei, Peng Hanyu
    conference: Arxiv
    year: 2021
    bibkey: zhang2021instance
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2108.05274"}
    tags: ['ARXIV', 'Image Retrieval', 'TIP', 'TOM']
    ---
    Deep hashing has been widely applied to large-scale image retrieval by encoding high-dimensional data points into binary codes for efficient retrieval. Compared with pairwise/triplet similarity based hash learning, central similarity based hashing can more efficiently capture the global data distribution. For multi-label image retrieval, however, previous methods only use multiple hash centers with equal weights to generate one centroid as the learning target, which ignores the relationship between the weights of hash centers and the proportion of instance regions in the image. To address the above issue, we propose a two-step alternative optimization approach, Instance-weighted Central Similarity (ICS), to automatically learn the center weight corresponding to a hash code. Firstly, we apply the maximum entropy regularizer to prevent one hash center from dominating the loss function, and compute the center weights via projection gradient descent. Secondly, we update neural network parameters by standard back-propagation with fixed center weights. More importantly, the learned center weights can well reflect the proportion of foreground instances in the image. Our method achieves the state-of-the-art performance on the image retrieval benchmarks, and especially improves the mAP by 1.6%-6.4% on the MS COCO dataset.