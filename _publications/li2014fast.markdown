---
layout: publication
title: Fast Construction Of Fm-index For Long Sequence Reads
authors: Heng Li
conference: Bioinformatics
year: 2014
bibkey: li2014fast
citations: 80
additional_links: [{name: Code, url: 'https://github.com/lh3/ropebwt2'}, {name: Paper,
    url: 'https://arxiv.org/abs/1406.0426'}]
tags: []
short_authors: Heng Li
---
Summary: We present a new method to incrementally construct the FM-index for
both short and long sequence reads, up to the size of a genome. It is the first
algorithm that can build the index while implicitly sorting the sequences in
the reverse (complement) lexicographical order without a separate sorting step.
The implementation is among the fastest for indexing short reads and the only
one that practically works for reads of averaged kilobases in length.
  Availability and implementation: https://github.com/lh3/ropebwt2
  Contact: hengli@broadinstitute.org