---
layout: publication
title: Stochastic Learning Of Nonstationary Kernels For Natural Language Modeling
authors: Sahil Garg, Greg Ver Steeg, Aram Galstyan
conference: Arxiv
year: 2018
bibkey: garg2018stochastic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.03911'}]
tags: ["Locality-Sensitive-Hashing", "Supervised"]
short_authors: Sahil Garg, Greg Ver Steeg, Aram Galstyan
---
Natural language processing often involves computations with semantic or
syntactic graphs to facilitate sophisticated reasoning based on structural
relationships. While convolution kernels provide a powerful tool for comparing
graph structure based on node (word) level relationships, they are difficult to
customize and can be computationally expensive. We propose a generalization of
convolution kernels, with a nonstationary model, for better expressibility of
natural languages in supervised settings. For a scalable learning of the
parameters introduced with our model, we propose a novel algorithm that
leverages stochastic sampling on k-nearest neighbor graphs, along with
approximations based on locality-sensitive hashing. We demonstrate the
advantages of our approach on a challenging real-world (structured inference)
problem of automatically extracting biological models from the text of
scientific papers.