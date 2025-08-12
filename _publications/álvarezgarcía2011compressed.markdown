---
layout: publication
title: Compressed K2-triples For Full-in-memory RDF Engines
authors: "Sandra \xC1lvarez-Garc\xEDa, Nieves R. Brisaboa, Javier D. Fern\xE1ndez,\
  \ Miguel A. Mart\xEDnez-Prieto"
conference: Arxiv
year: 2011
bibkey: "\xE1lvarezgarc\xEDa2011compressed"
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1105.4004'}]
tags: ["Compact Codes"]
short_authors: "\xC1lvarez-Garc\xEDa et al."
---
Current "data deluge" has flooded the Web of Data with very large RDF
datasets. They are hosted and queried through SPARQL endpoints which act as
nodes of a semantic net built on the principles of the Linked Data project.
Although this is a realistic philosophy for global data publishing, its query
performance is diminished when the RDF engines (behind the endpoints) manage
these huge datasets. Their indexes cannot be fully loaded in main memory, hence
these systems need to perform slow disk accesses to solve SPARQL queries. This
paper addresses this problem by a compact indexed RDF structure (called
k2-triples) applying compact k2-tree structures to the well-known
vertical-partitioning technique. It obtains an ultra-compressed representation
of large RDF graphs and allows SPARQL queries to be full-in-memory performed
without decompression. We show that k2-triples clearly outperforms
state-of-the-art compressibility and traditional vertical-partitioning query
resolution, remaining very competitive with multi-index solutions.