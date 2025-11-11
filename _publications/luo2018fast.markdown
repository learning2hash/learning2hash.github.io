---
layout: publication
title: Fast Scalable Supervised Hashing
authors: Xin Luo, Liqiang Nie, Xiangnan He, Ye Wu, Zhen-Duo Chen, Xin-Shun Xu
conference: 'SIGIR ''18: The 41st International ACM SIGIR conference on research and
  development in Information Retrieval'
year: 2018
bibkey: luo2018fast
citations: 75
additional_links: [{name: Code, url: 'https://lcbwlx.wixsite.com/fssh'}, {name: Paper,
    url: 'http://staff.ustc.edu.cn/~hexn/papers/sigir18-hashing.pdf'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "SIGIR", "Scalability", "Supervised"]
short_authors: Luo et al.
---
Despite significant progress in supervised hashing, there are three
common limitations of existing methods. First, most pioneer methods discretely learn hash codes bit by bit, making the learning
procedure rather time-consuming. Second, to reduce the large complexity of the n by n pairwise similarity matrix, most methods apply
sampling strategies during training, which inevitably results in information loss and suboptimal performance; some recent methods
try to replace the large matrix with a smaller one, but the size is
still large. Third, among the methods that leverage the pairwise
similarity matrix, most of them only encode the semantic label
information in learning the hash codes, failing to fully capture
the characteristics of data. In this paper, we present a novel supervised hashing method, called Fast Scalable Supervised Hashing
(FSSH), which circumvents the use of the large similarity matrix by
introducing a pre-computed intermediate term whose size is independent with the size of training data. Moreover, FSSH can learn
the hash codes with not only the semantic information but also
the features of data. Extensive experiments on three widely used
datasets demonstrate its superiority over several state-of-the-art
methods in both accuracy and scalability. Our experiment codes
are available at: https://lcbwlx.wixsite.com/fssh.