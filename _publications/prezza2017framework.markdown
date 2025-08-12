---
layout: publication
title: A Framework Of Dynamic Data Structures For String Processing
authors: Nicola Prezza
conference: Arxiv
year: 2017
bibkey: prezza2017framework
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.07238'}]
tags: ["Tools & Libraries"]
short_authors: Nicola Prezza
---
In this paper we present DYNAMIC, an open-source C++ library implementing
dynamic compressed data structures for string manipulation. Our framework
includes useful tools such as searchable partial sums, succinct/gap-encoded
bitvectors, and entropy/run-length compressed strings and FM-indexes. We prove
close-to-optimal theoretical bounds for the resources used by our structures,
and show that our theoretical predictions are empirically tightly verified in
practice. To conclude, we turn our attention to applications. We compare the
performance of four recently-published compression algorithms implemented using
DYNAMIC with those of state-of-the-art tools performing the same task. Our
experiments show that algorithms making use of dynamic compressed data
structures can be up to three orders of magnitude more space-efficient (albeit
slower) than classical ones performing the same tasks.