---
layout: publication
title: Semisupervised Clustering By Queries And Locally Encodable Source Coding
authors: Arya Mazumdar, Soumyabrata Pal
conference: IEEE Transactions on Information Theory 2020
year: 2017
bibkey: mazumdar2017semisupervised
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.00507'}]
tags: []
short_authors: Arya Mazumdar, Soumyabrata Pal
---
Source coding is the canonical problem of data compression in information
theory. In a locally encodable source coding, each compressed bit depends on
only few bits of the input. In this paper, we show that a recently popular
model of semi-supervised clustering is equivalent to locally encodable source
coding. In this model, the task is to perform multiclass labeling of unlabeled
elements. At the beginning, we can ask in parallel a set of simple queries to
an oracle who provides (possibly erroneous) binary answers to the queries. The
queries cannot involve more than two (or a fixed constant number of) elements.
Now the labeling of all the elements (or clustering) must be performed based on
the noisy query answers. The goal is to recover all the correct labelings while
minimizing the number of such queries. The equivalence to locally encodable
source codes leads us to find lower bounds on the number of queries required in
a variety of scenarios. We provide querying schemes based on pairwise `same
cluster' queries - and pairwise AND queries and show provable performance
guarantees for each of the schemes.