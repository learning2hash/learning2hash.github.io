---
layout: publication
title: Retrieval-based Text Selection For Addressing Class-imbalanced Data In Classification
authors: Sareh Ahmadi, Aditya Shah, Edward Fox
conference: Arxiv
year: 2023
bibkey: ahmadi2023retrieval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.14899'}]
tags: [Uncategorized]
short_authors: Sareh Ahmadi, Aditya Shah, Edward Fox
---
This paper addresses the problem of selecting of a set of texts for
annotation in text classification using retrieval methods when there are limits
on the number of annotations due to constraints on human resources. An
additional challenge addressed is dealing with binary categories that have a
small number of positive instances, reflecting severe class imbalance. In our
situation, where annotation occurs over a long time period, the selection of
texts to be annotated can be made in batches, with previous annotations guiding
the choice of the next set. To address these challenges, the paper proposes
leveraging SHAP to construct a quality set of queries for Elasticsearch and
semantic search, to try to identify optimal sets of texts for annotation that
will help with class imbalance. The approach is tested on sets of cue texts
describing possible future events, constructed by participants involved in
studies aimed to help with the management of obesity and diabetes. We introduce
an effective method for selecting a small set of texts for annotation and
building high-quality classifiers. We integrate vector search, semantic search,
and machine learning classifiers to yield a good solution. Our experiments
demonstrate improved F1 scores for the minority classes in binary
classification.