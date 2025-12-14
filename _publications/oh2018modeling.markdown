---
layout: publication
title: Modeling Uncertainty With Hedged Instance Embedding
authors: Seong Joon Oh, Kevin Murphy, Jiyan Pan, Joseph Roth, Florian Schroff, Andrew
  Gallagher
conference: Arxiv
year: 2018
bibkey: oh2018modeling
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.00319'}]
tags: [Evaluation, Distance Metric Learning, Datasets]
short_authors: Oh et al.
---
Instance embeddings are an efficient and versatile image representation that
facilitates applications like recognition, verification, retrieval, and
clustering. Many metric learning methods represent the input as a single point
in the embedding space. Often the distance between points is used as a proxy
for match confidence. However, this can fail to represent uncertainty arising
when the input is ambiguous, e.g., due to occlusion or blurriness. This work
addresses this issue and explicitly models the uncertainty by hedging the
location of each input in the embedding space. We introduce the hedged instance
embedding (HIB) in which embeddings are modeled as random variables and the
model is trained under the variational information bottleneck principle.
Empirical results on our new N-digit MNIST dataset show that our method leads
to the desired behavior of hedging its bets across the embedding space upon
encountering ambiguous inputs. This results in improved performance for image
matching and classification tasks, more structure in the learned embedding
space, and an ability to compute a per-exemplar uncertainty measure that is
correlated with downstream performance.