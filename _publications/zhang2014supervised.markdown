---
layout: publication
title: Supervised Hashing with Latent Factor Models
authors: Zhang et al.
conference: Proceedings of the 37th international ACM SIGIR conference on Research
  &amp; development in information retrieval
year: 2014
bibkey: zhang2014supervised
citations: 285
additional_links: [{name: Paper, url: 'https://cs.nju.edu.cn/lwj/paper/SIGIR14_LFH.pdf'}]
tags: ["Hashing Methods", "Neural Hashing", "SIGIR", "Supervised"]
---
Due to its low storage cost and fast query speed, hashing
has been widely adopted for approximate nearest neighbor
search in large-scale datasets. Traditional hashing methods
try to learn the hash codes in an unsupervised way where
the metric (Euclidean) structure of the training data is preserved.
Very recently, supervised hashing methods, which
try to preserve the semantic structure constructed from the
semantic labels of the training points, have exhibited higher
accuracy than unsupervised methods. In this paper, we
propose a novel supervised hashing method, called latent
factor hashing (LFH), to learn similarity-preserving binary
codes based on latent factor models. An algorithm with
convergence guarantee is proposed to learn the parameters
of LFH. Furthermore, a linear-time variant with stochastic
learning is proposed for training LFH on large-scale datasets.
Experimental results on two large datasets with semantic
labels show that LFH can achieve superior accuracy than
state-of-the-art methods with comparable training time.