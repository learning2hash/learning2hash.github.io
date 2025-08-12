---
layout: publication
title: 'Rerankmatch: Semi-supervised Learning With Semantics-oriented Similarity Representation'
authors: Trung Quang Tran, Mingu Kang, Daeyoung Kim
conference: Arxiv
year: 2021
bibkey: tran2021rerankmatch
citations: 1
additional_links: [{name: Code, url: 'https://github.com/tqtrunghnvn/ReRankMatch'},
  {name: Paper, url: 'https://arxiv.org/abs/2102.06328'}]
tags: []
short_authors: Trung Quang Tran, Mingu Kang, Daeyoung Kim
---
This paper proposes integrating semantics-oriented similarity representation
into RankingMatch, a recently proposed semi-supervised learning method. Our
method, dubbed ReRankMatch, aims to deal with the case in which labeled and
unlabeled data share non-overlapping categories. ReRankMatch encourages the
model to produce the similar image representations for the samples likely
belonging to the same class. We evaluate our method on various datasets such as
CIFAR-10, CIFAR-100, SVHN, STL-10, and Tiny ImageNet. We obtain promising
results (4.21% error rate on CIFAR-10 with 4000 labels, 22.32% error rate on
CIFAR-100 with 10000 labels, and 2.19% error rate on SVHN with 1000 labels)
when the amount of labeled data is sufficient to learn semantics-oriented
similarity representation. The code is made publicly available at
https://github.com/tqtrunghnvn/ReRankMatch.