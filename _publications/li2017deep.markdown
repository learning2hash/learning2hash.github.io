---
layout: publication
title: Deep Supervised Discrete Hashing
authors: Qi Li, Zhenan Sun, Ran He, Tieniu Tan
conference: "Neural Information Processing Systems"
year: 2017
bibkey: li2017deep
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2017/hash/e94f63f579e05cb49c05c2d050ead9c0-Abstract.html"}
tags: ['Deep Learning', 'Image Retrieval', 'NEURIPS', 'Supervised']
---
With the rapid growth of image and video data on the web, hashing has been extensively studied for image or video search in recent years. Benefiting from recent advances in deep learning, deep hashing methods have achieved promising results for image retrieval. However, there are some limitations of previous deep hashing methods (e.g., the semantic information is not fully exploited). In this paper, we develop a deep supervised discrete hashing algorithm based on the assumption that the learned binary codes should be ideal for classification. Both the pairwise label information and the classification information are used to learn the hash codes within one stream framework. We constrain the outputs of the last layer to be binary codes directly, which is rarely investigated in deep hashing algorithm. Because of the discrete nature of hash codes, an alternating minimization method is used to optimize the objective function. Experimental results have shown that our method outperforms current state-of-the-art methods on benchmark datasets.
