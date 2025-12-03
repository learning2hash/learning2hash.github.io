---
layout: publication
title: 'Fifty: Large-scale File Fragment Type Identification Using Neural Networks'
authors: Govind Mittal, Pawel Korus, Nasir Memon
conference: Arxiv
year: 2019
bibkey: mittal2019fifty
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.06148'}]
tags: ["Datasets", "Scalability"]
short_authors: Govind Mittal, Pawel Korus, Nasir Memon
---
We present FiFTy, a modern file type identification tool for memory forensics
and data carving. In contrast to previous approaches based on hand-crafted
features, we design a compact neural network architecture, which uses a
trainable embedding space, akin to successful natural language processing
models. Our approach dispenses with explicit feature extraction which is a
bottleneck in legacy systems. We evaluate the proposed method on a novel
dataset with 75 file types - the most diverse and balanced dataset reported to
date. FiFTy consistently outperforms all baselines in terms of speed, accuracy
and individual misclassification rates. We achieved an average accuracy of
77.5% with processing speed of approx 38 sec/GB, which is better and more than
an order of magnitude faster than the previous state-of-the-art tool - Sceadan
(69% at 9 min/GB). Our tool and the corresponding dataset are available
publicly online.