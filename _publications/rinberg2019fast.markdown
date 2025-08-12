---
layout: publication
title: Fast Concurrent Data Sketches
authors: Arik Rinberg, Alexander Spiegelman, Edward Bortnikov, Eshcar Hillel, Idit
  Keidar, Lee Rhodes, Hadar Serviansky
conference: Proceedings of the 2019 ACM Symposium on Principles of Distributed Computing
year: 2019
bibkey: rinberg2019fast
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.10995'}]
tags: ["Efficiency", "Scalability"]
short_authors: Rinberg et al.
---
Data sketches are approximate succinct summaries of long streams. They are
widely used for processing massive amounts of data and answering statistical
queries about it in real-time. Existing libraries producing sketches are very
fast, but do not allow parallelism for creating sketches using multiple threads
or querying them while they are being built. We present a generic approach to
parallelising data sketches efficiently, while bounding the error that such
parallelism introduces. Utilising relaxed semantics and the notion of strong
linearisability we prove our algorithm's correctness and analyse the error it
induces in two specific sketches. Our implementation achieves high scalability
while keeping the error small.