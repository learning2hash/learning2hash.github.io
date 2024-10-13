---
layout: publication
title: Fast Hashing With Strong Concentration Bounds
authors: Aamand Anders, Knudsen Jakob B. T., Knudsen Mathias B. T., Rasmussen Peter M. R., Thorup Mikkel
conference: "Arxiv"
year: 2019
bibkey: aamand2019fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1905.00369"}
tags: ['ARXIV']
---
<p>Previous work on tabulation hashing by Patrascu and Thorup from
STOC’11 on simple tabulation and from SODA’13 on twisted tabulation
offered Chernoff-style concentration bounds on hash based sums, e.g.,
the number of balls/keys hashing to a given bin, but under some quite
severe restrictions on the expected values of these sums. The basic idea
in tabulation hashing is to view a key as consisting of <span
class="math inline">\(c=O(1)\)</span> characters, e.g., a 64-bit key as
<span class="math inline">\(c=8\)</span> characters of 8-bits. The
character domain <span class="math inline">\(\Sigma\)</span> should be
small enough that character tables of size <span
class="math inline">\(|\Sigma|\)</span> fit in fast cache. The schemes
then use <span class="math inline">\(O(1)\)</span> tables of this size,
so the space of tabulation hashing is <span
class="math inline">\(O(|\Sigma|)\)</span>. However, the concentration
bounds by Patrascu and Thorup only apply if the expected sums are <span
class="math inline">\(\ll |\Sigma|\)</span>. To see the problem,
consider the very simple case where we use tabulation hashing to throw
<span class="math inline">\(n\)</span> balls into <span
class="math inline">\(m\)</span> bins and want to analyse the number of
balls in a given bin. With their concentration bounds, we are fine if
<span class="math inline">\(n=m\)</span>, for then the expected value is
<span class="math inline">\(1\)</span>. However, if <span
class="math inline">\(m=2\)</span>, as when tossing <span
class="math inline">\(n\)</span> unbiased coins, the expected value
<span class="math inline">\(n/2\)</span> is <span
class="math inline">\(\gg |\Sigma|\)</span> for large data sets, e.g.,
data sets that do not fit in fast cache. To handle expectations that go
beyond the limits of our small space, we need a much more advanced
analysis of simple tabulation, plus a new tabulation technique that we
call hashing which is at most twice as slow as simple tabulation. No
other hashing scheme of comparable speed offers similar Chernoff-style
concentration bounds.</p>
