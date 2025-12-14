---
layout: publication
title: 'Cort: Complementary Rankings From Transformers'
authors: Marco Wrzalik, Dirk Krechel
conference: 'Proceedings of the 2021 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2020
bibkey: wrzalik2020cort
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.10252'}]
tags: [NAACL, Evaluation, Similarity Search, Efficiency, Datasets, ACL]
short_authors: Marco Wrzalik, Dirk Krechel
---
Many recent approaches towards neural information retrieval mitigate their
computational costs by using a multi-stage ranking pipeline. In the first
stage, a number of potentially relevant candidates are retrieved using an
efficient retrieval model such as BM25. Although BM25 has proven decent
performance as a first-stage ranker, it tends to miss relevant passages. In
this context we propose CoRT, a simple neural first-stage ranking model that
leverages contextual representations from pretrained language models such as
BERT to complement term-based ranking functions while causing no significant
delay at query time. Using the MS MARCO dataset, we show that CoRT
significantly increases the candidate recall by complementing BM25 with missing
candidates. Consequently, we find subsequent re-rankers achieve superior
results with less candidates. We further demonstrate that passage retrieval
using CoRT can be realized with surprisingly low latencies.