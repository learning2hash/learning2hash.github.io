---
layout: publication
title: Distributed And Consistent Multi-image Feature Matching Via Quickmatch
authors: Zachary Serlin, Guang Yang, Brandon Sookraj, Calin Belta, Roberto Tron
conference: The International Journal of Robotics Research
year: 2020
bibkey: serlin2019distributed
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.13317'}]
tags: []
short_authors: Serlin et al.
---
In this work we consider the multi-image object matching problem, extend a
centralized solution of the problem to a distributed solution, and present an
experimental application of the centralized solution. Multi-image feature
matching is a keystone of many applications, including simultaneous
localization and mapping, homography, object detection, and structure from
motion. We first review the QuickMatch algorithm for multi-image feature
matching. We then present a scheme for distributing sets of features across
computational units (agents) that largely preserves feature match quality and
minimizes communication between agents (avoiding, in particular, the need of
flooding all data to all agents). Finally, we show how QuickMatch performs on
an object matching test with low quality images. The centralized QuickMatch
algorithm is compared to other standard matching algorithms, while the
Distributed QuickMatch algorithm is compared to the centralized algorithm in
terms of preservation of match consistency. The presented experiment shows that
QuickMatch matches features across a large number of images and features in
larger numbers and more accurately than standard techniques.