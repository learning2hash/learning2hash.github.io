---
layout: publication
title: On Equivariant And Invariant Learning Of Object Landmark Representations
authors: Zezhou Cheng, Jong-chyi Su, Subhransu Maji
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: cheng2020equivariant
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.14787'}]
tags: ["ICCV"]
short_authors: Zezhou Cheng, Jong-chyi Su, Subhransu Maji
---
Given a collection of images, humans are able to discover landmarks by
modeling the shared geometric structure across instances. This idea of
geometric equivariance has been widely used for the unsupervised discovery of
object landmark representations. In this paper, we develop a simple and
effective approach by combining instance-discriminative and
spatially-discriminative contrastive learning. We show that when a deep network
is trained to be invariant to geometric and photometric transformations,
representations emerge from its intermediate layers that are highly predictive
of object landmarks. Stacking these across layers in a "hypercolumn" and
projecting them using spatially-contrastive learning further improves their
performance on matching and few-shot landmark regression tasks. We also present
a unified view of existing equivariant and invariant representation learning
approaches through the lens of contrastive learning, shedding light on the
nature of invariances learned. Experiments on standard benchmarks for landmark
learning, as well as a new challenging one we propose, show that the proposed
approach surpasses prior state-of-the-art.