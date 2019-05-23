---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearevst Neighbour Search
---

# A Living Literature Review of Learning-to-Hash for Nearest Neighbour Search

**Don't see your paper listed? A paper missing that you think really should be listed here? This website accepts reader contributions! Please see [these instructions for contributing](contributing.html)**

### Welcome

Welcome, you've found one of the internet's most comprehensive survey's on the exciting and fast changing field of learning-to-hash! With [Jeff Dean's](https://twitter.com/jeffdean/status/1063679694283857920?lang=en) recent keynote at [NeurIPS 2018](https://nips.cc/Conferences/2018), learned [index structures](https://dl.acm.org/citation.cfm?id=3196909) of which learning-to-hash is an important sub-field, is gaining more prominence in the research literature. We have put together this website to help researchers learn about, share and more easily discover recent work in the field. If you've enjoyed this resource or have feedback [we'd](mailto:sean.j.moran@gmail.com) be happy to hear from you.

### Background

*[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the problem of finding the most similar data-points to a query in a large database, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision. An obvious way of finding similar data-points would simply be to search through the entire dataset comparing each data-point to the query. Unfortunately, for most datasets of practical interest, particularly in the age of big-data and deep learning, this brute-force search is too computationally expensive and much more efficient search methods are required.

Learning2hash provides curated links to a host of *approximate nearest neighbour search* (ANN) models that permit constant-time retrieval of nearest neighbours, independent of the dataset size. Typically these algorithms generate similar binary hashcodes for similar data-points, with these hashcodes then used as the indices into the buckets of hashtables, yielding a query time that is substantially improved over an exhaustive comparison. The only downside to these models is they might not return the closest nearest neighbour every time, which is usually an acceptable trade-off in practice. We give a particular focus here on recently proposed approximate nearest neighbour search models that improve retrieval effectiveness by learning *task specific* binary hashcodes.

Learning2hash is in essence a *living literature review* that allows you explore the navigate the models in the field following a [taxonomy](\base-taxonomy) based on the fundamental properties of each model. New models can be added to this website by anyone simply by making a GitHub pull request (see *Contributing* below).

### Survey Paper

The full survey is available [as a research paper](http://seanjmoran.com/pdfs/hashing_review.pdf) currently under submission to a peer-reviewed journal. Full citation information will appear here in due course. In the meantime please cite the following thesis upon which the review is based:

<pre>
@phdthesis{Moran16,
  author       = {Sean Moran}, 
  title        = {Learning to hash for large-scale image retrieval},
  school       = {University of Edinburgh},
  year         = 2016,
}
</pre>

### Additional Learning Resources

Please also see the excellent [tutorial slides](https://cs.nju.edu.cn/lwj/slides/L2H.pdf) of [Dr. Wu-Jun Li](https://cs.nju.edu.cn/lwj/) for a nice introduction to the field.

[Dr Victor Lavrenko](https://www.youtube.com/user/victorlavrenko) has two excellent youtube videos [here](https://www.youtube.com/watch?v=Arni-zkqMBA) and [here](https://www.youtube.com/watch?v=dgH0NP8Qxa8), describing the basics of locality sensitive hashing (LSH). These are ideal for those just entering the field or curious how to apply the method to their problem domain.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Arni-zkqMBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

There are also alternative survey papers which are complementary to this one and take a different approach to summarising available research. The reader is encouraged to further explore the following publications:

* [Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)
* [A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)
* [Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)

### Contributing

Learning-to-hash is a vibrant research field and is rapidly evolving, particularly with the recent surge in interest in deep neural network-based models. The purpose of this website is to augment the static literature review with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website simply create a markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).

### Acknowledgements

This website has been forked from the original living literature review of [Allamanis](https://ml4code.github.io).
