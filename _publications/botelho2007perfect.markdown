---
layout: publication
title: Perfect Hashing For Data Management Applications
authors: Botelho Fabiano C., Pagh Rasmus, Ziviani Nivio
conference: "Arxiv"
year: 2007
bibkey: botelho2007perfect
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0702159"}
tags: ['ARXIV', 'Independent']
---
Perfect hash functions can potentially be used to compress data in connection
with a variety of data management tasks. Though there has been considerable
work on how to construct good perfect hash functions, there is a gap between
theory and practice among all previous methods on minimal perfect hashing. On
one side, there are good theoretical results without experimentally proven
practicality for large key sets. On the other side, there are the theoretically
analyzed time and space usage algorithms that assume that truly random hash
functions are available for free, which is an unrealistic assumption. In this
paper we attempt to bridge this gap between theory and practice, using a number
of techniques from the literature to obtain a novel scheme that is
theoretically well-understood and at the same time achieves an
order-of-magnitude increase in performance compared to previous ``practical''
methods. This improvement comes from a combination of a novel, theoretically
optimal perfect hashing scheme that greatly simplifies previous methods, and
the fact that our algorithm is designed to make good use of the memory
hierarchy. We demonstrate the scalability of our algorithm by considering a set
of over one billion URLs from the World Wide Web of average length 64, for
which we construct a minimal perfect hash function on a commodity PC in a
little more than 1 hour. Our scheme produces minimal perfect hash functions
using slightly more than 3 bits per key. For perfect hash functions in the
range \\(\\{0,...,2n-1\\}\\) the space usage drops to just over 2 bits per key (i.e.,
one bit more than optimal for representing the key). This is significantly
below of what has been achieved previously for very large values of \\(n\\).
