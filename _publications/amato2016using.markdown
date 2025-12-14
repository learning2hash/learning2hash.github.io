---
layout: publication
title: Using Apache Lucene To Search Vector Of Locally Aggregated Descriptors
authors: Giuseppe Amato, Paolo Bolettieri, Fabrizio Falchi, Claudio Gennaro, Lucia
  Vadicamo
conference: Proceedings of the 11th Joint Conference on Computer Vision, Imaging and
  Computer Graphics Theory and Applications
year: 2016
bibkey: amato2016using
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.05576'}]
tags: [Text Retrieval, Evaluation, Datasets, Similarity Search]
short_authors: Amato et al.
---
Surrogate Text Representation (STR) is a profitable solution to efficient
similarity search on metric space using conventional text search engines, such
as Apache Lucene. This technique is based on comparing the permutations of some
reference objects in place of the original metric distance. However, the
Achilles heel of STR approach is the need to reorder the result set of the
search according to the metric distance. This forces to use a support database
to store the original objects, which requires efficient random I/O on a fast
secondary memory (such as flash-based storages). In this paper, we propose to
extend the Surrogate Text Representation to specifically address a class of
visual metric objects known as Vector of Locally Aggregated Descriptors (VLAD).
This approach is based on representing the individual sub-vectors forming the
VLAD vector with the STR, providing a finer representation of the vector and
enabling us to get rid of the reordering phase. The experiments on a publicly
available dataset show that the extended STR outperforms the baseline STR
achieving satisfactory performance near to the one obtained with the original
VLAD vectors.