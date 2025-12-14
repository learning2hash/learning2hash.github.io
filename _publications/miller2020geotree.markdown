---
layout: publication
title: 'Geotree: A Data Structure For Constant Time Geospatial Search Enabling A Real-time
  Mix-adjusted Median Property Price Index'
authors: Robert Miller, Phil Maguire
conference: Arxiv
year: 2020
bibkey: miller2020geotree
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.02167'}]
tags: [Evaluation, Datasets, Efficiency]
short_authors: Robert Miller, Phil Maguire
---
A common problem appearing across the field of data science is \(k\)-NN
(\(k\)-nearest neighbours), particularly within the context of Geographic
Information Systems. In this article, we present a novel data structure, the
GeoTree, which holds a collection of geohashes (string encodings of GPS
co-ordinates). This enables a constant \(O\left(1\right)\) time search algorithm
that returns a set of geohashes surrounding a given geohash in the GeoTree,
representing the approximate \(k\)-nearest neighbours of that geohash.
Furthermore, the GeoTree data structure retains \(O\left(n\right)\) memory
requirement. We apply the data structure to a property price index algorithm
focused on price comparison with historical neighbouring sales, demonstrating
an enhanced performance. The results show that this data structure allows for
the development of a real-time property price index, and can be scaled to
larger datasets with ease.