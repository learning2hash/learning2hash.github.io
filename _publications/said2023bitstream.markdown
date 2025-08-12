---
layout: publication
title: Bitstream Organization For Parallel Entropy Coding On Neural Network-based
  Video Codecs
authors: Amir Said, Hoang Le, Farzad Farhadzadeh
conference: 2023 IEEE International Symposium on Multimedia (ISM)
year: 2023
bibkey: said2023bitstream
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.00921'}]
tags: ["Efficiency"]
short_authors: Amir Said, Hoang Le, Farzad Farhadzadeh
---
Video compression systems must support increasing bandwidth and data
throughput at low cost and power, and can be limited by entropy coding
bottlenecks. Efficiency can be greatly improved by parallelizing coding, which
can be done at much larger scales with new neural-based codecs, but with some
compression loss related to data organization. We analyze the bit rate overhead
needed to support multiple bitstreams for concurrent decoding, and for its
minimization propose a method for compressing parallel-decoding entry points,
using bidirectional bitstream packing, and a new form of jointly optimizing
arithmetic coding termination. It is shown that those techniques significantly
lower the overhead, making it easier to reduce it to a small fraction of the
average bitstream size, like, for example, less than 1% and 0.1% when the
average number of bitstream bytes is respectively larger than 95 and 1,200
bytes.