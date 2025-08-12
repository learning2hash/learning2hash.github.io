---
layout: publication
title: Training Binary Neural Networks With Real-to-binary Convolutions
authors: Brais Martinez, Jing Yang, Adrian Bulat, Georgios Tzimiropoulos
conference: Arxiv
year: 2020
bibkey: martinez2020training
citations: 106
additional_links: [{name: Code, url: 'https://github.com/brais-martinez/real2binary'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.11535'}]
tags: []
short_authors: Martinez et al.
---
This paper shows how to train binary networks to within a few percent points
(\(\sim 3-5 %\)) of the full precision counterpart. We first show how to build a
strong baseline, which already achieves state-of-the-art accuracy, by combining
recently proposed advances and carefully adjusting the optimization procedure.
Secondly, we show that by attempting to minimize the discrepancy between the
output of the binary and the corresponding real-valued convolution, additional
significant accuracy gains can be obtained. We materialize this idea in two
complementary ways: (1) with a loss function, during training, by matching the
spatial attention maps computed at the output of the binary and real-valued
convolutions, and (2) in a data-driven manner, by using the real-valued
activations, available during inference prior to the binarization process, for
re-scaling the activations right after the binary convolution. Finally, we show
that, when putting all of our improvements together, the proposed model beats
the current state of the art by more than 5% top-1 accuracy on ImageNet and
reduces the gap to its real-valued counterpart to less than 3% and 5% top-1
accuracy on CIFAR-100 and ImageNet respectively when using a ResNet-18
architecture. Code available at https://github.com/brais-martinez/real2binary.