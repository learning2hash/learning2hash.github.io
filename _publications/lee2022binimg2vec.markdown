---
layout: publication
title: 'Binimg2vec: Augmenting Malware Binary Image Classification With Data2vec'
authors: Joon Sern Lee, Kai Keng Tay, Zong Fu Chua
conference: 2022 1st International Conference on AI in Cybersecurity (ICAIC)
year: 2022
bibkey: lee2022binimg2vec
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.00782'}]
tags: ["Tools & Libraries"]
short_authors: Joon Sern Lee, Kai Keng Tay, Zong Fu Chua
---
Rapid digitalisation spurred by the Covid-19 pandemic has resulted in more
cyber crime. Malware-as-a-service is now a booming business for cyber
criminals. With the surge in malware activities, it is vital for cyber
defenders to understand more about the malware samples they have at hand as
such information can greatly influence their next course of actions during a
breach. Recently, researchers have shown how malware family classification can
be done by first converting malware binaries into grayscale images and then
passing them through neural networks for classification. However, most work
focus on studying the impact of different neural network architectures on
classification performance. In the last year, researchers have shown that
augmenting supervised learning with self-supervised learning can improve
performance. Even more recently, Data2Vec was proposed as a modality agnostic
self-supervised framework to train neural networks. In this paper, we present
BinImg2Vec, a framework of training malware binary image classifiers that
incorporates both self-supervised learning and supervised learning to produce a
model that consistently outperforms one trained only via supervised learning.
We were able to achieve a 4% improvement in classification performance and a
0.5% reduction in performance variance over multiple runs. We also show how our
framework produces embeddings that can be well clustered, facilitating model
explanability.