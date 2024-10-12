---
layout: publication
title: Near Neighbor Who Is The Fairest Of Them All
authors: Sariel Har-peled, Sepideh Mahabadi
conference: "Neural Information Processing Systems"
year: 2019
bibkey: harpeled2019near
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2019/hash/742141ceda6b8f6786609d31c8ef129f-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
In this work we study a fair variant of the near neighbor problem. Namely, given a set of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} points \{&#37; raw &#37;\}\\(P\\)\{&#37; endraw &#37;\} and a parameter \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}, the goal is to preprocess the points, such that given a query point \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}, any point in the \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-neighborhood of the query, i.e., \{&#37; raw &#37;\}\\(B(q,r)\\)\{&#37; endraw &#37;\}, have the same probability of being reported as the near neighbor. We show that LSH based algorithms can be made fair, without a significant loss in efficiency. Specifically, we show an algorithm that reports a point \{&#37; raw &#37;\}\\(p\\)\{&#37; endraw &#37;\} in the \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}-neighborhood of a query \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\} with almost uniform probability. The time to report such a point is proportional to \{&#37; raw &#37;\}\\(O(\dns(q.r) Q(n,c))\\)\{&#37; endraw &#37;\}, and its space is \{&#37; raw &#37;\}\\(O(S(n,c))\\)\{&#37; endraw &#37;\}, where \{&#37; raw &#37;\}\\(Q(n,c)\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(S(n,c)\\)\{&#37; endraw &#37;\} are the query time and space of an LSH algorithm for \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}-approximate near neighbor, and \{&#37; raw &#37;\}\\(\dns(q,r)\\)\{&#37; endraw &#37;\} is a function of the local density around \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}. Our approach works more generally for sampling uniformly from a sub-collection of sets of a given collection and can be used in a few other applications. Finally, we run experiments to show performance of our approach on real data.
