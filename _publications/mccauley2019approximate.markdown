---
layout: publication
title: Approximate Similarity Search Under Edit Distance Using Locality-sensitive Hashing
authors: Mccauley Samuel
conference: "Arxiv"
year: 2019
bibkey: mccauley2019approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1907.01600"}
tags: ['ARXIV', 'Independent']
---
<p>Edit distance similarity search, also called approximate pattern
matching, is a fundamental problem with widespread database
applications. The goal of the problem is to preprocess <span
class="math inline">\(n\)</span> strings of length <span
class="math inline">\(d\)</span>, to quickly answer queries <span
class="math inline">\(q\)</span> of the form: if there is a database
string within edit distance <span class="math inline">\(r\)</span> of
<span class="math inline">\(q\)</span>, return a database string within
edit distance <span class="math inline">\(cr\)</span> of <span
class="math inline">\(q\)</span>. Previous approaches to this problem
either rely on very large (superconstant) approximation ratios <span
class="math inline">\(c\)</span>, or very small search radii <span
class="math inline">\(r\)</span>. Outside of a narrow parameter range,
these solutions are not competitive with trivially searching through all
<span class="math inline">\(n\)</span> strings. In this work give a
simple and easy-to-implement hash function that can quickly answer
queries for a wide range of parameters. Specifically, our strategy can
answer queries in time <span
class="math inline">\(\tilde{O}(d3^rn^{1/c})\)</span>. The best known
practical results require <span class="math inline">\(c \gg r\)</span>
to achieve any correctness guarantee; meanwhile, the best known
theoretical results are very involved and difficult to implement, and
require query time at least <span class="math inline">\(24^r\)</span>.
Our results significantly broaden the range of parameters for which we
can achieve nontrivial bounds, while retaining the practicality of a
locality-sensitive hash function. We also show how to apply our ideas to
the closely-related Approximate Nearest Neighbor problem for edit
distance, obtaining similar time bounds.</p>
