---
layout: publication
title: Using \(k\)-way Co-occurrences For Learning Word Embeddings
authors: Danushka Bollegala, Yuichi Yoshida, Ken-ichi Kawarabayashi
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2018
bibkey: bollegala2017using
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.01199'}]
tags: ["AAAI"]
short_authors: Danushka Bollegala, Yuichi Yoshida, Ken-ichi Kawarabayashi
---
Co-occurrences between two words provide useful insights into the semantics
of those words. Consequently, numerous prior work on word embedding learning
have used co-occurrences between two words as the training signal for learning
word embeddings. However, in natural language texts it is common for multiple
words to be related and co-occurring in the same context. We extend the notion
of co-occurrences to cover \\(k(\geq\!\!2)\\)-way co-occurrences among a set of
\\(k\\)-words. Specifically, we prove a theoretical relationship between the joint
probability of \\(k(\geq\!\!2)\\) words, and the sum of \\(ℓ₂\\) norms of their
embeddings. Next, we propose a learning objective motivated by our theoretical
result that utilises \\(k\\)-way co-occurrences for learning word embeddings. Our
experimental results show that the derived theoretical relationship does indeed
hold empirically, and despite data sparsity, for some smaller \\(k\\) values,
\\(k\\)-way embeddings perform comparably or better than \\(2\\)-way embeddings in a
range of tasks.