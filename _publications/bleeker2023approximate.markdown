---
layout: publication
title: Approximate Nearest Neighbour Phrase Mining For Contextual Speech Recognition
authors: Maurits Bleeker, Pawel Swietojanski, Stefan Braun, Xiaodan Zhuang
conference: INTERSPEECH 2023
year: 2023
bibkey: bleeker2023approximate
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.08862'}]
tags: ["Datasets", "Interspeech", "Scalability", "Similarity Search"]
short_authors: Bleeker et al.
---
This paper presents an extension to train end-to-end Context-Aware
Transformer Transducer ( CATT ) models by using a simple, yet efficient method
of mining hard negative phrases from the latent space of the context encoder.
During training, given a reference query, we mine a number of similar phrases
using approximate nearest neighbour search. These sampled phrases are then used
as negative examples in the context list alongside random and ground truth
contextual information. By including approximate nearest neighbour phrases
(ANN-P) in the context list, we encourage the learned representation to
disambiguate between similar, but not identical, biasing phrases. This improves
biasing accuracy when there are several similar phrases in the biasing
inventory. We carry out experiments in a large-scale data regime obtaining up
to 7% relative word error rate reductions for the contextual portion of test
data. We also extend and evaluate CATT approach in streaming applications.