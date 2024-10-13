---
layout: publication
title: Approximate String Matching Theory And Applications (la Recherche Approchee De Motifs Theorie Et Applications)
authors: Chegrane Ibrahim
conference: "Arxiv"
year: 2017
bibkey: chegrane2017approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1701.08688"}
tags: ['ARXIV']
---
The approximate string matching is a fundamental and recurrent problem that
arises in most computer science fields. This problem can be defined as follows:
  Let \{D=\{x_1,x_2,\ldots x_d\}\} be a set of \{d\} words defined on an alphabet
\{\Sigma\}, let \{q\} be a query defined also on \{\Sigma\}, and let \{k\} be a
positive integer. We want to build a data structure on \{D\} capable of answering
the following query: find all words in \{D\} that are at most different from the
query word \{q\} with \{k\} errors.
  In this thesis, we study the approximate string matching methods in
dictionaries, texts, and indexes, to propose practical methods that solve this
problem efficiently. We explore this problem in three complementary directions:
  1) The approximate string matching in the dictionary. We propose two
solutions to this problem, the first one uses hash tables for \{k \geq 2\}, the
second uses the Trie and reverse Trie, and it is restricted to (k = 1). The two
solutions are adaptable, without loss of performance, to the approximate string
matching in a text.
  2) The approximate string matching for \textit{autocompletion}, which is,
find all suffixes of a given prefix that may contain errors. We give a new
solution better in practice than all the previous proposed solutions.
  3) The problem of the alignment of biological sequences can be interpreted as
an approximate string matching problem. We propose a solution for peers and
multiple sequences alignment.
  \medskip All the results obtained showed that our algorithms, give the best
performance on sets of practical data (benchmark from the real world). All our
methods are proposed as libraries, and they are published online.
