---
layout: publication
title: Similarity Search For Efficient Active Learning And Search Of Rare Concepts
authors: Coleman Cody, Chou Edward, Katz-samuels Julian, Culatana Sean, Bailis Peter,
  Berg Alexander C., Nowak Robert, Sumbaly Roshan, Zaharia Matei, Yalniz I. Zeki
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: coleman2020similarity
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.00077'}]
tags: ["AAAI", "Datasets", "Efficiency", "Evaluation", "Large-Scale Search", "Scalability", "Similarity Search"]
short_authors: Coleman et al.
---
Many active learning and search approaches are intractable for large-scale
industrial settings with billions of unlabeled examples. Existing approaches
search globally for the optimal examples to label, scaling linearly or even
quadratically with the unlabeled data. In this paper, we improve the
computational efficiency of active learning and search methods by restricting
the candidate pool for labeling to the nearest neighbors of the currently
labeled set instead of scanning over all of the unlabeled data. We evaluate
several selection strategies in this setting on three large-scale computer
vision datasets: ImageNet, OpenImages, and a de-identified and aggregated
dataset of 10 billion images provided by a large internet company. Our approach
achieved similar mean average precision and recall as the traditional global
approach while reducing the computational cost of selection by up to three
orders of magnitude, thus enabling web-scale active learning.