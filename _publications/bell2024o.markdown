---
layout: publication
title: O(1) Insertion For Random Walk D-ary Cuckoo Hashing Up To The Load Threshold
authors: Tolson Bell, Alan Frieze
conference: 2024 IEEE 65th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2024
bibkey: bell2024o
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14394'}]
tags: ["Hashing Methods"]
short_authors: Tolson Bell, Alan Frieze
---
The random walk \(d\)-ary cuckoo hashing algorithm was defined by Fotakis,
Pagh, Sanders, and Spirakis to generalize and improve upon the standard cuckoo
hashing algorithm of Pagh and Rodler. Random walk \(d\)-ary cuckoo hashing has
low space overhead, guaranteed fast access, and fast in practice insertion
time. In this paper, we give a theoretical insertion time bound for this
algorithm. More precisely, for every \(d\ge 3\) hashes, let \(c_d^*\) be the sharp
threshold for the load factor at which a valid assignment of \(cm\) objects to a
hash table of size \(m\) likely exists. We show that for any \(d\ge 4\) hashes and
load factor \(c<c_d^*\), the expectation of the random walk insertion time is
\(O(1)\), that is, a constant depending only on \(d\) and \(c\) but not \(m\).