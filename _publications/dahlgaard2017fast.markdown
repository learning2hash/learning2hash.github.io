---
layout: publication
title: Fast Similarity Sketching
authors: Dahlgaard Søren, Langhede Mathias Bæk Tejs, Houen Jakob Bæk Tejs, Thorup Mikkel
conference: "Arxiv"
year: 2017
bibkey: dahlgaard2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.04370"}
tags: ['ARXIV', 'Supervised']
---
We consider the \(\textbackslash\textit\{Similarity Sketching\}\) problem: Given a universe \([u] = \\{0,\ldots, u-1\\}\) we want a random function \(S\) mapping subsets \(A\subseteq [u]\) into vectors \(S(A)\) of size \(t\), such that the Jaccard similarity \(J(A,B) = \|A\cap B\|/\|A\cup B\|\) between sets \(A\) and \(B\) is preserved. More precisely, define \(X\_i = [S(A)[i] = S(B)[i]]\) and \(X = \textbackslash\sum\_\{i\in [t]\} X\_i\). We want \(E[X\_i]=J(A,B)\), and we want \(X\) to be strongly concentrated around \(E[X] = t \cdot J(A,B)\) (i.e. Chernoff-style bounds). This is a fundamental problem which has found numerous applications in data mining, large-scale classification, computer vision, similarity search, etc. via the classic MinHash algorithm. The vectors \(S(A)\) are also called \(\textbackslash\textit\{sketches\}\). Strong concentration is critical, for often we want to sketch many sets \(B\_1,\ldots,B\_n\) so that we later, for a query set \(A\), can find (one of) the most similar \(B\_i\). It is then critical that no \(B\_i\) looks much more similar to \(A\) due to errors in the sketch. The seminal \(t\times\textbackslash\textit\{MinHash\}\) algorithm uses \(t\) random hash functions \(h\_1,\ldots, h\_t\), and stores \(\left ( \min\_\{a\in A\} h\_1(A),\ldots, \min\_\{a\in A\} h\_t(A) \right )\) as the sketch of \(A\). The main drawback of MinHash is, however, its \(O(t\cdot \|A\|)\) running time, and finding a sketch with similar properties and faster running time has been the subject of several papers. (continued...)
