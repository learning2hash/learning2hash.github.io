---
layout: publication
title: The Power of Simple Tabulation Hashing
authors: Patrascu Mihai, Thorup Mikkel
conference: "Arxiv"
year: 2010
bibkey: patrascu2010power
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1011.5200"}
tags: ['ARXIV']
---
Randomized algorithms are often enjoyed for their simplicity but the hash functions used to yield the desired theoretical guarantees are often neither simple nor practical. Here we show that the simplest possible tabulation hashing provides unexpectedly strong guarantees. The scheme itself dates back to Carter and Wegman (STOC77). Keys are viewed as consisting of c characters. We initialize c tables T_1 ... T_c mapping characters to random hash codes. A key x=(x_1 ... x_q) is hashed to T_1x_1 xor ... xor T_cx_c. While this scheme is not even 4-independent we show that it provides many of the guarantees that are normally obtained via higher independence e.g. Chernoff-type concentration min-wise hashing for estimating set intersection and cuckoo hashing.
