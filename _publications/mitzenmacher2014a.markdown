---
layout: publication
title: A New Approach to Analyzing Robin Hood Hashing
authors: Mitzenmacher Michael
conference: "Arxiv"
year: 2014
bibkey: mitzenmacher2014a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1401.7616"}
tags: ['ARXIV']
---
Robin Hood hashing is a variation on open addressing hashing designed to reduce the maximum search time as well as the variance in the search time for elements in the hash table. While the case of insertions only using Robin Hood hashing is well understood, the behavior with deletions has remained open. Here we show that Robin Hood hashing can be analyzed under the framework of finite-level finite-dimensional jump Markov chains. This framework allows us to re-derive some past results for the insertion-only case with some new insight, as well as provide a new analysis for a standard deletion model, where we alternate between deleting a random old key and inserting a new one. In particular, we show that a simple but apparently unstudied approach for handling deletions with Robin Hood hashing offers good performance even under high loads.
