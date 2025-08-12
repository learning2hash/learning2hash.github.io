---
layout: publication
title: A Self-supervised GAN For Unsupervised Few-shot Object Recognition
authors: Khoi Nguyen, Sinisa Todorovic
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: nguyen2020self
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.06982'}]
tags: ["Few Shot & Zero Shot", "Self-Supervised", "Unsupervised"]
short_authors: Khoi Nguyen, Sinisa Todorovic
---
This paper addresses unsupervised few-shot object recognition, where all
training images are unlabeled, and test images are divided into queries and a
few labeled support images per object class of interest. The training and test
images do not share object classes. We extend the vanilla GAN with two loss
functions, both aimed at self-supervised learning. The first is a
reconstruction loss that enforces the discriminator to reconstruct the
probabilistically sampled latent code which has been used for generating the
"fake" image. The second is a triplet loss that enforces the discriminator to
output image encodings that are closer for more similar images. Evaluation,
comparisons, and detailed ablation studies are done in the context of few-shot
classification. Our approach significantly outperforms the state of the art on
the Mini-Imagenet and Tiered-Imagenet datasets.