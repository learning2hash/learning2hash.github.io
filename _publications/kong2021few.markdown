---
layout: publication
title: Few-shot Image Generation With Mixup-based Distance Learning
authors: Chaerin Kong, Jeesoo Kim, Donghoon Han, Nojun Kwak
conference: Lecture Notes in Computer Science
year: 2022
bibkey: kong2021few
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.11672'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Kong et al.
---
Producing diverse and realistic images with generative models such as GANs
typically requires large scale training with vast amount of images. GANs
trained with limited data can easily memorize few training samples and display
undesirable properties like "stairlike" latent space where interpolation in the
latent space yields discontinuous transitions in the output space. In this
work, we consider a challenging task of pretraining-free few-shot image
synthesis, and seek to train existing generative models with minimal
overfitting and mode collapse. We propose mixup-based distance regularization
on the feature space of both a generator and the counterpart discriminator that
encourages the two players to reason not only about the scarce observed data
points but the relative distances in the feature space they reside. Qualitative
and quantitative evaluation on diverse datasets demonstrates that our method is
generally applicable to existing models to enhance both fidelity and diversity
under few-shot setting. Code is available.