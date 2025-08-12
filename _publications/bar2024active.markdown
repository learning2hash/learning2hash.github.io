---
layout: publication
title: Active Learning Via Classifier Impact And Greedy Selection For Interactive
  Image Retrieval
authors: Leah Bar, Boaz Lerner, Nir Darshan, Rami Ben-Ari
conference: Arxiv
year: 2024
bibkey: bar2024active
citations: 0
additional_links: [{name: Code, url: 'https://github.com/barleah/GreedyAL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2412.02310'}]
tags: []
short_authors: Bar et al.
---
Active Learning (AL) is a user-interactive approach aimed at reducing
annotation costs by selecting the most crucial examples to label. Although AL
has been extensively studied for image classification tasks, the specific
scenario of interactive image retrieval has received relatively little
attention. This scenario presents unique characteristics, including an open-set
and class-imbalanced binary classification, starting with very few labeled
samples. We introduce a novel batch-mode Active Learning framework named GAL
(Greedy Active Learning) that better copes with this application. It
incorporates a new acquisition function for sample selection that measures the
impact of each unlabeled sample on the classifier. We further embed this
strategy in a greedy selection approach, better exploiting the samples within
each batch. We evaluate our framework with both linear (SVM) and non-linear
MLP/Gaussian Process classifiers. For the Gaussian Process case, we show a
theoretical guarantee on the greedy approximation. Finally, we assess our
performance for the interactive content-based image retrieval task on several
benchmarks and demonstrate its superiority over existing approaches and common
baselines. Code is available at https://github.com/barleah/GreedyAL.