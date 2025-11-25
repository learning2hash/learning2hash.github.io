---
layout: publication
title: Context-aware Sentence/passage Term Importance Estimation For First Stage Retrieval
authors: Zhuyun Dai, Jamie Callan
conference: Arxiv
year: 2019
bibkey: dai2019context
citations: 117
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.10687'}]
tags: ["Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Zhuyun Dai, Jamie Callan
---
Term frequency is a common method for identifying the importance of a term in
a query or document. But it is a weak signal, especially when the frequency
distribution is flat, such as in long queries or short documents where the text
is of sentence/passage-length. This paper proposes a Deep Contextualized Term
Weighting framework that learns to map BERT's contextualized text
representations to context-aware term weights for sentences and passages. When
applied to passages, DeepCT-Index produces term weights that can be stored in
an ordinary inverted index for passage retrieval. When applied to query text,
DeepCT-Query generates a weighted bag-of-words query. Both types of term weight
can be used directly by typical first-stage retrieval algorithms. This is novel
because most deep neural network based ranking models have higher computational
costs, and thus are restricted to later-stage rankers. Experiments on four
datasets demonstrate that DeepCT's deep contextualized text understanding
greatly improves the accuracy of first-stage retrieval algorithms.