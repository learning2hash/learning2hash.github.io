---
layout: publication
title: How Long Can Optimal Locally Repairable Codes Be?
authors: Venkatesan Guruswami, Chaoping Xing, Chen Yuan
conference: IEEE Transactions on Information Theory
year: 2019
bibkey: guruswami2018how
citations: 91
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.01064'}]
tags: ["Compact Codes"]
short_authors: Venkatesan Guruswami, Chaoping Xing, Chen Yuan
---
A locally repairable code (LRC) with locality \\(r\\) allows for the recovery of
any erased codeword symbol using only \\(r\\) other codeword symbols. A
Singleton-type bound dictates the best possible trade-off between the dimension
and distance of LRCs --- an LRC attaining this trade-off is deemed
*optimal*. Such optimal LRCs have been constructed over alphabets growing
linearly in the block length. Unlike the classical Singleton bound, however, it
was not known if such a linear growth in the alphabet size is necessary, or for
that matter even if the alphabet needs to grow at all with the block length.
Indeed, for small code distances \\(3,4\\), arbitrarily long optimal LRCs were
known over fixed alphabets.
  Here, we prove that for distances \\(d \ge 5\\), the code length \\(n\\) of an
optimal LRC over an alphabet of size \\(q\\) must be at most roughly \\(O(d q^3)\\).
For the case \\(d=5\\), our upper bound is \\(O(q^2)\\). We complement these bounds by
showing the existence of optimal LRCs of length
\\(Ω_\{d,r\}(q^\{1+1/\lfloor(d-3)/2\rfloor\})\\) when \\(d \le r+2\\). These bounds
match when \\(d=5\\), thus pinning down \\(n=\Theta(q^2)\\) as the asymptotically
largest length of an optimal LRC for this case.