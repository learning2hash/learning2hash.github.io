---
layout: publication
title: A New Coreset Framework For Clustering
authors: Vincent Cohen-Addad, David Saulpic, Chris Schwiegelshohn
conference: Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing
year: 2021
bibkey: cohenaddad2021new
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.06133'}]
tags: []
short_authors: Vincent Cohen-Addad, David Saulpic, Chris Schwiegelshohn
---
Given a metric space, the \((k,z)\)-clustering problem consists of finding \(k\)
centers such that the sum of the of distances raised to the power \(z\) of every
point to its closest center is minimized. This encapsulates the famous
\(k\)-median (\(z=1\)) and \(k\)-means (\(z=2\)) clustering problems. Designing
small-space sketches of the data that approximately preserves the cost of the
solutions, also known as *coresets*, has been an important research
direction over the last 15 years.
  In this paper, we present a new, simple coreset framework that simultaneously
improves upon the best known bounds for a large variety of settings, ranging
from Euclidean space, doubling metric, minor-free metric, and the general
metric cases.