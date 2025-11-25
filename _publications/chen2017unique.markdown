---
layout: publication
title: Unique Entity Estimation With Application To The Syrian Conflict
authors: Beidi Chen, Anshumali Shrivastava, Rebecca C. Steorts
conference: Arxiv
year: 2017
bibkey: chen2017unique
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.02690'}]
tags: ["Evaluation", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Beidi Chen, Anshumali Shrivastava, Rebecca C. Steorts
---
Entity resolution identifies and removes duplicate entities in large, noisy
databases and has grown in both usage and new developments as a result of
increased data availability. Nevertheless, entity resolution has tradeoffs
regarding assumptions of the data generation process, error rates, and
computational scalability that make it a difficult task for real applications.
In this paper, we focus on a related problem of unique entity estimation, which
is the task of estimating the unique number of entities and associated standard
errors in a data set with duplicate entities. Unique entity estimation shares
many fundamental challenges of entity resolution, namely, that the
computational cost of all-to-all entity comparisons is intractable for large
databases. To circumvent this computational barrier, we propose an efficient
(near-linear time) estimation algorithm based on locality sensitive hashing.
Our estimator, under realistic assumptions, is unbiased and has provably low
variance compared to existing random sampling based approaches. In addition, we
empirically show its superiority over the state-of-the-art estimators on three
real applications. The motivation for our work is to derive an accurate
estimate of the documented, identifiable deaths in the ongoing Syrian conflict.
Our methodology, when applied to the Syrian data set, provides an estimate of
\(191,874 \pm 1772\) documented, identifiable deaths, which is very close to the
Human Rights Data Analysis Group (HRDAG) estimate of 191,369. Our work provides
an example of challenges and efforts involved in solving a real, noisy
challenging problem where modeling assumptions may not hold.