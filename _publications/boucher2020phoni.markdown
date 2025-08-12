---
layout: publication
title: 'PHONI: Streamed Matching Statistics With Multi-genome References'
authors: "Christina Boucher, Travis Gagie, Tomohiro I, Dominik K\xF6ppl, Ben Langmead,\
  \ Giovanni Manzini, Gonzalo Navarro, Alejandro Pacheco, Massimiliano Rossi"
conference: 2021 Data Compression Conference (DCC)
year: 2021
bibkey: boucher2020phoni
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.05610'}]
tags: ["Efficiency"]
short_authors: Boucher et al.
---
Computing the matching statistics of patterns with respect to a text is a
fundamental task in bioinformatics, but a formidable one when the text is a
highly compressed genomic database. Bannai et al. gave an efficient solution
for this case, which Rossi et al. recently implemented, but it uses two passes
over the patterns and buffers a pointer for each character during the first
pass. In this paper, we simplify their solution and make it streaming, at the
cost of slowing it down slightly. This means that, first, we can compute the
matching statistics of several long patterns (such as whole human chromosomes)
in parallel while still using a reasonable amount of RAM; second, we can
compute matching statistics online with low latency and thus quickly recognize
when a pattern becomes incompressible relative to the database.