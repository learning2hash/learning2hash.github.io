---
layout: publication
title: An Elegant Algorithm For The Construction Of Suffix Arrays
authors: Sanguthevar Rajasekaran, Marius Nicolae
conference: Journal of Discrete Algorithms
year: 2014
bibkey: rajasekaran2013elegant
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1307.1417'}]
tags: ["Efficiency"]
short_authors: Sanguthevar Rajasekaran, Marius Nicolae
---
The suffix array is a data structure that finds numerous applications in
string processing problems for both linguistic texts and biological data. It
has been introduced as a memory efficient alternative for suffix trees. The
suffix array consists of the sorted suffixes of a string. There are several
linear time suffix array construction algorithms (SACAs) known in the
literature. However, one of the fastest algorithms in practice has a worst case
run time of \\(O(n^2)\\). The problem of designing practically and theoretically
efficient techniques remains open. In this paper we present an elegant
algorithm for suffix array construction which takes linear time with high
probability; the probability is on the space of all possible inputs. Our
algorithm is one of the simplest of the known SACAs and it opens up a new
dimension of suffix array construction that has not been explored until now.
Our algorithm is easily parallelizable. We offer parallel implementations on
various parallel models of computing. We prove a lemma on the \\(\ell\\)-mers of a
random string which might find independent applications. We also present
another algorithm that utilizes the above algorithm. This algorithm is called
RadixSA and has a worst case run time of \\(O(nlog\{n\})\\). RadixSA introduces an
idea that may find independent applications as a speedup technique for other
SACAs. An empirical comparison of RadixSA with other algorithms on various
datasets reveals that our algorithm is one of the fastest algorithms to date.
The C++ source code is freely available at
http://www.engr.uconn.edu/~man09004/radixSA.zip