---
layout: publication
title: 'The Met Dataset: Instance-level Recognition For Artworks'
authors: Nikolaos-Antonios Ypsilantis, Noa Garcia, Guangxing Han, Sarah Ibrahimi,
  Nanne van Noord, Giorgos Tolias
conference: Arxiv
year: 2022
bibkey: ypsilantis2022met
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.01747'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ypsilantis et al.
---
This work introduces a dataset for large-scale instance-level recognition in
the domain of artworks. The proposed benchmark exhibits a number of different
challenges such as large inter-class similarity, long tail distribution, and
many classes. We rely on the open access collection of The Met museum to form a
large training set of about 224k classes, where each class corresponds to a
museum exhibit with photos taken under studio conditions. Testing is primarily
performed on photos taken by museum guests depicting exhibits, which introduces
a distribution shift between training and testing. Testing is additionally
performed on a set of images not related to Met exhibits making the task
resemble an out-of-distribution detection problem. The proposed benchmark
follows the paradigm of other recent datasets for instance-level recognition on
different domains to encourage research on domain independent approaches. A
number of suitable approaches are evaluated to offer a testbed for future
comparisons. Self-supervised and supervised contrastive learning are
effectively combined to train the backbone which is used for non-parametric
classification that is shown as a promising direction. Dataset webpage:
http://cmp.felk.cvut.cz/met/