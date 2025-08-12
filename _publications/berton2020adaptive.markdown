---
layout: publication
title: 'Adaptive-attentive Geolocalization From Few Queries: A Hybrid Approach'
authors: Gabriele Moreno Berton, Valerio Paolicelli, Carlo Masone, Barbara Caputo
conference: Frontiers in Computer Science
year: 2022
bibkey: berton2020adaptive
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.06897'}]
tags: []
short_authors: Berton et al.
---
We address the task of cross-domain visual place recognition, where the goal
is to geolocalize a given query image against a labeled gallery, in the case
where the query and the gallery belong to different visual domains. To achieve
this, we focus on building a domain robust deep network by leveraging over an
attention mechanism combined with few-shot unsupervised domain adaptation
techniques, where we use a small number of unlabeled target domain images to
learn about the target distribution. With our method, we are able to outperform
the current state of the art while using two orders of magnitude less target
domain images. Finally we propose a new large-scale dataset for cross-domain
visual place recognition, called SVOX. The pytorch code is available at
https://github.com/valeriopaolicelli/AdAGeo .