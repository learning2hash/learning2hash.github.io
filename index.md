---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearest Neighbour Search
---

Nearest neighbour search is the problem of finding the most similar data-points to a query in a large database, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision.

This website has links to a host of important approximate nearest neighbour search algorithms that permit constant-time retrieval of nearest neighbours, independent of the dataset size. Typically these algorithms generate similar binary hashcodes for similar data-points, with these hashcodes then used as the indices into the buckets of hashtables, yielding a query time that is substantially improved over an exhaustive comparison.

This website is a living literature review that allows you explore the navigate the models in the field following a [taxonomy](\taxnomomy) based on the fundamental properties of each model. It contains links to a host of recently proposed approximate nearest neighbour search algorithms that improve retrieval effectiveness by learning task specific binary hashcodes.

The field is broadly categorised according to the standard two-step pipeline employed by many existing hashing models, namely projection and quantisation. The generation of a binary hashcode comprises two main steps carried out sequentially: *projection* of the data feature vector onto the normal vectors of a set of hyperplanes that fracture the input feature space followed by a *quantisation* operation that thresholds the projections to generate the binary hashcodes. The degree to which these two operations preserve the relative distances between the data-points in the input feature space has a direct influence on the effectiveness of using the resulting hashcodes for the task of nearest neighbour search.

This website and the accompanying literature review form a useful primer of the main concepts of learning-to-hash for those entering the field and a reference for more established researchers and practioners alike.

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


This site has been inspired by the original living literature review of [Allamanis](https://ml4code.github.io).

### Contributing

Learning-to-hash is a vibrant research field and is rapidly evolving, particularly with the surge in interest in deep learning models. The purpose of this website is to augment the static literature review with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website create a Markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).
