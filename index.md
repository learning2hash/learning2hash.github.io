---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearest Neighbour Search
---

Nearest neighbour search is the problem of finding the most similar data-points to a query in a large database, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision.

This website has links to a host of approximate nearest neighbour search algorithms that permit constant-time retrieval of nearest neighbours, independent of the dataset size. Typically these algorithms generate similar binary hashcodes for similar data-points, with these hashcodes then used as the indices into the buckets of hashtables, yielding a query time that is substantially improved over an exhaustive comparison.

This website is a *living literature review* that allows you explore the navigate the models in the field following a [taxonomy](\taxnomomy) based on the fundamental properties of each model. It contains links to a host of recently proposed approximate nearest neighbour search algorithms that improve retrieval effectiveness by learning *task specific* binary hashcodes. New models can be added to this website by anyone simply by making a GitHub pull request (see *Contributing* below).

This website and the accompanying literature review form a useful primer of the main concepts of learning-to-hash for those just entering the field and a reference for more established researchers and practioners in academia and industry alike.

The full survey is available [as a research paper](https//).
Please cite as
<pre>
@article{moran2017survey,
  title={A Primer on Learning to Hash for Approximate Nearest Neighbour Search},
  author={Moran, Sean},
  journal={arXiv preprint arXiv:1709.06182},
  year={2017}
}
</pre>


This site has been inspired and forked from the original living literature review of [Allamanis](https://ml4code.github.io).

### Contributing

Learning-to-hash is a vibrant research field and is rapidly evolving, particularly with the recent surge in interest in deep neural network-based models. The purpose of this website is to augment the static literature review with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website simply create a markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).
