---
layout: publication
title: Image Splicing Localization Using A Multi-task Fully Convolutional Network
  (MFCN)
authors: Ronald Salloum, Yuzhuo Ren, C. -c. Jay Kuo
conference: Journal of Visual Communication and Image Representation
year: 2018
bibkey: salloum2017image
citations: 340
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.02016'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ronald Salloum, Yuzhuo Ren, C. -c. Jay Kuo
---
In this work, we propose a technique that utilizes a fully convolutional
network (FCN) to localize image splicing attacks. We first evaluated a
single-task FCN (SFCN) trained only on the surface label. Although the SFCN is
shown to provide superior performance over existing methods, it still provides
a coarse localization output in certain cases. Therefore, we propose the use of
a multi-task FCN (MFCN) that utilizes two output branches for multi-task
learning. One branch is used to learn the surface label, while the other branch
is used to learn the edge or boundary of the spliced region. We trained the
networks using the CASIA v2.0 dataset, and tested the trained models on the
CASIA v1.0, Columbia Uncompressed, Carvalho, and the DARPA/NIST Nimble
Challenge 2016 SCI datasets. Experiments show that the SFCN and MFCN outperform
existing splicing localization algorithms, and that the MFCN can achieve finer
localization than the SFCN.