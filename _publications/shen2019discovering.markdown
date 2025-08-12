---
layout: publication
title: Discovering Visual Patterns In Art Collections With Spatially-consistent Feature
  Learning
authors: Xi Shen, Alexei A. Efros, Mathieu Aubry
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: shen2019discovering
citations: 87
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.02678'}]
tags: ["CVPR"]
short_authors: Xi Shen, Alexei A. Efros, Mathieu Aubry
---
Our goal in this paper is to discover near duplicate patterns in large
collections of artworks. This is harder than standard instance mining due to
differences in the artistic media (oil, pastel, drawing, etc), and
imperfections inherent in the copying process. The key technical insight is to
adapt a standard deep feature to this task by fine-tuning it on the specific
art collection using self-supervised learning. More specifically, spatial
consistency between neighbouring feature matches is used as supervisory
fine-tuning signal. The adapted feature leads to more accurate style-invariant
matching, and can be used with a standard discovery approach, based on
geometric verification, to identify duplicate patterns in the dataset. The
approach is evaluated on several different datasets and shows surprisingly good
qualitative discovery results. For quantitative evaluation of the method, we
annotated 273 near duplicate details in a dataset of 1587 artworks attributed
to Jan Brueghel and his workshop. Beyond artwork, we also demonstrate
improvement on localization on the Oxford5K photo dataset as well as on
historical photograph localization on the Large Time Lags Location (LTLL)
dataset.