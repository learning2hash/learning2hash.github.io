---
layout: publication
title: Visual Place Recognition With Probabilistic Vertex Voting
authors: Mathias Gehrig, Elena Stumm, Timo Hinzmann, Roland Siegwart
conference: 2017 IEEE International Conference on Robotics and Automation (ICRA)
year: 2016
bibkey: gehrig2016visual
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.03548'}]
tags: [Evaluation, Tools & Libraries, ICRA, Datasets]
short_authors: Gehrig et al.
---
We propose a novel scoring concept for visual place recognition based on
nearest neighbor descriptor voting and demonstrate how the algorithm naturally
emerges from the problem formulation. Based on the observation that the number
of votes for matching places can be evaluated using a binomial distribution
model, loop closures can be detected with high precision. By casting the
problem into a probabilistic framework, we not only remove the need for
commonly employed heuristic parameters but also provide a powerful score to
classify matching and non-matching places. We present methods for both a 2D-2D
pose-graph vertex matching and a 2D-3D landmark matching based on the above
scoring. The approach maintains accuracy while being efficient enough for
online application through the use of compact (low dimensional) descriptors and
fast nearest neighbor retrieval techniques. The proposed methods are evaluated
on several challenging datasets in varied environments, showing
state-of-the-art results with high precision and high recall.