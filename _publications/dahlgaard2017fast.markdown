---
layout: publication
title: Fast Similarity Sketching
authors: "S\xF8ren Dahlgaard, Mathias B\xE6k Tejs Langhede, Jakob B\xE6k Tejs Houen,\
  \ Mikkel Thorup"
conference: 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2017
bibkey: dahlgaard2017fast
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.04370'}]
tags: ["Scalability", "Similarity Search"]
short_authors: Dahlgaard et al.
---
We consider the \(\textit\{Similarity Sketching\}\) problem: Given a universe
\([u] = \\{0,\ldots, u-1\\}\) we want a random function \(S\) mapping subsets
\(A\subseteq [u]\) into vectors \(S(A)\) of size \(t\), such that the Jaccard
similarity \(J(A,B) = |A\cap B|/|A\cup B|\) between sets \(A\) and \(B\) is
preserved. More precisely, define \(X_i = [S(A)[i] =
  S(B)[i]]\) and \(X = \sum_\{i\in [t]\} X_i\). We want \(E[X_i]=J(A,B)\), and we want
\(X\) to be strongly concentrated around \(E[X] = t \cdot J(A,B)\) (i.e.
Chernoff-style bounds). This is a fundamental problem which has found numerous
applications in data mining, large-scale classification, computer vision,
similarity search, etc. via the classic MinHash algorithm. The vectors \(S(A)\)
are also called \(\textit\{sketches\}\). Strong concentration is critical, for
often we want to sketch many sets \(B_1,\ldots,B_n\) so that we later, for a
query set \(A\), can find (one of) the most similar \(B_i\). It is then critical
that no \(B_i\) looks much more similar to \(A\) due to errors in the sketch.
  The seminal \(t\times\textit\{MinHash\}\) algorithm uses \(t\) random hash
functions \(h_1,\ldots, h_t\), and stores \(\left ( \min_\{a\in A\} h_1(A),\ldots,
\min_\{a\in A\} h_t(A) \right )\) as the sketch of \(A\). The main drawback of
MinHash is, however, its \(O(t\cdot |A|)\) running time, and finding a sketch
with similar properties and faster running time has been the subject of several
papers. (continued...)