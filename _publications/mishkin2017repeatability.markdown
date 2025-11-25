---
layout: publication
title: 'Repeatability Is Not Enough: Learning Affine Regions Via Discriminability'
authors: Dmytro Mishkin, Filip Radenovic, Jiri Matas
conference: Arxiv
year: 2017
bibkey: mishkin2017repeatability
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ducha-aiki/affnet'}, {name: Paper,
    url: 'https://arxiv.org/abs/1711.06704'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Supervised"]
short_authors: Dmytro Mishkin, Filip Radenovic, Jiri Matas
---
A method for learning local affine-covariant regions is presented. We show
that maximizing geometric repeatability does not lead to local regions, a.k.a
features,that are reliably matched and this necessitates descriptor-based
learning. We explore factors that influence such learning and registration: the
loss function, descriptor type, geometric parametrization and the trade-off
between matchability and geometric accuracy and propose a novel hard
negative-constant loss function for learning of affine regions. The affine
shape estimator -- AffNet -- trained with the hard negative-constant loss
outperforms the state-of-the-art in bag-of-words image retrieval and wide
baseline stereo. The proposed training process does not require precisely
geometrically aligned patches.The source codes and trained weights are
available at https://github.com/ducha-aiki/affnet