---
layout: publication
title: Compactness Of Hashing Modes And Efficiency Beyond Merkle Tree
authors: Andreeva Elena, Bhattacharyya Rishiraj, Roy Arnab
conference: "Arxiv"
year: 2021
bibkey: andreeva2021compactness
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.15055"}
tags: ['ARXIV', 'Graph', 'Independent']
---
We revisit the classical problem of designing optimally efficient
cryptographically secure hash functions. Hash functions are traditionally
designed via applying modes of operation on primitives with smaller domains.
The results of Shrimpton and Stam (ICALP 2008), Rogaway and Steinberger (CRYPTO
2008), and Mennink and Preneel (CRYPTO 2012) show how to achieve optimally
efficient designs of \\(2n\\)-to-\\(n\\)-bit compression functions from non-compressing
primitives with asymptotically optimal \\(2^\{n/2-\epsilon\}\\)-query collision
resistance. Designing optimally efficient and secure hash functions for larger
domains (\\(> 2n\\) bits) is still an open problem.
  In this work we propose the new \textit\{compactness\} efficiency notion. It
allows us to focus on asymptotically optimally collision resistant hash
function and normalize their parameters based on Stam's bound from CRYPTO 2008
to obtain maximal efficiency.
  We then present two tree-based modes of operation
  -Our first construction is an \underline\{A\}ugmented \underline\{B\}inary
T\underline\{r\}ee (ABR) mode. The design is a \\((2^\{\ell\}+2^\{\ell-1\}
-1)n\\)-to-\\(n\\)-bit hash function making a total of \\((2^\{\ell\}-1)\\) calls to
\\(2n\\)-to-\\(n\\)-bit compression functions for any \\(\ell\geq 2\\). Our construction is
optimally compact with asymptotically (optimal) \\(2^\{n/2-\epsilon\}\\)-query
collision resistance in the ideal model. For a tree of height \\(\ell\\), in
comparison with Merkle tree, the \\(ABR\\) mode processes additional
\\((2^\{\ell-1\}-1)\\) data blocks making the same number of internal compression
function calls.
  -While the \\(ABR\\) mode achieves collision resistance, it fails to achieve
indifferentiability from a random oracle within \\(2^\{n/3\}\\) queries. \\(ABR^\{+\}\\)
compresses only \\(1\\) less data block than \\(ABR\\) with the same number of
compression calls and achieves in addition indifferentiability up to
\\(2^\{n/2-\epsilon\}\\) queries.
