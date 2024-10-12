---
layout: publication
title: Non-empty Bins With Simple Tabulation Hashing
authors: Aamand Anders, Thorup Mikkel
conference: "Arxiv"
year: 2018
bibkey: aamand2018non
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1810.13187"}
tags: ['ARXIV', 'Independent']
---
We consider the hashing of a set \{&#37; raw &#37;\}\\(X\subseteq U\\)\{&#37; endraw &#37;\} with \{&#37; raw &#37;\}\\(|X|=m\\)\{&#37; endraw &#37;\} using a simple tabulation hash function \{&#37; raw &#37;\}\\(h:U\to [n]=\\{0,\dots,n-1\\}\\)\{&#37; endraw &#37;\} and analyse the number of non-empty bins, that is, the size of \{&#37; raw &#37;\}\\(h(X)\\)\{&#37; endraw &#37;\}. We show that the expected size of \{&#37; raw &#37;\}\\(h(X)\\)\{&#37; endraw &#37;\} matches that with fully random hashing to within low-order terms. We also provide concentration bounds. The number of non-empty bins is a fundamental measure in the balls and bins paradigm, and it is critical in applications such as Bloom filters and Filter hashing. For example, normally Bloom filters are proportioned for a desired low false-positive probability assuming fully random hashing (see \url\{en.wikipedia.org/wiki/Bloom\_filter\}). Our results imply that if we implement the hashing with simple tabulation, we obtain the same low false-positive probability for any possible input.
