---
layout: publication
title: 'Recoil: Parallel Rans Decoding With Decoder-adaptive Scalability'
authors: Fangzheng Lin, Kasidis Arunruangsirilert, Heming Sun, Jiro Katto
conference: Proceedings of the 52nd International Conference on Parallel Processing
year: 2023
bibkey: lin2023recoil
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.12141'}]
tags: ["Scalability"]
short_authors: Lin et al.
---
Entropy coding is essential to data compression, image and video coding, etc.
The Range variant of Asymmetric Numeral Systems (rANS) is a modern entropy
coder, featuring superior speed and compression rate. As rANS is not designed
for parallel execution, the conventional approach to parallel rANS partitions
the input symbol sequence and encodes partitions with independent codecs, and
more partitions bring extra overhead. This approach is found in
state-of-the-art implementations such as DietGPU. It is unsuitable for
content-delivery applications, as the parallelism is wasted if the decoder
cannot decode all the partitions in parallel, but all the overhead is still
transferred.
  To solve this, we propose Recoil, a parallel rANS decoding approach with
decoder-adaptive scalability. We discover that a single rANS-encoded bitstream
can be decoded from any arbitrary position if the intermediate states are
known. After renormalization, these states also have a smaller upper bound,
which can be stored efficiently. We then split the encoded bitstream using a
heuristic to evenly distribute the workload, and store the intermediate states
and corresponding symbol indices as metadata. The splits can then be combined
simply by eliminating extra metadata entries.
  The main contribution of Recoil is reducing unnecessary data transfer by
adaptively scaling parallelism overhead to match the decoder capability. The
experiments show that Recoil decoding throughput is comparable to the
conventional approach, scaling massively on CPUs and GPUs and greatly
outperforming various other ANS-based codecs.