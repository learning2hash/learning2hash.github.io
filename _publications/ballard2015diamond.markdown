---
layout: publication
title: "Diamond Sampling for Approximate Maximum All-pairs Dot-product (MAD) Search"
authors: Ballard Grey, Pinar Ali, Kolda Tamara G., Seshadhri C.
conference: ICDM
year: 2015
bibkey: ballard2015diamond
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1506.03872"}
tags: []
---
Given two sets of vectors, \$A = \\{\{a_1\}, \dots, \{a_m\}\\}\$ and
\$B=\\{\{b_1\},\dots,\{b_n\}\\}\$, our problem is to find the top-\$t\$ dot
products, i.e., the largest \$|\{a_i\}\cdot\{b_j\}|\$ among all possible pairs.
This is a fundamental mathematical problem that appears in numerous data
applications involving similarity search, link prediction, and collaborative
filtering. We propose a sampling-based approach that avoids direct computation
of all \$mn\$ dot products. We select diamonds (i.e., four-cycles) from the
weighted tripartite representation of \$A\$ and \$B\$. The probability of
selecting a diamond corresponding to pair \$(i,j)\$ is proportional to
\$(\{a_i\}\cdot\{b_j\})^2\$, amplifying the focus on the largest-magnitude
entries. Experimental results indicate that diamond sampling is orders of
magnitude faster than direct computation and requires far fewer samples than any
competing approach. We also apply diamond sampling to the special case of
maximum inner product search, and get significantly better results than the
state-of-the-art hashing methods.
