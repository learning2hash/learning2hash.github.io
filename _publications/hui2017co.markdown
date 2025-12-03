---
layout: publication
title: 'Co-pacrr: A Context-aware Neural IR Model For Ad-hoc Retrieval'
authors: Kai Hui, Andrew Yates, Klaus Berberich, Gerard de Melo
conference: Arxiv
year: 2017
bibkey: hui2017co
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.10192'}]
tags: ["Evaluation"]
short_authors: Hui et al.
---
Neural IR models, such as DRMM and PACRR, have achieved strong results by
successfully capturing relevance matching signals. We argue that the context of
these matching signals is also important. Intuitively, when extracting,
modeling, and combining matching signals, one would like to consider the
surrounding text (local context) as well as other signals from the same
document that can contribute to the overall relevance score. In this work, we
highlight three potential shortcomings caused by not considering context
information and propose three neural ingredients to address them: a
disambiguation component, cascade k-max pooling, and a shuffling combination
layer. Incorporating these components into the PACRR model yields Co-PACRR, a
novel context-aware neural IR model. Extensive comparisons with established
models on Trec Web Track data confirm that the proposed model can achieve
superior search results. In addition, an ablation analysis is conducted to gain
insights into the impact of and interactions between different components. We
release our code to enable future comparisons.