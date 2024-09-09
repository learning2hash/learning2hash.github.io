---
layout: publication
title: Cascade hash tables a series of multilevel double hashing schemes with O(1) worst case lookup time
authors: Li Shaohua
conference: "Arxiv"
year: 2006
bibkey: li2006cascade
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0608037"}
tags: ['ARXIV']
---
In this paper, the author proposes a series of multilevel double hashing schemes called cascade hash tables. They use several levels of hash tables. In each table, we use the common double hashing scheme. Higher level hash tables work as fail-safes of lower level hash tables. By this strategy, it could effectively reduce collisions in hash insertion. Thus it gains a constant worst case lookup time with a relatively high load factor(70%-85%) in random experiments. Different parameters of cascade hash tables are tested.
