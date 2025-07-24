---
layout: publication
title: Deep Unsupervised Hashing With Latent Semantic Components
authors: Qinghong Lin, Xiaojun Chen, Qin Zhang, Shaotian Cai, Wenzhe Zhao, Hongfa
  Wang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: lin2022deep
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.09420'}]
tags: ["AAAI", "Evaluation", "Hashing Methods", "Unsupervised"]
short_authors: Lin et al.
---
Deep unsupervised hashing has been appreciated in the regime of image
retrieval. However, most prior arts failed to detect the semantic components
and their relationships behind the images, which makes them lack discriminative
power. To make up the defect, we propose a novel Deep Semantic Components
Hashing (DSCH), which involves a common sense that an image normally contains a
bunch of semantic components with homology and co-occurrence relationships.
Based on this prior, DSCH regards the semantic components as latent variables
under the Expectation-Maximization framework and designs a two-step iterative
algorithm with the objective of maximum likelihood of training data. Firstly,
DSCH constructs a semantic component structure by uncovering the fine-grained
semantics components of images with a Gaussian Mixture Modal~(GMM), where an
image is represented as a mixture of multiple components, and the semantics
co-occurrence are exploited. Besides, coarse-grained semantics components, are
discovered by considering the homology relationships between fine-grained
components, and the hierarchy organization is then constructed. Secondly, DSCH
makes the images close to their semantic component centers at both fine-grained
and coarse-grained levels, and also makes the images share similar semantic
components close to each other. Extensive experiments on three benchmark
datasets demonstrate that the proposed hierarchical semantic components indeed
facilitate the hashing model to achieve superior performance.