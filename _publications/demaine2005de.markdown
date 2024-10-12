---
layout: publication
title: De Dictionariis Dynamicis Pauco Spatio Utentibus
authors: Demaine Erik D., Der Heide Friedhelm Meyer Auf, Pagh Rasmus, Patrascu Mihai
conference: "Arxiv"
year: 2005
bibkey: demaine2005de
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0512081"}
tags: ['ARXIV']
---
We develop dynamic dictionaries on the word RAM that use asymptotically optimal space, up to constant factors, subject to insertions and deletions, and subject to supporting perfect-hashing queries and/or membership queries, each operation in constant time with high probability. When supporting only membership queries, we attain the optimal space bound of Theta(n lg(u/n)) bits, where n and u are the sizes of the dictionary and the universe, respectively. Previous dictionaries either did not achieve this space bound or had time bounds that were only expected and amortized. When supporting perfect-hashing queries, the optimal space bound depends on the range &amp;\#123;1,2,...,n+t&amp;\#125; of hashcodes allowed as output. We prove that the optimal space bound is Theta(n lglg(u/n) + n lg(n/(t+1))) bits when supporting only perfect-hashing queries, and it is Theta(n lg(u/n) + n lg(n/(t+1))) bits when also supporting membership queries. All upper bounds are new, as is the Omega(n lg(n/(t+1))) lower bound.
