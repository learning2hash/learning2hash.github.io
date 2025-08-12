---
layout: publication
title: Efficient Processing Of Raster And Vector Data
authors: "Fernando Silva-coira, Jos\xE9 R. Param\xE1, Susana Ladra, Juan R. L\xF3\
  pez, Gilberto Guti\xE9rrez"
conference: PLOS ONE
year: 2020
bibkey: silvacoira2019efficient
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.11866'}]
tags: []
short_authors: Silva-coira et al.
---
In this work, we propose a framework to store and manage spatial data, which
includes new efficient algorithms to perform operations accepting as input a
raster dataset and a vector dataset. More concretely, we present algorithms for
solving a spatial join between a raster and a vector dataset imposing a
restriction on the values of the cells of the raster; and an algorithm for
retrieving K objects of a vector dataset that overlap cells of a raster
dataset, such that the K objects are those overlapping the highest (or lowest)
cell values among all objects. The raster data is stored using a compact data
structure, which can directly manipulate compressed data without the need for
prior decompression. This leads to better running times and lower memory
consumption. In our experimental evaluation comparing our solution to other
baselines, we obtain the best space/time trade-offs.