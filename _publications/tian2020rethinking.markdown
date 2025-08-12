---
layout: publication
title: 'Rethinking Few-shot Image Classification: A Good Embedding Is All You Need?'
authors: Yonglong Tian, Yue Wang, Dilip Krishnan, Joshua B. Tenenbaum, Phillip Isola
conference: Lecture Notes in Computer Science
year: 2020
bibkey: tian2020rethinking
citations: 686
additional_links: [{name: Code, url: 'http://github.com/WangYueFt/rfs/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2003.11539'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tian et al.
---
The focus of recent meta-learning research has been on the development of
learning algorithms that can quickly adapt to test time tasks with limited data
and low computational cost. Few-shot learning is widely used as one of the
standard benchmarks in meta-learning. In this work, we show that a simple
baseline: learning a supervised or self-supervised representation on the
meta-training set, followed by training a linear classifier on top of this
representation, outperforms state-of-the-art few-shot learning methods. An
additional boost can be achieved through the use of self-distillation. This
demonstrates that using a good learned embedding model can be more effective
than sophisticated meta-learning algorithms. We believe that our findings
motivate a rethinking of few-shot image classification benchmarks and the
associated role of meta-learning algorithms. Code is available at:
http://github.com/WangYueFt/rfs/.