---
layout: publication
title: Learning To Rank Binary Codes
authors: Jie Feng, Wei Liu, Yan Wang
conference: Arxiv
year: 2014
citations: 1
bibkey: feng2014learning
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1410.5524'}]
tags: [Applications, Tools and Libraries, ANN Search, Evaluation Metrics, Hashing
    Methods]
---
Binary codes have been widely used in vision problems as a compact feature
representation to achieve both space and time advantages. Various methods have
been proposed to learn data-dependent hash functions which map a feature vector
to a binary code. However, considerable data information is inevitably lost
during the binarization step which also causes ambiguity in measuring sample
similarity using Hamming distance. Besides, the learned hash functions cannot
be changed after training, which makes them incapable of adapting to new data
outside the training data set. To address both issues, in this paper we propose
a flexible bitwise weight learning framework based on the binary codes obtained
by state-of-the-art hashing methods, and incorporate the learned weights into
the weighted Hamming distance computation. We then formulate the proposed
framework as a ranking problem and leverage the Ranking SVM model to offline
tackle the weight learning. The framework is further extended to an online mode
which updates the weights at each time new data comes, thereby making it
scalable to large and dynamic data sets. Extensive experimental results
demonstrate significant performance gains of using binary codes with bitwise
weighting in image retrieval tasks. It is appealing that the online weight
learning leads to comparable accuracy with its offline counterpart, which thus
makes our approach practical for realistic applications.