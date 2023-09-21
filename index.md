---
layout: default
title: Awesome Papers on Learning to Hash
comments: true
---

# Awesome Papers on Learning to Hash

### 🏷 Browse Papers by Tag

{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort %}
{% for tag in rawtags %}<tag><a href="/tags.html#{{ tag }}">{{ tag }}</a></tag> {% endfor %}

### The Field of Learning to Hash

This website exists to help researchers learn about, share and more easily discover recent work in the field of learning to hash. Awesome learning to hash is a *living literature review* that allows the reader to explore models in the field following a [taxonomy](\base-taxonomy) based on model properties. New models can be added to this website by anyone simply by filling out a form [see *Contributing* below](contributing.html). Select ["All Papers"](https://learning2hash.github.io/papers.html) on the right-hand menu to get started.

### Background

In general, *[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the problem of finding the most similar data-points to a query in a large database of data-points. Nearest neighbour search is a fundamental operation in computer science that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision. A selection of interesting and successful application areas include:

* [A Scalable Sourcecode Search Engine](https://arxiv.org/abs/2111.04473): Enabling code-to-code recommendation over large-scale sourcecode repositories with MinHash.
* [Making the Transformer from NLP much more efficient](https://openreview.net/pdf?id=rkgNKkHtvB): large Transformer models achieve state-of-the-art results but training these models can be costly. LSH to the rescue!
* [Detecting and Tracking Interesting Events on Social Media](https://www.aclweb.org/anthology/P14-5007): a real-time system incorporating LSH to detect and track interesting [social media events](http://seanjmoran.com/pdfs/sigir16_embeddings.pdf) over time.
* [Earthquake Hunting with Efficient Time Series Similarity Search](https://dawn.cs.stanford.edu/2018/09/05/quake/): detecting earthquakes by comparing segments of seismic activity time series. Some nice lessons learnt [here](http://www.vldb.org/pvldb/vol11/p1674-rong.pdf) about applying LSH in real-world applications.
* [Detecting Fraudulent Taxi Rides](https://eng.uber.com/lsh/): Uber has applied LSH to detect rides that are similar based on their spatial properties.
* [Audio Fingerprinting](https://santhoshhari.github.io/Locality-Sensitive-Hashing/) Matching a query snippet of audio to a large database (think Shazam!) can be achieved efficiently by using learning-to-hash methods.
* [Genomics](https://www.ncbi.nlm.nih.gov/pubmed/26006009): Locality sensitive hashing (LSH) is used by Biologists to assemble large genomes and to find genes with similar expression in genomic databases.
* [Image Retrieval](https://ai.google/research/pubs/pub34634): Google applies locality sensitive hashing (LSH) alongside [PageRank](https://en.wikipedia.org/wiki/PageRank) to index planet-scale collections of images.
* [Malware Detection](https://media.kaspersky.com/en/enterprise-security/Kaspersky-Lab-Whitepaper-Machine-Learning.pdf): Developers of anti-viral software use hashcode learning models to quickly match a possibly malign code snippet to a database of known viruses.

The list is truly endless! 

[Learning2hash](https://learning2hash.github.io/papers.html) provides a set of curated, community-driven links to a host of *approximate nearest neighbour search* (ANN) models that permit sublinear-time retrieval of nearest neighbours. Hashing models work by generating similar binary hashcodes for semantically similar data-points (illustrated by the diagram below). These similarity preserving hashcodes can then be used to index the data-points (images, documents etc) into the buckets of hashtables. Similar data-points should ideally end up in the same bucket of the hash table if we happen to have an effective hash function. This whole process is illustrated in the diagram below:

![Locality Sensitive Hashing (LSH)](/public/media/hashing.png?raw=true "Locality Sensitive 
Hashing (LSH)")

Diagram taken from the [PhD thesis of Sean Moran](https://learning2hash.github.io/cite.html).

Given a query, such as the image of the tiger in the example above, we can search for similar data-points by generating a hashcode for the query and only comparing the query data-point to the data-points that collide with it in the same hashtable bucket (or buckets if we have multiple independent hashtables). Usually the number of data-points in the colliding hash table bucket(s) should be much less than the total number of data-points in the entire dataset, yielding a query time that is substantially improved over a simple brute-force search. The only downside to these models is they might not return the closest nearest neighbour(s) every time (that is, we forgo a degree of accuracy), which is usually an acceptable trade-off in practice.

Much more introductory material on hashing and learning-to-hash can be found in [*Resources*](resources.html).

This literature review gives a particular focus on recently proposed approximate nearest neighbour search models that improve retrieval effectiveness by learning *task specific* hashcodes that are sensitive to the distribution of the data. All the papers listed in this review website suggest new methods for learning the hash functions to generate more effective similarity preserving hashcodes.

### Contributing

Learning to hash is rapidly evolving. The purpose of this website is to augment static literature reviews with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website simply create a markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).

Copyright © [Sean Moran](https://sjmoran.github.io/) 2023. All opinions are my own.


