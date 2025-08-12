---
layout: publication
title: Pointwise Binary Classification With Pairwise Confidence Comparisons
authors: Lei Feng, Senlin Shu, Nan Lu, Bo Han, Miao Xu, Gang Niu, Bo An, Masashi Sugiyama
conference: Arxiv
year: 2020
bibkey: feng2020pointwise
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.01875'}]
tags: ["Evaluation", "Supervised"]
short_authors: Feng et al.
---
To alleviate the data requirement for training effective binary classifiers
in binary classification, many weakly supervised learning settings have been
proposed. Among them, some consider using pairwise but not pointwise labels,
when pointwise labels are not accessible due to privacy, confidentiality, or
security reasons. However, as a pairwise label denotes whether or not two data
points share a pointwise label, it cannot be easily collected if either point
is equally likely to be positive or negative. Thus, in this paper, we propose a
novel setting called pairwise comparison (Pcomp) classification, where we have
only pairs of unlabeled data that we know one is more likely to be positive
than the other. Firstly, we give a Pcomp data generation process, derive an
unbiased risk estimator (URE) with theoretical guarantee, and further improve
URE using correction functions. Secondly, we link Pcomp classification to
noisy-label learning to develop a progressive URE and improve it by imposing
consistency regularization. Finally, we demonstrate by experiments the
effectiveness of our methods, which suggests Pcomp is a valuable and
practically useful type of pairwise supervision besides the pairwise label.