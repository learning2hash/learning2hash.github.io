---
layout: publication
title: Similarity Search And Locality Sensitive Hashing Using Tcams
authors: Shinde Rajendra, Goel Ashish, Gupta Pankaj, Dutta Debojyoti
conference: "Arxiv"
year: 2010
bibkey: shinde2010similarity
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1006.3514"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>Similarity search methods are widely used as kernels in various
machine learning applications. Nearest neighbor search (NNS) algorithms
are often used to retrieve similar entries, given a query. While there
exist efficient techniques for exact query lookup using hashing,
similarity search using exact nearest neighbors is known to be a hard
problem and in high dimensions, best known solutions offer little
improvement over a linear scan. Fast solutions to the approximate NNS
problem include Locality Sensitive Hashing (LSH) based techniques, which
need storage polynomial in <span class="math inline">\(n\)</span> with
exponent greater than <span class="math inline">\(1\)</span>, and query
time sublinear, but still polynomial in <span
class="math inline">\(n\)</span>, where <span
class="math inline">\(n\)</span> is the size of the database. In this
work we present a new technique of solving the approximate NNS problem
in Euclidean space using a Ternary Content Addressable Memory (TCAM),
which needs near linear space and has O(1) query time. In fact, this
method also works around the best known lower bounds in the cell probe
model for the query time using a data structure near linear in the size
of the data base. TCAMs are high performance associative memories widely
used in networking applications such as access control lists. A TCAM can
query for a bit vector within a database of ternary vectors, where every
bit position represents <span class="math inline">\(0\)</span>, <span
class="math inline">\(1\)</span> or <span
class="math inline">\(*\)</span>. The <span
class="math inline">\(*\)</span> is a wild card representing either a
<span class="math inline">\(0\)</span> or a <span
class="math inline">\(1\)</span>. We leverage TCAMs to design a variant
of LSH, called Ternary Locality Sensitive Hashing (TLSH) wherein we hash
database entries represented by vectors in the Euclidean space into
<span class="math inline">\(\{0,1,*\}\)</span>. By using the added
functionality of a TLSH scheme with respect to the <span
class="math inline">\(*\)</span> character, we solve an instance of the
approximate nearest neighbor problem with 1 TCAM access and storage
nearly linear in the size of the database. We believe that this work can
open new avenues in very high speed data mining.</p>
