---
layout: publication
title: Learned Monotone Minimal Perfect Hashing
authors: Paolo Ferragina, Hans-Peter Lehmann, Peter Sanders, Giorgio Vinciguerra
conference: Arxiv
year: 2023
bibkey: ferragina2023learned
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.11012'}]
tags: ["Hashing Methods", "Memory Efficiency"]
short_authors: Ferragina et al.
---
A Monotone Minimal Perfect Hash Function (MMPHF) constructed on a set S of
keys is a function that maps each key in S to its rank. On keys not in S, the
function returns an arbitrary value. Applications range from databases, search
engines, data encryption, to pattern-matching algorithms.
  In this paper, we describe LeMonHash, a new technique for constructing MMPHFs
for integers. The core idea of LeMonHash is surprisingly simple and effective:
we learn a monotone mapping from keys to their rank via an error-bounded
piecewise linear model (the PGM-index), and then we solve the collisions that
might arise among keys mapping to the same rank estimate by associating small
integers with them in a retrieval data structure (BuRR). On synthetic random
datasets, LeMonHash needs 34% less space than the next larger competitor, while
achieving about 16 times faster queries. On real-world datasets, the space
usage is very close to or much better than the best competitors, while
achieving up to 19 times faster queries than the next larger competitor. As far
as the construction of LeMonHash is concerned, we get an improvement by a
factor of up to 2, compared to the competitor with the next best space usage.
  We also investigate the case of keys being variable-length strings,
introducing the so-called LeMonHash-VL: it needs space within 13% of the best
competitors while achieving up to 3 times faster queries than the next larger
competitor.