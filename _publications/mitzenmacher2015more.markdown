---
layout: publication
title: More Analysis Of Double Hashing For Balanced Allocations
authors: Mitzenmacher Michael
conference: "Arxiv"
year: 2015
bibkey: mitzenmacher2015more
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.00658"}
tags: ['ARXIV', 'Independent']
---
With double hashing, for a key \{&#37; raw &#37;\}\\(x\\)\{&#37; endraw &#37;\}, one generates two hash values \{&#37; raw &#37;\}\\(f(x)\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(g(x)\\)\{&#37; endraw &#37;\}, and then uses combinations \{&#37; raw &#37;\}\\((f(x) +i g(x)) \bmod n\\)\{&#37; endraw &#37;\} for \{&#37; raw &#37;\}\\(i=0,1,2,...\\)\{&#37; endraw &#37;\} to generate multiple hash values in the range \{&#37; raw &#37;\}\\([0,n-1]\\)\{&#37; endraw &#37;\} from the initial two. For balanced allocations, keys are hashed into a hash table where each bucket can hold multiple keys, and each key is placed in the least loaded of \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\} choices. It has been shown previously that asymptotically the performance of double hashing and fully random hashing is the same in the balanced allocation paradigm using fluid limit methods. Here we extend a coupling argument used by Lueker and Molodowitch to show that double hashing and ideal uniform hashing are asymptotically equivalent in the setting of open address hash tables to the balanced allocation setting, providing further insight into this phenomenon. We also discuss the potential for and bottlenecks limiting the use this approach for other multiple choice hashing schemes.
