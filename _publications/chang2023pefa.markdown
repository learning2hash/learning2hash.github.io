---
layout: publication
title: 'PEFA: Parameter-free Adapters For Large-scale Embedding-based Retrieval Models'
authors: Wei-Cheng Chang, Jyun-Yu Jiang, Jiong Zhang, Mutasem Al-Darabsah, Choon Hui
  Teo, Cho-Jui Hsieh, Hsiang-Fu Yu, S. V. N. Vishwanathan
conference: Proceedings of the 17th ACM International Conference on Web Search and
  Data Mining
year: 2023
bibkey: chang2023pefa
citations: 1
additional_links: [{name: Code, url: 'https://github.com/amzn/pecos/tree/mainline/examples/pefa-wsdm24'},
  {name: Paper, url: 'https://arxiv.org/abs/2312.02429'}]
tags: [Evaluation, Vector Indexing, Scalability, Tools & Libraries, Text Retrieval]
short_authors: Chang et al.
---
Embedding-based Retrieval Models (ERMs) have emerged as a promising framework
for large-scale text retrieval problems due to powerful large language models.
Nevertheless, fine-tuning ERMs to reach state-of-the-art results can be
expensive due to the extreme scale of data as well as the complexity of
multi-stages pipelines (e.g., pre-training, fine-tuning, distillation). In this
work, we propose the PEFA framework, namely ParamEter-Free Adapters, for fast
tuning of ERMs without any backward pass in the optimization. At index building
stage, PEFA equips the ERM with a non-parametric k-nearest neighbor (kNN)
component. At inference stage, PEFA performs a convex combination of two
scoring functions, one from the ERM and the other from the kNN. Based on the
neighborhood definition, PEFA framework induces two realizations, namely
PEFA-XL (i.e., extra large) using double ANN indices and PEFA-XS (i.e., extra
small) using a single ANN index. Empirically, PEFA achieves significant
improvement on two retrieval applications. For document retrieval, regarding
Recall@100 metric, PEFA improves not only pre-trained ERMs on Trivia-QA by an
average of 13.2%, but also fine-tuned ERMs on NQ-320K by an average of 5.5%,
respectively. For product search, PEFA improves the Recall@100 of the
fine-tuned ERMs by an average of 5.3% and 14.5%, for PEFA-XS and PEFA-XL,
respectively. Our code is available at
https://github.com/amzn/pecos/tree/mainline/examples/pefa-wsdm24.