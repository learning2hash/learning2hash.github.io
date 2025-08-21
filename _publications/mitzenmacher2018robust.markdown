---
layout: publication
title: Robust Set Reconciliation Via Locality Sensitive Hashing
authors: Michael Mitzenmacher, Tom Morgan
conference: Proceedings of the 38th ACM SIGMOD-SIGACT-SIGAI Symposium on Principles
  of Database Systems
year: 2019
bibkey: mitzenmacher2018robust
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.09694'}]
tags: ["Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Michael Mitzenmacher, Tom Morgan
---
We consider variations of set reconciliation problems where two parties,
Alice and Bob, each hold a set of points in a metric space, and the goal is for
Bob to conclude with a set of points that is close to Alice's set of points in
a well-defined way. This setting has been referred to as robust set
reconciliation. More specifically, in one variation we examine the goal is for
Bob to end with a set of points that is close to Alice's in earth mover's
distance, and in another the goal is for Bob to have a point that is close to
each of Alice's. The first problem has been studied before; our results scale
better with the dimension of the space. The second problem appears new.
  Our primary novelty is utilizing Invertible Bloom Lookup Tables in
combination with locality sensitive hashing. This combination allows us to cope
with the geometric setting in a communication-efficient manner.