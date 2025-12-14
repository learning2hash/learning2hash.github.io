---
layout: publication
title: 'Wv-net: A Foundation Model For SAR Wv-mode Satellite Imagery Trained Using
  Contrastive Self-supervised Learning On 10 Million Images'
authors: Yannik Glaser, Justin E. Stopa, Linnea M. Wolniewicz, Ralph Foster, Doug
  Vandemark, Alexis Mouche, Bertrand Chapron, Peter Sadowski
conference: Arxiv
year: 2024
bibkey: glaser2024wv
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.18765'}]
tags: [Self-Supervised, Supervised, Image Retrieval, Unsupervised]
short_authors: Glaser et al.
---
The European Space Agency's Copernicus Sentinel-1 (S-1) mission is a
constellation of C-band synthetic aperture radar (SAR) satellites that provide
unprecedented monitoring of the world's oceans. S-1's wave mode (WV) captures
20x20 km image patches at 5 m pixel resolution and is unaffected by cloud cover
or time-of-day. The mission's open data policy has made SAR data easily
accessible for a range of applications, but the need for manual image
annotations is a bottleneck that hinders the use of machine learning methods.
This study uses nearly 10 million WV-mode images and contrastive
self-supervised learning to train a semantic embedding model called WV-Net. In
multiple downstream tasks, WV-Net outperforms a comparable model that was
pre-trained on natural images (ImageNet) with supervised learning. Experiments
show improvements for estimating wave height (0.50 vs 0.60 RMSE using linear
probing), estimating near-surface air temperature (0.90 vs 0.97 RMSE), and
performing multilabel-classification of geophysical and atmospheric phenomena
(0.96 vs 0.95 micro-averaged AUROC). WV-Net embeddings are also superior in an
unsupervised image-retrieval task and scale better in data-sparse settings.
Together, these results demonstrate that WV-Net embeddings can support
geophysical research by providing a convenient foundation model for a variety
of data analysis and exploration tasks.