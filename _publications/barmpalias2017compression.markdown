---
layout: publication
title: Compression Of Data Streams Down To Their Information Content
authors: George Barmpalias, Andrew Lewis-pye
conference: IEEE Transactions on Information Theory
year: 2019
bibkey: barmpalias2017compression
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.02092'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: George Barmpalias, Andrew Lewis-pye
---
According to Kolmogorov complexity, every finite binary string is
compressible to a shortest code -- its information content -- from which it is
effectively recoverable. We investigate the extent to which this holds for
infinite binary sequences (streams). We devise a new coding method which
uniformly codes every stream \\(X\\) into an algorithmically random stream \\(Y\\), in
such a way that the first \\(n\\) bits of \\(X\\) are recoverable from the first
\\(I(X\upharpoonright_n)\\) bits of \\(Y\\), where \\(I\\) is any partial computable
information content measure which is defined on all prefixes of \\(X\\), and where
\\(X\upharpoonright_n\\) is the initial segment of \\(X\\) of length \\(n\\). As a
consequence, if \\(g\\) is any computable upper bound on the initial segment
prefix-free complexity of \\(X\\), then \\(X\\) is computable from an algorithmically
random \\(Y\\) with oracle-use at most \\(g\\). Alternatively (making no use of such a
computable bound \\(g\\)) one can achieve an oracle-use bounded above by
\\(K(X\upharpoonright_n)+log n\\). This provides a strong analogue of Shannon's
source coding theorem for algorithmic information theory.