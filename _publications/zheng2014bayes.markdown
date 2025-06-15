---
layout: publication
title: 'Bayes Merging Of Multiple Vocabularies For Scalable Image Retrieval'
authors: Liang Zheng, Shengjin Wang, Wengang Zhou, Qi Tian
conference: "Arxiv"
year: 2014
citations: 57
bibkey: zheng2014bayes
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1403.0284'}
tags: ['Applications', 'Evaluation Metrics', 'Quantization and Compression', 'Tools and Libraries', 'Quantization']
---
The Bag-of-Words (BoW) representation is well applied to recent
state-of-the-art image retrieval works. Typically, multiple vocabularies are
generated to correct quantization artifacts and improve recall. However, this
routine is corrupted by vocabulary correlation, i.e., overlapping among
different vocabularies. Vocabulary correlation leads to an over-counting of the
indexed features in the overlapped area, or the intersection set, thus
compromising the retrieval accuracy. In order to address the correlation
problem while preserve the benefit of high recall, this paper proposes a Bayes
merging approach to down-weight the indexed features in the intersection set.
Through explicitly modeling the correlation problem in a probabilistic view, a
joint similarity on both image- and feature-level is estimated for the indexed
features in the intersection set.
  We evaluate our method through extensive experiments on three benchmark
datasets. Albeit simple, Bayes merging can be well applied in various merging
tasks, and consistently improves the baselines on multi-vocabulary merging.
Moreover, Bayes merging is efficient in terms of both time and memory cost, and
yields competitive performance compared with the state-of-the-art methods.
