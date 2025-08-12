---
layout: publication
title: 'Word Mover''s Embedding: From Word2vec To Document Embedding'
authors: Lingfei Wu, Ian E. H. Yen, Kun Xu, Fangli Xu, Avinash Balakrishnan, Pin-Yu
  Chen, Pradeep Ravikumar, Michael J. Witbrock
conference: Arxiv
year: 2018
bibkey: wu2018word
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.01713'}]
tags: []
short_authors: Wu et al.
---
While the celebrated Word2Vec technique yields semantically rich
representations for individual words, there has been relatively less success in
extending to generate unsupervised sentences or documents embeddings. Recent
work has demonstrated that a distance measure between documents called
*Word Mover's Distance* (WMD) that aligns semantically similar words,
yields unprecedented KNN classification accuracy. However, WMD is expensive to
compute, and it is hard to extend its use beyond a KNN classifier. In this
paper, we propose the *Word Mover's Embedding * (WME), a novel approach to
building an unsupervised document (sentence) embedding from pre-trained word
embeddings. In our experiments on 9 benchmark text classification datasets and
22 textual similarity tasks, the proposed technique consistently matches or
outperforms state-of-the-art techniques, with significantly higher accuracy on
problems of short length.