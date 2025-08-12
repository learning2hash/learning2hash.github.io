---
layout: publication
title: Fast Sampling Based Sketches For Tensors
authors: William Swartworth, David P. Woodruff
conference: Arxiv
year: 2024
bibkey: swartworth2024fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.06735'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: William Swartworth, David P. Woodruff
---
We introduce a new approach for applying sampling-based sketches to two and
three mode tensors. We illustrate our technique to construct sketches for the
classical problems of \(\ell_0\) sampling and producing \(\ell_1\) embeddings. In
both settings we achieve sketches that can be applied to a rank one tensor in
\((\mathbb\{R\}^d)^\{\otimes q\}\) (for \(q=2,3\)) in time scaling with \(d\) rather than
\(d^2\) or \(d^3\). Our main idea is a particular sampling construction based on
fast convolution which allows us to quickly compute sums over sufficiently
random subsets of tensor entries.