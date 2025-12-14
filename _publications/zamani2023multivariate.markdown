---
layout: publication
title: Multivariate Representation Learning For Information Retrieval
authors: Hamed Zamani, Michael Bendersky
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: zamani2023multivariate
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.14522'}]
tags: [Tools & Libraries, SIGIR, Efficiency, Datasets]
short_authors: Hamed Zamani, Michael Bendersky
---
Dense retrieval models use bi-encoder network architectures for learning
query and document representations. These representations are often in the form
of a vector representation and their similarities are often computed using the
dot product function. In this paper, we propose a new representation learning
framework for dense retrieval. Instead of learning a vector for each query and
document, our framework learns a multivariate distribution and uses negative
multivariate KL divergence to compute the similarity between distributions. For
simplicity and efficiency reasons, we assume that the distributions are
multivariate normals and then train large language models to produce mean and
variance vectors for these distributions. We provide a theoretical foundation
for the proposed framework and show that it can be seamlessly integrated into
the existing approximate nearest neighbor algorithms to perform retrieval
efficiently. We conduct an extensive suite of experiments on a wide range of
datasets, and demonstrate significant improvements compared to competitive
dense retrieval models.