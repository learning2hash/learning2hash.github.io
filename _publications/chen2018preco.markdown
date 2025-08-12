---
layout: publication
title: 'Preco: A Large-scale Dataset In Preschool Vocabulary For Coreference Resolution'
authors: Hong Chen, Zhenhua Fan, Hao Lu, Alan L. Yuille, Shu Rong
conference: Proceedings of the 2018 Conference on Empirical Methods in Natural Language
  Processing
year: 2018
bibkey: chen2018preco
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09807'}]
tags: ["Datasets", "EMNLP"]
short_authors: Chen et al.
---
We introduce PreCo, a large-scale English dataset for coreference resolution.
The dataset is designed to embody the core challenges in coreference, such as
entity representation, by alleviating the challenge of low overlap between
training and test sets and enabling separated analysis of mention detection and
mention clustering. To strengthen the training-test overlap, we collect a large
corpus of about 38K documents and 12.4M words which are mostly from the
vocabulary of English-speaking preschoolers. Experiments show that with higher
training-test overlap, error analysis on PreCo is more efficient than the one
on OntoNotes, a popular existing dataset. Furthermore, we annotate singleton
mentions making it possible for the first time to quantify the influence that a
mention detector makes on coreference resolution performance. The dataset is
freely available at https://preschool-lab.github.io/PreCo/.