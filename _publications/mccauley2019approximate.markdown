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
Edit distance similarity search, also called approximate pattern matching, is
a fundamental problem with widespread database applications. The goal of the
problem is to preprocess \\(n\\) strings of length \\(d\\), to quickly answer queries
\\(q\\) of the form: if there is a database string within edit distance \\(r\\) of \\(q\\),
return a database string within edit distance \\(cr\\) of \\(q\\). Previous approaches
to this problem either rely on very large (superconstant) approximation ratios
\\(c\\), or very small search radii \\(r\\). Outside of a narrow parameter range, these
solutions are not competitive with trivially searching through all \\(n\\) strings.
  In this work give a simple and easy-to-implement hash function that can
quickly answer queries for a wide range of parameters. Specifically, our
strategy can answer queries in time \\(\tilde\{O\}(d3^rn^\{1/c\})\\). The best known
practical results require \\(c \gg r\\) to achieve any correctness guarantee;
meanwhile, the best known theoretical results are very involved and difficult
to implement, and require query time at least \\(24^r\\). Our results significantly
broaden the range of parameters for which we can achieve nontrivial bounds,
while retaining the practicality of a locality-sensitive hash function.
  We also show how to apply our ideas to the closely-related Approximate
Nearest Neighbor problem for edit distance, obtaining similar time bounds.
