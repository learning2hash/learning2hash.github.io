---
layout: publication
title: Learning Conditional Distributions On Continuous Spaces
authors: "Cyril B\xE9n\xE9zet, Ziteng Cheng, Sebastian Jaimungal"
conference: Arxiv
year: 2024
bibkey: "b\xE9n\xE9zet2024learning"
citations: 0
additional_links: [{name: Code, url: 'https://github.com/zcheng-a/LCD_kNN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.09375'}]
tags: [Evaluation, Efficiency]
short_authors: "Cyril B\xE9n\xE9zet, Ziteng Cheng, Sebastian Jaimungal"
---
We investigate sample-based learning of conditional distributions on
multi-dimensional unit boxes, allowing for different dimensions of the feature
and target spaces. Our approach involves clustering data near varying query
points in the feature space to create empirical measures in the target space.
We employ two distinct clustering schemes: one based on a fixed-radius ball and
the other on nearest neighbors. We establish upper bounds for the convergence
rates of both methods and, from these bounds, deduce optimal configurations for
the radius and the number of neighbors. We propose to incorporate the nearest
neighbors method into neural network training, as our empirical analysis
indicates it has better performance in practice. For efficiency, our training
process utilizes approximate nearest neighbors search with random binary space
partitioning. Additionally, we employ the Sinkhorn algorithm and a
sparsity-enforced transport plan. Our empirical findings demonstrate that, with
a suitably designed structure, the neural network has the ability to adapt to a
suitable level of Lipschitz continuity locally. For reproducibility, our code
is available at https://github.com/zcheng-a/LCD_kNN.