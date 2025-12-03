---
layout: publication
title: 'RHINO: Regularizing The Hash-based Implicit Neural Representation'
authors: Hao Zhu, Fengyi Liu, Qi Zhang, Xun Cao, Zhan Ma
conference: Arxiv
year: 2023
bibkey: zhu2023rhino
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.12642'}]
tags: ["Efficiency"]
short_authors: Zhu et al.
---
The use of Implicit Neural Representation (INR) through a hash-table has
demonstrated impressive effectiveness and efficiency in characterizing
intricate signals. However, current state-of-the-art methods exhibit
insufficient regularization, often yielding unreliable and noisy results during
interpolations. We find that this issue stems from broken gradient flow between
input coordinates and indexed hash-keys, where the chain rule attempts to model
discrete hash-keys, rather than the continuous coordinates. To tackle this
concern, we introduce RHINO, in which a continuous analytical function is
incorporated to facilitate regularization by connecting the input coordinate
and the network additionally without modifying the architecture of current
hash-based INRs. This connection ensures a seamless backpropagation of
gradients from the network's output back to the input coordinates, thereby
enhancing regularization. Our experimental results not only showcase the
broadened regularization capability across different hash-based INRs like DINER
and Instant NGP, but also across a variety of tasks such as image fitting,
representation of signed distance functions, and optimization of 5D static / 6D
dynamic neural radiance fields. Notably, RHINO outperforms current
state-of-the-art techniques in both quality and speed, affirming its
superiority.