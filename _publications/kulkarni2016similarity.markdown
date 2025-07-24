---
layout: publication
title: Similarity Preserving Compressions Of High Dimensional Sparse Data
authors: Raghav Kulkarni, Rameshwar Pratap
conference: Arxiv
year: 2016
bibkey: kulkarni2016similarity
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06057'}]
tags: ["Datasets", "Distance Metric Learning"]
short_authors: Raghav Kulkarni, Rameshwar Pratap
---
The rise of internet has resulted in an explosion of data consisting of
millions of articles, images, songs, and videos. Most of this data is high
dimensional and sparse. The need to perform an efficient search for similar
objects in such high dimensional big datasets is becoming increasingly common.
Even with the rapid growth in computing power, the brute-force search for such
a task is impractical and at times impossible. Therefore it is quite natural to
investigate the techniques that compress the dimension of the data-set while
preserving the similarity between data objects.
  In this work, we propose an efficient compression scheme mapping binary
vectors into binary vectors and simultaneously preserving Hamming distance and
Inner Product. The length of our compression depends only on the sparsity and
is independent of the dimension of the data. Moreover our schemes provide
one-shot solution for Hamming distance and Inner Product, and work in the
streaming setting as well. In contrast with the "local projection" strategies
used by most of the previous schemes, our scheme combines (using sparsity) the
following two strategies: \\(1.\\) Partitioning the dimensions into several
buckets, \\(2.\\) Then obtaining "global linear summaries" in each of these
buckets. We generalize our scheme for real-valued data and obtain compressions
for Euclidean distance, Inner Product, and \\(k\\)-way Inner Product.