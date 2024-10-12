---
layout: publication
title: Pthash Revisiting FCH Minimal Perfect Hashing
authors: Pibiri Giulio Ermanno, Trani Roberto
conference: "SIGIR"
year: 2021
bibkey: pibiri2021pthash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.10402"}
tags: ['Independent', 'SIGIR']
---
Given a set \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} distinct keys, a function \{&#37; raw &#37;\}\\(f\\)\{&#37; endraw &#37;\} that bijectively maps the keys of \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} into the range \{&#37; raw &#37;\}\\(\\{0,\ldots,n-1\\}\\)\{&#37; endraw &#37;\} is called a minimal perfect hash function for \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\}. Algorithms that find such functions when \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} is large and retain constant evaluation time are of practical interest; for instance, search engines and databases typically use minimal perfect hash functions to quickly assign identifiers to static sets of variable-length keys such as strings. The challenge is to design an algorithm which is efficient in three different aspects: time to find \{&#37; raw &#37;\}\\(f\\)\{&#37; endraw &#37;\} (construction time), time to evaluate \{&#37; raw &#37;\}\\(f\\)\{&#37; endraw &#37;\} on a key of \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} (lookup time), and space of representation for \{&#37; raw &#37;\}\\(f\\)\{&#37; endraw &#37;\}. Several algorithms have been proposed to trade-off between these aspects. In 1992, Fox, Chen, and Heath (FCH) presented an algorithm at SIGIR providing very fast lookup evaluation. However, the approach received little attention because of its large construction time and higher space consumption compared to other subsequent techniques. Almost thirty years later we revisit their framework and present an improved algorithm that scales well to large sets and reduces space consumption altogether, without compromising the lookup time. We conduct an extensive experimental assessment and show that the algorithm finds functions that are competitive in space with state-of-the art techniques and provide \{&#37; raw &#37;\}\\(2-4\times\\)\{&#37; endraw &#37;\} better lookup time.
