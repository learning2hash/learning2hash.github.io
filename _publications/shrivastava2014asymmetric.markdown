---
layout: publication
title: "Asymmetric LSH (ALSH) for Sublinear Time Maximum Inner Product Search (MIPS)."
authors: A. Shrivastava, P. Li
conference: NIPS
year: 2014
bibkey: shrivastava2014asymmetric
additional_links:
   - {name: "PDF", url: "http://papers.nips.cc/paper/5329-asymmetric-lsh-alsh-for-sublinear-time-maximum-inner-product-search-mips.pdf"}
---
We present the first provably sublinear time hashing algorithm for approximate
Maximum Inner Product Search (MIPS). Searching with (un-normalized) inner
product as the underlying similarity measure is a known difficult problem and
finding hashing schemes for MIPS was considered hard. While the existing Locality
Sensitive Hashing (LSH) framework is insufficient for solving MIPS, in this
paper we extend the LSH framework to allow asymmetric hashing schemes. Our
proposal is based on a key observation that the problem of finding maximum inner
products, after independent asymmetric transformations, can be converted into
the problem of approximate near neighbor search in classical settings. This key
observation makes efficient sublinear hashing scheme for MIPS possible. Under
the extended asymmetric LSH (ALSH) framework, this paper provides an example
of explicit construction of provably fast hashing scheme for MIPS. Our proposed
algorithm is simple and easy to implement. The proposed hashing scheme
leads to significant computational savings over the two popular conventional LSH
schemes: (i) Sign Random Projection (SRP) and (ii) hashing based on p-stable
distributions for L2 norm (L2LSH), in the collaborative filtering task of item recommendations
on Netflix and Movielens (10M) datasets.
