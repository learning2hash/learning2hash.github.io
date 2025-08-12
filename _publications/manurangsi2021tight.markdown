---
layout: publication
title: Tight Bounds For Differentially Private Anonymized Histograms
authors: Pasin Manurangsi
conference: Symposium on Simplicity in Algorithms (SOSA)
year: 2022
bibkey: manurangsi2021tight
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.03257'}]
tags: []
short_authors: Pasin Manurangsi
---
In this note, we consider the problem of differentially privately (DP)
computing an anonymized histogram, which is defined as the multiset of counts
of the input dataset (without bucket labels). In the low-privacy regime
\\(\epsilon \geq 1\\), we give an \\(\epsilon\\)-DP algorithm with an expected
\\(\ell_1\\)-error bound of \\(O(\sqrt\{n\} / e^\epsilon)\\). In the high-privacy regime
\\(\epsilon < 1\\), we give an \\(Ω(\sqrt\{n log(1/\epsilon) / \epsilon\})\\) lower
bound on the expected \\(\ell_1\\) error. In both cases, our bounds asymptotically
match the previously known lower/upper bounds due to [Suresh, NeurIPS 2019].