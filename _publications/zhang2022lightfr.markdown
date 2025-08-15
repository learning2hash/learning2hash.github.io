---
layout: publication
title: 'Lightfr: Lightweight Federated Recommendation With Privacy-preserving Matrix
  Factorization'
authors: Honglei Zhang, Fangyuan Luo, Jun Wu, Xiangnan He, Yidong Li
conference: ACM Transactions on Information Systems
year: 2022
bibkey: zhang2022lightfr
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.11743'}]
tags: ["Compact Codes", "Efficiency", "Hashing Methods", "Recommender Systems", "Scalability", "Similarity Search"]
short_authors: Zhang et al.
---
Federated recommender system (FRS), which enables many local devices to train
a shared model jointly without transmitting local raw data, has become a
prevalent recommendation paradigm with privacy-preserving advantages. However,
previous work on FRS performs similarity search via inner product in continuous
embedding space, which causes an efficiency bottleneck when the scale of items
is extremely large. We argue that such a scheme in federated settings ignores
the limited capacities in resource-constrained user devices (i.e., storage
space, computational overhead, and communication bandwidth), and makes it
harder to be deployed in large-scale recommender systems. Besides, it has been
shown that transmitting local gradients in real-valued form between server and
clients may leak users' private information. To this end, we propose a
lightweight federated recommendation framework with privacy-preserving matrix
factorization, LightFR, that is able to generate high-quality binary codes by
exploiting learning to hash technique under federated settings, and thus enjoys
both fast online inference and economic memory consumption. Moreover, we devise
an efficient federated discrete optimization algorithm to collaboratively train
model parameters between the server and clients, which can effectively prevent
real-valued gradient attacks from malicious parties. Through extensive
experiments on four real-world datasets, we show that our LightFR model
outperforms several state-of-the-art FRS methods in terms of recommendation
accuracy, inference efficiency and data privacy.