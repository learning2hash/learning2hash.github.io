---
layout: publication
title: Diamond Sampling For Approximate Maximum All-pairs Dot-product (MAD) Search
authors: Ballard Grey, Pinar Ali, Kolda Tamara G., Seshadhri C.
conference: "ICDM"
year: 2015
bibkey: ballard2015diamond
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1506.03872"}
tags: []
---
Given two sets of vectors, \\(A = \&#123;&#123;a_1&#125;, \dots, &#123;a_m&#125;\&#125;\\) and \\(B=\&#123;&#123;b_1&#125;,\dots,&#123;b_n&#125;\&#125;\\), our problem is to find the top-\\(t\\) dot products, i.e., the largest \\(|&#123;a_i&#125;\cdot&#123;b_j&#125;|\\) among all possible pairs. This is a fundamental mathematical problem that appears in numerous data applications involving similarity search, link prediction, and collaborative filtering. We propose a sampling-based approach that avoids direct computation of all \\(mn\\) dot products. We select diamonds (i.e., four-cycles) from the weighted tripartite representation of \\(A\\) and \\(B\\). The probability of selecting a diamond corresponding to pair \\((i,j)\\) is proportional to \\((&#123;a_i&#125;\cdot&#123;b_j&#125;)^2\\), amplifying the focus on the largest-magnitude entries. Experimental results indicate that diamond sampling is orders of magnitude faster than direct computation and requires far fewer samples than any competing approach. We also apply diamond sampling to the special case of maximum inner product search, and get significantly better results than the state-of-the-art hashing methods.
