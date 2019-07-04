---
layout: publication
title: "The Power of Asymmetry in Binary Hashing"
authors: B. Neyshabur, R. Salakhutdinov, N. Srebro
conference: NIPS
year: 2013
bibkey: neyshabur2013power
additional_links:
   - {name: "PDF", url: "https://ttic.uchicago.edu/~yury/papers/nips2013_asym.pdf"}
   - {name: "Code", url: "https://ttic.uchicago.edu/~yury/papers/nips2013_asym.pdf"}
---
When approximating binary similarity using the hamming distance between short
binary hashes, we show that even if the similarity is symmetric, we can have
shorter and more accurate hashes by using two distinct code maps. I.e. by approximating the similarity between x and x
0
as the hamming distance between f(x)
and g(x0), for two distinct binary codes f, g, rather than as the hamming distance
between f(x) and f(x0).
