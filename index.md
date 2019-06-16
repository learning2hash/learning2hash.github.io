---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearevst Neighbour Search
---

# A Living Literature Review of Learning-to-Hash for Nearest Neighbour Search

### Learning-to-Hash: Overview

With [Jeff Dean's](https://twitter.com/jeffdean/status/1063679694283857920?lang=en) recent keynote at [NeurIPS 2018](https://nips.cc/Conferences/2018), learned [index structures](https://dl.acm.org/citation.cfm?id=3196909) of which learning-to-hash is an important sub-field, are gaining much more prominence in the research literature. We have put together this website to help researchers learn about, share and more easily discover recent work in the field. Select "All Papers" on the righthand menu to get started.

<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### Background

*[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the problem of finding the most similar data-points to a query in a large database, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision. An obvious way of finding similar data-points would simply be to search through the entire dataset comparing each data-point to the query. Unfortunately, for most datasets of practical interest, particularly in the age of big-data and deep learning, this brute-force search is too computationally expensive and much more efficient search methods are required.

Learning2hash provides curated links to a host of *approximate nearest neighbour search* (ANN) models that permit constant-time retrieval of nearest neighbours, independent of the dataset size. Typically these algorithms generate similar binary hashcodes for similar data-points, with these hashcodes then used as the indices into the buckets of hashtables, yielding a query time that is substantially improved over an exhaustive comparison. The only downside to these models is they might not return the closest nearest neighbour every time, which is usually an acceptable trade-off in practice. We give a particular focus here on recently proposed approximate nearest neighbour search models that improve retrieval effectiveness by learning *task specific* binary hashcodes.

Learning2hash is a *living literature review* that allows you explore the navigate the models in the field following a [taxonomy](\base-taxonomy) based on the fundamental properties of each model. New models can be added to this website by anyone simply by making a GitHub pull request [see *Contributing* below](contributing.html).

### Contributing

Learning-to-hash is a vibrant research field and is rapidly evolving, particularly with the recent surge in interest in deep neural network-based models. The purpose of this website is to augment the static literature review with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website simply create a markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).

