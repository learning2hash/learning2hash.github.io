---
layout: publication
title: Generative Or Contrastive? Phrase Reconstruction For Better Sentence Representation
  Learning
authors: Bohong Wu, Hai Zhao
conference: Arxiv
year: 2022
bibkey: wu2022generative
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.09358'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Bohong Wu, Hai Zhao
---
Though offering amazing contextualized token-level representations, current
pre-trained language models actually take less attention on acquiring
sentence-level representation during its self-supervised pre-training. If
self-supervised learning can be distinguished into two subcategories,
generative and contrastive, then most existing studies show that sentence
representation learning may more benefit from the contrastive methods but not
the generative methods. However, contrastive learning cannot be well compatible
with the common token-level generative self-supervised learning, and does not
guarantee good performance on downstream semantic retrieval tasks. Thus, to
alleviate such obvious inconveniences, we instead propose a novel generative
self-supervised learning objective based on phrase reconstruction. Empirical
studies show that our generative learning may yield powerful enough sentence
representation and achieve performance in Sentence Textual Similarity (STS)
tasks on par with contrastive learning. Further, in terms of unsupervised
setting, our generative method outperforms previous state-of-the-art SimCSE on
the benchmark of downstream semantic retrieval tasks.