---
layout: publication
title: Guided Similarity Separation For Image Retrieval
authors: Chundi Liu, Guangwei Yu, Maksims Volkovs, Cheng Chang, Himanshu Rai, Junwei Ma, Satya Krishna Gorti
conference: "Neural Information Processing Systems"
year: 2019
bibkey: liu2019guided
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2019/hash/7504adad8bb96320eb3afdd4df6e1f60-Abstract.html"}
  - {name: "Code", url: "https://github.com/layer6ai-labs/GSS"}
tags: ['Graph', 'Has Code', 'Image Retrieval', 'NEURIPS', 'Unsupervised']
---
Despite recent progress in computer vision image retrieval remains a challenging open problem. Numerous variations such as view angle lighting and occlusion make it difficult to design models that are both robust and efficient. Many leading methods traverse the nearest neighbor graph to exploit higher order neighbor information and uncover the highly complex underlying manifold. In this work we propose a different approach where we leverage graph convolutional networks to directly encode neighbor information into image descriptors. We further leverage ideas from clustering and manifold learning and introduce an unsupervised loss based on pairwise separation of image similarities. Empirically we demonstrate that our model is able to successfully learn a new descriptor space that significantly improves retrieval accuracy while still allowing efficient inner product inference. Experiments on five public benchmarks show highly competitive performance with up to 2437; relative improvement in mAP over leading baselines. Full code for this work is available here https://github.com/layer6ai-labs/GSS.
