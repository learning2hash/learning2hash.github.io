---
layout: publication
title: Clustering-correcting Codes
authors: Tal Shinkar, Eitan Yaakobi, Andreas Lenz, Antonia Wachter-Zeh
conference: 2019 IEEE International Symposium on Information Theory (ISIT)
year: 2019
bibkey: shinkar2019clustering
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.04122'}]
tags: ["Compact Codes"]
short_authors: Shinkar et al.
---
A new family of codes, called clustering-correcting codes, is presented in
this paper. This family of codes is motivated by the special structure of data
that is stored in DNA-based storage systems. The data stored in these systems
has the form of unordered sequences, also called strands, and every strand is
synthesized thousands to millions of times, where some of these copies are read
back during sequencing. Due to the unordered structure of the strands, an
important task in the decoding process is to place them in their correct order.
This is usually accomplished by allocating a part of the strand for an index.
However, in the presence of errors in the index field, important information on
the order of the strands may be lost.
  Clustering-correcting codes ensure that if the distance between the index
fields of two strands is small, then there will be a large distance between
their data fields. It is shown how this property enables to place the strands
together in their correct clusters even in the presence of errors. We present
lower and upper bounds on the size of clustering-correcting codes and an
explicit construction of these codes which uses only a single bit of
redundancy.