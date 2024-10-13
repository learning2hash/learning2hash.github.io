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
In this work we study a "fair" variant of the near neighbor problem. Namely, given a set of \\{n\\} points \\{P\\} and a parameter \\{r\\}, the goal is to preprocess the points, such that given a query point \\{q\\}, any point in the \\{r\\}-neighborhood of the query, i.e., \\{B(q,r)\\}, have the same probability of being reported as the near neighbor.

We show that LSH based algorithms can be made fair, without a significant loss in efficiency. Specifically, we show an algorithm that reports a point \\{p\\} in the \\{r\\}-neighborhood of a query \\{q\\} with almost uniform probability.  The time to report such a point is proportional to \\{O(\dns(q.r) Q(n,c))\\}, and its space is \\{O(S(n,c))\\}, where \\{Q(n,c)\\} and \\{S(n,c)\\} are the query time and space of an LSH algorithm for \\{c\\}-approximate near neighbor, and \\{\dns(q,r)\\} is a function of the local density around \\{q\\}.

Our approach works more generally for sampling uniformly from a sub-collection of sets of a given collection and can be used in a few other applications. Finally, we run experiments to show performance of our approach on real data.
