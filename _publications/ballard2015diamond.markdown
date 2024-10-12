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
Given two sets of vectors, \{&#37; raw &#37;\}\\(A = \\{\{a\_1\}, \dots, \{a\_m\}\\}\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(B=\\{\{b\_1\},\dots,\{b\_n\}\\}\\)\{&#37; endraw &#37;\}, our problem is to find the top-\{&#37; raw &#37;\}\\(t\\)\{&#37; endraw &#37;\} dot products, i.e., the largest \{&#37; raw &#37;\}\\(|\{a\_i\}\cdot\{b\_j\}|\\)\{&#37; endraw &#37;\} among all possible pairs. This is a fundamental mathematical problem that appears in numerous data applications involving similarity search, link prediction, and collaborative filtering. We propose a sampling-based approach that avoids direct computation of all \{&#37; raw &#37;\}\\(mn\\)\{&#37; endraw &#37;\} dot products. We select diamonds (i.e., four-cycles) from the weighted tripartite representation of \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(B\\)\{&#37; endraw &#37;\}. The probability of selecting a diamond corresponding to pair \{&#37; raw &#37;\}\\((i,j)\\)\{&#37; endraw &#37;\} is proportional to \{&#37; raw &#37;\}\\((\{a\_i\}\cdot\{b\_j\})^2\\)\{&#37; endraw &#37;\}, amplifying the focus on the largest-magnitude entries. Experimental results indicate that diamond sampling is orders of magnitude faster than direct computation and requires far fewer samples than any competing approach. We also apply diamond sampling to the special case of maximum inner product search, and get significantly better results than the state-of-the-art hashing methods.
