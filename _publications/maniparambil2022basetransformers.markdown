---
layout: publication
title: 'Basetransformers: Attention Over Base Data-points For One Shot Learning'
authors: Mayug Maniparambil, Kevin McGuinness, Noel O'Connor
conference: Arxiv
year: 2022
bibkey: maniparambil2022basetransformers
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.02476'}]
tags: []
short_authors: Mayug Maniparambil, Kevin McGuinness, Noel O'Connor
---
Few shot classification aims to learn to recognize novel categories using
only limited samples per category. Most current few shot methods use a base
dataset rich in labeled examples to train an encoder that is used for obtaining
representations of support instances for novel classes. Since the test
instances are from a distribution different to the base distribution, their
feature representations are of poor quality, degrading performance. In this
paper we propose to make use of the well-trained feature representations of the
base dataset that are closest to each support instance to improve its
representation during meta-test time. To this end, we propose BaseTransformers,
that attends to the most relevant regions of the base dataset feature space and
improves support instance representations. Experiments on three benchmark data
sets show that our method works well for several backbones and achieves
state-of-the-art results in the inductive one shot setting. Code is available
at github.com/mayug/BaseTransformers