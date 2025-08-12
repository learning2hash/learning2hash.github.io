---
layout: publication
title: Patchperpix For Instance Segmentation
authors: Peter Hirsch, Lisa Mais, Dagmar Kainmueller
conference: Lecture Notes in Computer Science
year: 2020
bibkey: hirsch2020patchperpix
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.07626'}]
tags: []
short_authors: Peter Hirsch, Lisa Mais, Dagmar Kainmueller
---
We present a novel method for proposal free instance segmentation that can
handle sophisticated object shapes which span large parts of an image and form
dense object clusters with crossovers. Our method is based on predicting dense
local shape descriptors, which we assemble to form instances. All instances are
assembled simultaneously in one go. To our knowledge, our method is the first
non-iterative method that yields instances that are composed of learnt shape
patches. We evaluate our method on a diverse range of data domains, where it
defines the new state of the art on four benchmarks, namely the ISBI 2012 EM
segmentation benchmark, the BBBC010 C. elegans dataset, and 2d as well as 3d
fluorescence microscopy data of cell nuclei. We show furthermore that our
method also applies to 3d light microscopy data of Drosophila neurons, which
exhibit extreme cases of complex shape clusters