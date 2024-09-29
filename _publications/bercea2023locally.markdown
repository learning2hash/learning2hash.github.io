---
layout: publication
title: Locally Uniform Hashing
authors: Bercea Ioana O., Beretta Lorenzo, Klausen Jonas, Houen Jakob Bæk Tejs, Thorup Mikkel
conference: "Arxiv"
year: 2023
bibkey: bercea2023locally
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2308.14134"}
tags: ['ARXIV', 'Independent']
---
Hashing is a common technique used in data processing with a strong impact on the time and resources spent on computation. Hashing also affects the applicability of theoretical results that often assume access to (unrealistic) uniform/fully45;random hash functions. In this paper we are concerned with designing hash functions that are practical and come with strong theoretical guarantees on their performance. To this end we present tornado tabulation hashing which is simple fast and exhibits a certain full local randomness property that provably makes diverse algorithms perform almost as if (abstract) fully45;random hashing was used. For example this includes classic linear probing the widely used HyperLogLog algorithm of Flajolet Fusy Gandouet Meunier AOFA 97 for counting distinct elements and the one45;permutation hashing of Li Owen and Zhang NIPS 12 for large45;scale machine learning. We also provide a very efficient solution for the classical problem of obtaining fully45;random hashing on a fixed (but unknown to the hash function) set of n keys using O(n) space. As a consequence we get more efficient implementations of the splitting trick of Dietzfelbinger and Rink ICALP09 and the succinct space uniform hashing of Pagh and Pagh SICOMP08. Tornado tabulation hashing is based on a simple method to systematically break dependencies in tabulation45;based hashing techniques.
