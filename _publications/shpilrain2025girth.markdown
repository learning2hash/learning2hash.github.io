---
layout: publication
title: 'Girth Of The Cayley Graph And Cayley Hash Functions'
authors: Vladimir Shpilrain
conference: "London Math. Soc. Newsletter (2025)"
year: 2025
citations: 0
bibkey: shpilrain2025girth
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2502.13197'}
tags: ['Hashing Fundamentals', 'Survey Paper', 'Hashing Methods', 'Survey']
---
Cayley hash functions are based on a simple idea of using a pair of semigroup
elements, A and B, to hash the 0 and 1 bit, respectively, and then to hash an
arbitrary bit string in the natural way, by using multiplication of elements in
the semigroup. The main advantage of Cayley hash functions compared to, say,
hash functions in the SHA family is that when an already hashed document is
amended, one does not have to hash the whole amended document all over again,
but rather hash just the amended part and then multiply the result by the hash
of the original document. In this article, we survey some of the previously
proposed Cayley hash functions and single out a very simple hash function whose
security has not been compromised up to date.
