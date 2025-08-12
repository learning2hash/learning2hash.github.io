---
layout: publication
title: Fast And Accurate \(k\)-means++ Via Rejection Sampling
authors: Vincent Cohen-Addad, Silvio Lattanzi, Ashkan Norouzi-Fard, Christian Sohler,
  Ola Svensson
conference: Arxiv
year: 2020
bibkey: cohenaddad2020fast
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.11891'}]
tags: []
short_authors: Cohen-Addad et al.
---
\(k\)-means++ \cite\{arthur2007k\} is a widely used clustering algorithm that is
easy to implement, has nice theoretical guarantees and strong empirical
performance. Despite its wide adoption, \(k\)-means++ sometimes suffers from
being slow on large data-sets so a natural question has been to obtain more
efficient algorithms with similar guarantees. In this paper, we present a near
linear time algorithm for \(k\)-means++ seeding. Interestingly our algorithm
obtains the same theoretical guarantees as \(k\)-means++ and significantly
improves earlier results on fast \(k\)-means++ seeding. Moreover, we show
empirically that our algorithm is significantly faster than \(k\)-means++ and
obtains solutions of equivalent quality.