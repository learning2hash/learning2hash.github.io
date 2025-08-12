---
layout: publication
title: 'Openstreetview-5m: The Many Roads To Global Visual Geolocation'
authors: Guillaume Astruc, Nicolas Dufour, Ioannis Siglidis, Constantin Aronssohn,
  Nacim Bouia, Stephanie Fu, Romain Loiseau, van Nguyen Nguyen, Charles Raude, Elliot
  Vincent, Lintao Xu, Hongyu Zhou, Loic Landrieu
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: astruc2024openstreetview
citations: 2
additional_links: [{name: Code, url: 'https://github.com/gastruc/osv5m'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.18873'}]
tags: ["CVPR", "Datasets"]
short_authors: Astruc et al.
---
Determining the location of an image anywhere on Earth is a complex visual
task, which makes it particularly relevant for evaluating computer vision
algorithms. Yet, the absence of standard, large-scale, open-access datasets
with reliably localizable images has limited its potential. To address this
issue, we introduce OpenStreetView-5M, a large-scale, open-access dataset
comprising over 5.1 million geo-referenced street view images, covering 225
countries and territories. In contrast to existing benchmarks, we enforce a
strict train/test separation, allowing us to evaluate the relevance of learned
geographical features beyond mere memorization. To demonstrate the utility of
our dataset, we conduct an extensive benchmark of various state-of-the-art
image encoders, spatial representations, and training strategies. All
associated codes and models can be found at https://github.com/gastruc/osv5m.