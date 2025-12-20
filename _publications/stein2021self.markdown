---
layout: publication
title: Self-supervised Similarity Search For Large Scientific Datasets
authors: George Stein, Peter Harrington, Jacqueline Blaum, Tomislav Medan, Zarija
  Lukic
conference: Arxiv
year: 2021
bibkey: stein2021self
citations: 0
additional_links: [{name: Code, url: 'https://github.com/georgestein/galaxy_search'},
  {name: Paper, url: 'https://arxiv.org/abs/2110.13151'}]
tags: ["Datasets", "Self-Supervised", "Similarity Search", "Supervised", "Survey Paper"]
short_authors: Stein et al.
---
We present the use of self-supervised learning to explore and exploit large
unlabeled datasets. Focusing on 42 million galaxy images from the latest data
release of the Dark Energy Spectroscopic Instrument (DESI) Legacy Imaging
Surveys, we first train a self-supervised model to distill low-dimensional
representations that are robust to symmetries, uncertainties, and noise in each
image. We then use the representations to construct and publicly release an
interactive semantic similarity search tool. We demonstrate how our tool can be
used to rapidly discover rare objects given only a single example, increase the
speed of crowd-sourcing campaigns, and construct and improve training sets for
supervised applications. While we focus on images from sky surveys, the
technique is straightforward to apply to any scientific dataset of any
dimensionality. The similarity search web app can be found at
https://github.com/georgestein/galaxy_search