---
layout: publication
title: Raising The Bar On The Evaluation Of Out-of-distribution Detection
authors: Jishnu Mukhoti, Tsung-yu Lin, Bor-chun Chen, Ashish Shah, Philip H. S. Torr,
  Puneet K. Dokania, Ser-nam Lim
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: mukhoti2022raising
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.11960'}]
tags: ["Evaluation", "ICCV"]
short_authors: Mukhoti et al.
---
In image classification, a lot of development has happened in detecting
out-of-distribution (OoD) data. However, most OoD detection methods are
evaluated on a standard set of datasets, arbitrarily different from training
data. There is no clear definition of what forms a ``good" OoD dataset.
Furthermore, the state-of-the-art OoD detection methods already achieve near
perfect results on these standard benchmarks. In this paper, we define 2
categories of OoD data using the subtly different concepts of perceptual/visual
and semantic similarity to in-distribution (iD) data. We define Near OoD
samples as perceptually similar but semantically different from iD samples, and
Shifted samples as points which are visually different but semantically akin to
iD data. We then propose a GAN based framework for generating OoD samples from
each of these 2 categories, given an iD dataset. Through extensive experiments
on MNIST, CIFAR-10/100 and ImageNet, we show that a) state-of-the-art OoD
detection methods which perform exceedingly well on conventional benchmarks are
significantly less robust to our proposed benchmark. Moreover, b) models
performing well on our setup also perform well on conventional real-world OoD
detection benchmarks and vice versa, thereby indicating that one might not even
need a separate OoD set, to reliably evaluate performance in OoD detection.