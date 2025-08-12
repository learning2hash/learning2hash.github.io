---
layout: publication
title: Optimised One-class Classification Performance
authors: Oliver Urs Lenz, Daniel Peralta, Chris Cornelis
conference: Machine Learning
year: 2022
bibkey: lenz2021optimised
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.02618'}]
tags: ["Evaluation"]
short_authors: Oliver Urs Lenz, Daniel Peralta, Chris Cornelis
---
We provide a thorough treatment of one-class classification with
hyperparameter optimisation for five data descriptors: Support Vector Machine
(SVM), Nearest Neighbour Distance (NND), Localised Nearest Neighbour Distance
(LNND), Local Outlier Factor (LOF) and Average Localised Proximity (ALP). The
hyperparameters of SVM and LOF have to be optimised through cross-validation,
while NND, LNND and ALP allow an efficient form of leave-one-out validation and
the reuse of a single nearest-neighbour query. We experimentally evaluate the
effect of hyperparameter optimisation with 246 classification problems drawn
from 50 datasets. From a selection of optimisation algorithms, the recent
Malherbe-Powell proposal optimises the hyperparameters of all data descriptors
most efficiently. We calculate the increase in test AUROC and the amount of
overfitting as a function of the number of hyperparameter evaluations. After 50
evaluations, ALP and SVM significantly outperform LOF, NND and LNND, and LOF
and NND outperform LNND. The performance of ALP and SVM is comparable, but ALP
can be optimised more efficiently so constitutes a good default choice.
Alternatively, using validation AUROC as a selection criterion between ALP or
SVM gives the best overall result, and NND is the least computationally
demanding option. We thus end up with a clear trade-off between three choices,
allowing practitioners to make an informed decision.