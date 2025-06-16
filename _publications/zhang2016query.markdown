---
layout: publication
title: Query-adaptive Image Retrieval By Deep Weighted Hashing
authors: Jian Zhang, Yuxin Peng
conference: Arxiv
year: 2016
citations: 46
bibkey: zhang2016query
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.02541'}]
tags: [Applications, Deep Hashing, Evaluation Metrics, Hashing Methods]
---
Hashing methods have attracted much attention for large scale image
retrieval. Some deep hashing methods have achieved promising results by taking
advantage of the strong representation power of deep networks recently.
However, existing deep hashing methods treat all hash bits equally. On one
hand, a large number of images share the same distance to a query image due to
the discrete Hamming distance, which raises a critical issue of image retrieval
where fine-grained rankings are very important. On the other hand, different
hash bits actually contribute to the image retrieval differently, and treating
them equally greatly affects the retrieval accuracy of image. To address the
above two problems, we propose the query-adaptive deep weighted hashing (QaDWH)
approach, which can perform fine-grained ranking for different queries by
weighted Hamming distance. First, a novel deep hashing network is proposed to
learn the hash codes and corresponding class-wise weights jointly, so that the
learned weights can reflect the importance of different hash bits for different
image classes. Second, a query-adaptive image retrieval method is proposed,
which rapidly generates hash bit weights for different query images by fusing
its semantic probability and the learned class-wise weights. Fine-grained image
retrieval is then performed by the weighted Hamming distance, which can provide
more accurate ranking than the traditional Hamming distance. Experiments on
four widely used datasets show that the proposed approach outperforms eight
state-of-the-art hashing methods.