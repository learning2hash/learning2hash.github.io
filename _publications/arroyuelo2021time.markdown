---
layout: publication
title: Time- And Space-efficient Regular Path Queries On Graphs
authors: Diego Arroyuelo, Aidan Hogan, Gonzalo Navarro, Javiel Rojas-Ledesma
conference: Arxiv
year: 2021
bibkey: arroyuelo2021time
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04556'}]
tags: ["Efficiency"]
short_authors: Arroyuelo et al.
---
We introduce a time- and space-efficient technique to solve regularpath
queries over labeled graphs. We combine a bit-parallel simula-tion of the
Glushkov automaton of the regular expression with thering index introduced by
Arroyuelo et al., exploiting its wavelettree representation of the triples in
order to efficiently reach thestates of the product graph that are relevant for
the query. Ourquery algorithm is able to simultaneously process several
automa-ton states, as well as several graph nodes/labels. Our
experimentalresults show that our representation uses 3-5 times less space
thanthe alternatives in the literature, while generally outperformingthem in
query times (1.67 times faster than the next best).