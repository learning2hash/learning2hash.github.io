---
layout: publication
title: Stochastic Prototype Embeddings
authors: Tyler R. Scott, Karl Ridgeway, Michael C. Mozer
conference: Arxiv
year: 2019
bibkey: scott2019stochastic
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.11702'}]
tags: []
short_authors: Tyler R. Scott, Karl Ridgeway, Michael C. Mozer
---
Supervised deep-embedding methods project inputs of a domain to a
representational space in which same-class instances lie near one another and
different-class instances lie far apart. We propose a probabilistic method that
treats embeddings as random variables. Extending a state-of-the-art
deterministic method, Prototypical Networks (Snell et al., 2017), our approach
supposes the existence of a class prototype around which class instances are
Gaussian distributed. The prototype posterior is a product distribution over
labeled instances, and query instances are classified by marginalizing relative
prototype proximity over embedding uncertainty. We describe an efficient
sampler for approximate inference that allows us to train the model at roughly
the same space and time cost as its deterministic sibling. Incorporating
uncertainty improves performance on few-shot learning and gracefully handles
label noise and out-of-distribution inputs. Compared to the state-of-the-art
stochastic method, Hedged Instance Embeddings (Oh et al., 2019), we achieve
superior large- and open-set classification accuracy. Our method also aligns
class-discriminating features with the axes of the embedding space, yielding an
interpretable, disentangled representation.