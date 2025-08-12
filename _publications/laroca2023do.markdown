---
layout: publication
title: Do We Train On Test Data? The Impact Of Near-duplicates On License Plate Recognition
authors: Rayson Laroca, Valter Estevam, Alceu S. Britto, Rodrigo Minetto, David Menotti
conference: 2023 International Joint Conference on Neural Networks (IJCNN)
year: 2023
bibkey: laroca2023do
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.04653'}]
tags: ["Datasets", "Evaluation"]
short_authors: Laroca et al.
---
This work draws attention to the large fraction of near-duplicates in the
training and test sets of datasets widely adopted in License Plate Recognition
(LPR) research. These duplicates refer to images that, although different, show
the same license plate. Our experiments, conducted on the two most popular
datasets in the field, show a substantial decrease in recognition rate when six
well-known models are trained and tested under fair splits, that is, in the
absence of duplicates in the training and test sets. Moreover, in one of the
datasets, the ranking of models changed considerably when they were trained and
tested under duplicate-free splits. These findings suggest that such duplicates
have significantly biased the evaluation and development of deep learning-based
models for LPR. The list of near-duplicates we have found and proposals for
fair splits are publicly available for further research at
https://raysonlaroca.github.io/supp/lpr-train-on-test/