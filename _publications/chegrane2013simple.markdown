---
layout: publication
title: Simple Compact And Robust Approximate String Dictionary
authors: Chegrane Ibrahim, Belazzougui Djamal
conference: "Arxiv"
year: 2013
bibkey: chegrane2013simple
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1312.4678"}
tags: ['ARXIV']
---
<p>This paper is concerned with practical implementations of approximate
string dictionaries that allow edit errors. In this problem, we have as
input a dictionary <span class="math inline">\(D\)</span> of <span
class="math inline">\(d\)</span> strings of total length <span
class="math inline">\(n\)</span> over an alphabet of size <span
class="math inline">\(\sigma\)</span>. Given a bound <span
class="math inline">\(k\)</span> and a pattern <span
class="math inline">\(x\)</span> of length <span
class="math inline">\(m\)</span>, a query has to return all the strings
of the dictionary which are at edit distance at most <span
class="math inline">\(k\)</span> from <span
class="math inline">\(x\)</span>, where the edit distance between two
strings <span class="math inline">\(x\)</span> and <span
class="math inline">\(y\)</span> is defined as the minimum-cost sequence
of edit operations that transform <span class="math inline">\(x\)</span>
into <span class="math inline">\(y\)</span>. The cost of a sequence of
operations is defined as the sum of the costs of the operations involved
in the sequence. In this paper, we assume that each of these operations
has unit cost and consider only three operations: deletion of one
character, insertion of one character and substitution of a character by
another. We present a practical implementation of the data structure we
recently proposed and which works only for one error. We extend the
scheme to <span class="math inline">\(2\leq k&lt;m\)</span>. Our
implementation has many desirable properties: it has a very fast and
space-efficient building algorithm. The dictionary data structure is
compact and has fast and robust query time. Finally our data structure
is simple to implement as it only uses basic techniques from the
literature, mainly hashing (linear probing and hash signatures) and
succinct data structures (bitvectors supporting rank queries).</p>
