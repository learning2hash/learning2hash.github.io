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
<p>The approximate string matching is a fundamental and recurrent
problem that arises in most computer science fields. This problem can be
defined as follows: Let <span class="math inline">\(D=\{x_1,x_2,\ldots
x_d\}\)</span> be a set of <span class="math inline">\(d\)</span> words
defined on an alphabet <span class="math inline">\(\Sigma\)</span>, let
<span class="math inline">\(q\)</span> be a query defined also on <span
class="math inline">\(\Sigma\)</span>, and let <span
class="math inline">\(k\)</span> be a positive integer. We want to build
a data structure on <span class="math inline">\(D\)</span> capable of
answering the following query: find all words in <span
class="math inline">\(D\)</span> that are at most different from the
query word <span class="math inline">\(q\)</span> with <span
class="math inline">\(k\)</span> errors. In this thesis, we study the
approximate string matching methods in dictionaries, texts, and indexes,
to propose practical methods that solve this problem efficiently. We
explore this problem in three complementary directions: 1) The
approximate string matching in the dictionary. We propose two solutions
to this problem, the first one uses hash tables for <span
class="math inline">\(k \geq 2\)</span>, the second uses the Trie and
reverse Trie, and it is restricted to (k = 1). The two solutions are
adaptable, without loss of performance, to the approximate string
matching in a text. 2) The approximate string matching for , which is,
find all suffixes of a given prefix that may contain errors. We give a
new solution better in practice than all the previous proposed
solutions. 3) The problem of the alignment of biological sequences can
be interpreted as an approximate string matching problem. We propose a
solution for peers and multiple sequences alignment. All the results
obtained showed that our algorithms, give the best performance on sets
of practical data (benchmark from the real world). All our methods are
proposed as libraries, and they are published online.</p>
