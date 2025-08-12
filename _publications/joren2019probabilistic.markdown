---
layout: publication
title: Probabilistic Bias Mitigation In Word Embeddings
authors: Hailey Joren, David Alvarez-Melis
conference: Arxiv
year: 2019
bibkey: joren2019probabilistic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.14497'}]
tags: []
short_authors: Hailey Joren, David Alvarez-Melis
---
It has been shown that word embeddings derived from large corpora tend to
incorporate biases present in their training data. Various methods for
mitigating these biases have been proposed, but recent work has demonstrated
that these methods hide but fail to truly remove the biases, which can still be
observed in word nearest-neighbor statistics. In this work we propose a
probabilistic view of word embedding bias. We leverage this framework to
present a novel method for mitigating bias which relies on probabilistic
observations to yield a more robust bias mitigation algorithm. We demonstrate
that this method effectively reduces bias according to three separate measures
of bias while maintaining embedding quality across various popular benchmark
semantic tasks