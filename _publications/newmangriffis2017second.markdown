---
layout: publication
title: Second-order Word Embeddings From Nearest Neighbor Topological Features
authors: Denis Newman-Griffis, Eric Fosler-Lussier
conference: Arxiv
year: 2017
bibkey: newmangriffis2017second
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.08488'}]
tags: [Evaluation, Distance Metric Learning]
short_authors: Denis Newman-Griffis, Eric Fosler-Lussier
---
We introduce second-order vector representations of words, induced from
nearest neighborhood topological features in pre-trained contextual word
embeddings. We then analyze the effects of using second-order embeddings as
input features in two deep natural language processing models, for named entity
recognition and recognizing textual entailment, as well as a linear model for
paraphrase recognition. Surprisingly, we find that nearest neighbor information
alone is sufficient to capture most of the performance benefits derived from
using pre-trained word embeddings. Furthermore, second-order embeddings are
able to handle highly heterogeneous data better than first-order
representations, though at the cost of some specificity. Additionally,
augmenting contextual embeddings with second-order information further improves
model performance in some cases. Due to variance in the random initializations
of word embeddings, utilizing nearest neighbor features from multiple
first-order embedding samples can also contribute to downstream performance
gains. Finally, we identify intriguing characteristics of second-order
embedding spaces for further research, including much higher density and
different semantic interpretations of cosine similarity.