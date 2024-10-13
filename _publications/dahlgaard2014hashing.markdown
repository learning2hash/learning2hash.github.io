---
layout: publication
title: Hashing For Statistics Over K-partitions
authors: Dahlgaard Søren, Knudsen Mathias Bæk Tejs, Rotenberg Eva, Thorup Mikkel
conference: "Arxiv"
year: 2014
bibkey: dahlgaard2014hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1411.7191"}
tags: ['ARXIV', 'FOCS', 'Independent']
---
<p>In this paper we analyze a hash function for <span
class="math inline">\(k\)</span>-partitioning a set into bins, obtaining
strong concentration bounds for standard algorithms combining statistics
from each bin. This generic method was originally introduced by Flajolet
and Martin~[FOCS’83] in order to save a factor <span
class="math inline">\(\Omega(k)\)</span> of time per element over <span
class="math inline">\(k\)</span> independent samples when estimating the
number of distinct elements in a data stream. It was also used in the
widely used HyperLogLog algorithm of Flajolet et al.~[AOFA’97] and in
large-scale machine learning by Li et al.~[NIPS’12] for minwise
estimation of set similarity. The main issue of <span
class="math inline">\(k\)</span>-partition, is that the contents of
different bins may be highly correlated when using popular hash
functions. This means that methods of analyzing the marginal
distribution for a single bin do not apply. Here we show that a
tabulation based hash function, mixed tabulation, does yield strong
concentration bounds on the most popular applications of <span
class="math inline">\(k\)</span>-partitioning similar to those we would
get using a truly random hash function. The analysis is very involved
and implies several new results of independent interest for both simple
and double tabulation, e.g. a simple and efficient construction for
invertible bloom filters and uniform hashing on a given set.</p>
