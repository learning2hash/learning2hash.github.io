---
layout: publication
title: Improved Batch Code Lower Bounds
authors: Ray Li, Mary Wootters
conference: 2022 IEEE International Symposium on Information Theory (ISIT)
year: 2022
bibkey: li2021improved
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.02163'}]
tags: ["Compact Codes"]
short_authors: Ray Li, Mary Wootters
---
Batch codes are a useful notion of locality for error correcting codes,
originally introduced in the context of distributed storage and cryptography.
Many constructions of batch codes have been given, but few lower bound
(limitation) results are known, leaving gaps between the best known
constructions and best known lower bounds. Towards determining the optimal
redundancy of batch codes, we prove a new lower bound on the redundancy of
batch codes. Specifically, we study (primitive, multiset) linear batch codes
that systematically encode \\(n\\) information symbols into \\(N\\) codeword symbols,
with the requirement that any multiset of \\(k\\) symbol requests can be obtained
in disjoint ways. We show that such batch codes need \\(Ω(\sqrt\{Nk\})\\)
symbols of redundancy, improving on the previous best lower bounds of
\\(Ω(\sqrt\{N\}+k)\\) at all \\(k=n^\epsilon\\) with \\(\epsilon\in(0,1)\\). Our
proof follows from analyzing the dimension of the order-\\(O(k)\\) tensor of the
batch code's dual code.