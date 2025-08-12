---
layout: publication
title: Scalable String Reconciliation By Recursive Content-dependent Shingling
authors: Bowen Song, Ari Trachtenberg
conference: 2019 57th Annual Allerton Conference on Communication, Control, and Computing
  (Allerton)
year: 2019
bibkey: song2019scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.00536'}]
tags: ["Scalability"]
short_authors: Bowen Song, Ari Trachtenberg
---
We consider the problem of reconciling similar, but remote, strings with
minimum communication complexity. This "string reconciliation" problem is a
fundamental building block for a variety of networking applications, including
those that maintain large-scale distributed networks and perform remote file
synchronization. We present the novel Recursive Content-Dependent Shingling
(RCDS) protocol that is computationally practical for large strings and scales
linearly with the edit distance between the remote strings. We provide
comparisons to the performance of Rsync, one of the most popular file
synchronization tools in active use. Our experiments show that, with minimal
engineering, RCDS outperforms the heavily optimized Rsync in reconciling
release revisions for about 51% of the 5000 top starred git repositories on
GitHub. The improvement is particularly evident for repositories that see
frequent, but small, updates.