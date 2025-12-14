---
layout: publication
title: Lossless Compression Of Vector Ids For Approximate Nearest Neighbor Search
authors: Daniel Severo, Giuseppe Ottaviano, Matthew Muckley, Karen Ullrich, Matthijs
  Douze
conference: Arxiv
year: 2025
bibkey: severo2025lossless
citations: 0
additional_links: [{name: Code, url: 'https://github.com/facebookresearch/vector_db_id_compression'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.10479'}]
tags: [Vector Indexing, Graph-based ANN, Datasets, Quantization, Memory Efficiency,
  Scalability, Large-Scale Search]
short_authors: Severo et al.
---
Approximate nearest neighbor search for vectors relies on indexes that are
most often accessed from RAM. Therefore, storage is the factor limiting the
size of the database that can be served from a machine. Lossy vector
compression, i.e., embedding quantization, has been applied extensively to
reduce the size of indexes. However, for inverted file and graph-based indices,
auxiliary data such as vector ids and links (edges) can represent most of the
storage cost. We introduce and evaluate lossless compression schemes for these
cases. These approaches are based on asymmetric numeral systems or wavelet
trees that exploit the fact that the ordering of ids is irrelevant within the
data structures. In some settings, we are able to compress the vector ids by a
factor 7, with no impact on accuracy or search runtime. On billion-scale
datasets, this results in a reduction of 30% of the index size. Furthermore, we
show that for some datasets, these methods can also compress the quantized
vector codes losslessly, by exploiting sub-optimalities in the original
quantization algorithm. The source code for our approach available at
https://github.com/facebookresearch/vector_db_id_compression.