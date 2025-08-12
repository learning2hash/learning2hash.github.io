---
layout: publication
title: '"scatspotter" 2024 -- A Distributed Dog Poop Detection Dataset'
authors: Jon Crall
conference: Arxiv
year: 2024
bibkey: crall2024scatspotter
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.16473'}]
tags: ["Datasets"]
short_authors: Jon Crall
---
We introduce a new -- currently 42 gigabyte -- ``living'' dataset of phone
images of dog feces, annotated with manually drawn or AI-assisted polygon
labels. There are 6k full resolution images and 4k detailed polygon
annotations. The collection and annotation of images started in late 2020 and
the dataset grows by roughly 1GB a month. We train VIT and MaskRCNN baseline
models to explore the difficulty of the dataset. The best model achieves a
pixelwise average precision of 0.858 on a 691-image validation set and 0.847 on
a small independently captured 30-image contributor test set. The most recent
snapshot of dataset is made publicly available through three different
distribution methods: one centralized (Girder) and two decentralized (IPFS and
BitTorrent). We study of the trade-offs between distribution methods and
discuss the feasibility of each with respect to reliably sharing open
scientific data. The code to reproduce the experiments is hosted on GitHub, and
the data is published under the Creative Commons Attribution 4.0 International
license. Model weights are made publicly available with the dataset.
Experimental hardware, time, energy, and emissions are quantified.