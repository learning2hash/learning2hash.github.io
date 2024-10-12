---
layout: publication
title: SAH Shifting-aware Asymmetric Hashing For Reverse k-maximum Inner Product Search
authors: Huang Qiang, Wang Yanhao, Tung Anthony K. H.
conference: "Arxiv"
year: 2022
bibkey: huang2022sah
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2211.12751"}
  - {name: "Code", url: "https://github.com/HuangQiang/SAH}"}
tags: ['ARXIV', 'Has Code', 'Independent']
---
This paper investigates a new yet challenging problem called Reverse \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-Maximum Inner Product Search (R\{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}MIPS). Given a query (item) vector, a set of item vectors, and a set of user vectors, the problem of R\{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}MIPS aims to find a set of user vectors whose inner products with the query vector are one of the \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} largest among the query and item vectors. We propose the first subquadratic-time algorithm, i.e., Shifting-aware Asymmetric Hashing (SAH), to tackle the R\{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}MIPS problem. To speed up the Maximum Inner Product Search (MIPS) on item vectors, we design a shifting-invariant asymmetric transformation and develop a novel sublinear-time Shifting-Aware Asymmetric Locality Sensitive Hashing (SA-ALSH) scheme. Furthermore, we devise a new blocking strategy based on the Cone-Tree to effectively prune user vectors (in a batch). We prove that SAH achieves a theoretical guarantee for solving the RMIPS problem. Experimental results on five real-world datasets show that SAH runs 4\{&#37; raw &#37;\}\\(\sim\\)\{&#37; endraw &#37;\}8\{&#37; raw &#37;\}\\(\times\\)\{&#37; endraw &#37;\} faster than the state-of-the-art methods for R\{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}MIPS while achieving F1-scores of over 90\&#37;. The code is available at \url\{https://github.com/HuangQiang/SAH\}.
