---
layout: publication
title: Boosting The Performance Of Transformer Architectures For Semantic Textual
  Similarity
authors: "Ivan Rep, Vladimir \u010Ceperi\u0107"
conference: Arxiv
year: 2023
bibkey: rep2023boosting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.00708'}]
tags: []
short_authors: "Ivan Rep, Vladimir \u010Ceperi\u0107"
---
Semantic textual similarity is the task of estimating the similarity between
the meaning of two texts. In this paper, we fine-tune transformer architectures
for semantic textual similarity on the Semantic Textual Similarity Benchmark by
tuning the model partially and then end-to-end. We experiment with BERT,
RoBERTa, and DeBERTaV3 cross-encoders by approaching the problem as a binary
classification task or a regression task. We combine the outputs of the
transformer models and use handmade features as inputs for boosting algorithms.
Due to worse test set results coupled with improvements on the validation set,
we experiment with different dataset splits to further investigate this
occurrence. We also provide an error analysis, focused on the edges of the
prediction range.