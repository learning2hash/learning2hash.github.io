---
layout: publication
title: Learning From One And Only One Shot
authors: Haizi Yu, Igor Mineyev, Lav R. Varshney, James A. Evans
conference: Arxiv
year: 2022
bibkey: yu2022learning
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.08815'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yu et al.
---
Humans can generalize from only a few examples and from little pretraining on
similar tasks. Yet, machine learning (ML) typically requires large data to
learn or pre-learn to transfer. Motivated by nativism and artificial general
intelligence, we directly model human-innate priors in abstract visual tasks
such as character and doodle recognition. This yields a white-box model that
learns general-appearance similarity by mimicking how humans naturally
``distort'' an object at first sight. Using just nearest-neighbor
classification on this cognitively-inspired similarity space, we achieve
human-level recognition with only \(1\)--\(10\) examples per class and no
pretraining. This differs from few-shot learning that uses massive pretraining.
In the tiny-data regime of MNIST, EMNIST, Omniglot, and QuickDraw benchmarks,
we outperform both modern neural networks and classical ML. For unsupervised
learning, by learning the non-Euclidean, general-appearance similarity space in
a \(k\)-means style, we achieve multifarious visual realizations of abstract
concepts by generating human-intuitive archetypes as cluster centroids.