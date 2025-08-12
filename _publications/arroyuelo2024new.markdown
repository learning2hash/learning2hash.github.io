---
layout: publication
title: New Compressed Indices For Multijoins On Graph Databases
authors: "Diego Arroyuelo, Fabrizio Barisione, Antonio Fari\xF1a, Adri\xE1n G\xF3\
  mez-Brand\xF3n, Gonzalo Navarro"
conference: Arxiv
year: 2024
bibkey: arroyuelo2024new
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.00558'}]
tags: ["Efficiency"]
short_authors: Arroyuelo et al.
---
A recent surprising result in the implementation of worst-case-optimal (wco)
multijoins in graph databases (specifically, basic graph patterns) is that they
can be supported on graph representations that take even less space than a
plain representation, and orders of magnitude less space than classical
indices, while offering comparable performance. In this paper we uncover a wide
set of new wco space-time tradeoffs: we (1) introduce new compact indices that
handle multijoins in wco time, and (2) combine them with new query resolution
strategies that offer better times in practice. As a result, we improve the
average query times of current compact representations by a factor of up to 13
to produce the first 1000 results, and using twice their space, reduce their
total average query time by a factor of 2. Our experiments suggest that there
is more room for improvement in terms of generating better query plans for
multijoins.