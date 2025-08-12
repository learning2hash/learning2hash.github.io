---
layout: publication
title: Faster Privacy-preserving Computation Of Edit Distance With Moves
authors: Yohei Yoshimoto, Masaharu Kataoka, Yoshimasa Takabatake, Tomohiro I, Kilho
  Shin, Hiroshi Sakamoto
conference: Lecture Notes in Computer Science
year: 2020
bibkey: yoshimoto2019faster
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.10719'}]
tags: []
short_authors: Yoshimoto et al.
---
We consider an efficient two-party protocol for securely computing the
similarity of strings w.r.t. an extended edit distance measure. Here, two
parties possessing strings \\(x\\) and \\(y\\), respectively, want to jointly compute
an approximate value for \\(\mathrm\{EDM\}(x,y)\\), the minimum number of edit
operations including substring moves needed to transform \\(x\\) into \\(y\\), without
revealing any private information. Recently, the first secure two-party
protocol for this was proposed, based on homomorphic encryption, but this
approach is not suitable for long strings due to its high communication and
round complexities. In this paper, we propose an improved algorithm that
significantly reduces the round complexity without sacrificing its
cryptographic strength. We examine the performance of our algorithm for DNA
sequences compared to previous one.