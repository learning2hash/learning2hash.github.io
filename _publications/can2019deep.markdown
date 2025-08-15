---
layout: publication
title: Deep Metric Learning With Alternating Projections Onto Feasible Sets
authors: "O\u011Ful Can, Yeti Ziya G\xFCrb\xFCz, A. Ayd\u0131n Alatan"
conference: 2021 IEEE International Conference on Image Processing (ICIP)
year: 2021
bibkey: can2019deep
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.07585'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval"]
short_authors: "O\u011Ful Can, Yeti Ziya G\xFCrb\xFCz, A. Ayd\u0131n Alatan"
---
During the training of networks for distance metric learning, minimizers of
the typical loss functions can be considered as "feasible points" satisfying a
set of constraints imposed by the training data. To this end, we reformulate
distance metric learning problem as finding a feasible point of a constraint
set where the embedding vectors of the training data satisfy desired
intra-class and inter-class proximity. The feasible set induced by the
constraint set is expressed as the intersection of the relaxed feasible sets
which enforce the proximity constraints only for particular samples (a sample
from each class) of the training data. Then, the feasible point problem is to
be approximately solved by performing alternating projections onto those
feasible sets. Such an approach introduces a regularization term and results in
minimizing a typical loss function with a systematic batch set construction
where these batches are constrained to contain the same sample from each class
for a certain number of iterations. Moreover, these particular samples can be
considered as the class representatives, allowing efficient utilization of hard
class mining during batch construction. The proposed technique is applied with
the well-accepted losses and evaluated on Stanford Online Products, CAR196 and
CUB200-2011 datasets for image retrieval and clustering. Outperforming
state-of-the-art, the proposed approach consistently improves the performance
of the integrated loss functions with no additional computational cost and
boosts the performance further by hard negative class mining.