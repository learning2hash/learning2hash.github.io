---
layout: publication
title: 'RAMBO: Repeated And Merged Bloom Filter For Ultra-fast Multiple Set Membership
  Testing (MSMT) On Large-scale Data'
authors: Gaurav Gupta, Minghao Yan, Benjamin Coleman, R. A. Leo Elworth, Tharun Medini,
  Todd Treangen, Anshumali Shrivastava
conference: Arxiv
year: 2019
bibkey: gupta2019rambo
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.02611'}]
tags: ["Efficiency"]
short_authors: Gupta et al.
---
Multiple Set Membership Testing (MSMT) is a well-known problem in a variety
of search and query applications. Given a dataset of K different sets and a
query q, it aims to find all of the sets containing the query. Trivially, an
MSMT instance can be reduced to K membership testing instances, each with the
same q, leading to O(K) query time with a simple array of Bloom Filters. We
propose a data-structure called RAMBO (Repeated And Merged BloOm Filter) that
achieves O(\sqrt\{K\} log K) query time in expectation with an additional
worst-case memory cost factor of O(log K) beyond the array of Bloom Filters.
Due to this, RAMBO is a very fast and accurate data-structure. Apart from being
embarrassingly parallel, supporting cheap updates for streaming inputs, zero
false-negative rate, and low false-positive rate, RAMBO beats the
state-of-the-art approaches for genome indexing methods: COBS (Compact
bit-sliced signature index), Sequence Bloom Trees (a Bloofi based
implementation), HowDeSBT, SSBT, and document indexing methods like BitFunnel.
The proposed data-structure is simply a count-min sketch type arrangement of a
membership testing utility (Bloom Filter in our case). It indexes k-grams and
provides an approximate membership testing based search utility. The simplicity
of the algorithm and embarrassingly parallel architecture allows us to index a
170 TB genome dataset in a mere 14 hours on a cluster of 100 nodes while
competing methods require weeks.