---
layout: publication
title: Improved Word Sense Disambiguation Using Pre-trained Contextualized Word Representations
authors: Christian Hadiwinoto, Hwee Tou Ng, Wee Chung Gan
conference: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
  Processing and the 9th International Joint Conference on Natural Language Processing
  (EMNLP-IJCNLP)
year: 2019
bibkey: hadiwinoto2019improved
citations: 89
additional_links: [{name: Code, url: 'https://github.com/nusnlp/contextemb-wsd'},
  {name: Paper, url: 'https://arxiv.org/abs/1910.00194'}]
tags: ["EMNLP"]
short_authors: Christian Hadiwinoto, Hwee Tou Ng, Wee Chung Gan
---
Contextualized word representations are able to give different
representations for the same word in different contexts, and they have been
shown to be effective in downstream natural language processing tasks, such as
question answering, named entity recognition, and sentiment analysis. However,
evaluation on word sense disambiguation (WSD) in prior work shows that using
contextualized word representations does not outperform the state-of-the-art
approach that makes use of non-contextualized word embeddings. In this paper,
we explore different strategies of integrating pre-trained contextualized word
representations and our best strategy achieves accuracies exceeding the best
prior published accuracies by significant margins on multiple benchmark WSD
datasets. We make the source code available at
https://github.com/nusnlp/contextemb-wsd.