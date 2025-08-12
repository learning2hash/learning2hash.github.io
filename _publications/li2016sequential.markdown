---
layout: publication
title: Sequential Person Recognition In Photo Albums With A Recurrent Network
authors: Yao Li, Guosheng Lin, Bohan Zhuang, Lingqiao Liu, Chunhua Shen, Anton van
  Den Hengel
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: li2016sequential
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.09967'}]
tags: ["CVPR"]
short_authors: Li et al.
---
Recognizing the identities of people in everyday photos is still a very
challenging problem for machine vision, due to non-frontal faces, changes in
clothing, location, lighting and similar. Recent studies have shown that rich
relational information between people in the same photo can help in recognizing
their identities. In this work, we propose to model the relational information
between people as a sequence prediction task. At the core of our work is a
novel recurrent network architecture, in which relational information between
instances' labels and appearance are modeled jointly. In addition to relational
cues, scene context is incorporated in our sequence prediction model with no
additional cost. In this sense, our approach is a unified framework for
modeling both contextual cues and visual appearance of person instances. Our
model is trained end-to-end with a sequence of annotated instances in a photo
as inputs, and a sequence of corresponding labels as targets. We demonstrate
that this simple but elegant formulation achieves state-of-the-art performance
on the newly released People In Photo Albums (PIPA) dataset.