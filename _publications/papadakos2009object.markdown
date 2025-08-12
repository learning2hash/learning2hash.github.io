---
layout: publication
title: Object-relational Database Representations For Text Indexing
authors: Panagiotis Papadakos, Yannis Theoharis, Yannis Marketakis, Nikos Armenatzoglou,
  Yannis Tzitzikas
conference: Arxiv
year: 2009
bibkey: papadakos2009object
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0906.3112'}]
tags: ["Evaluation"]
short_authors: Papadakos et al.
---
One of the distinctive features of Information Retrieval systems comparing to
Database Management systems, is that they offer better compression for posting
lists, resulting in better I/O performance and thus faster query evaluation. In
this paper, we introduce database representations of the index that reduce the
size (and thus the disk I/Os) of the posting lists. This is not achieved by
redesigning the DBMS, but by exploiting the non 1NF features that existing
Object-Relational DBM systems (ORDBMS) already offer. Specifically, four
different database representations are described and detailed experimental
results for one million pages are reported. Three of these representations are
one order of magnitude more space efficient and faster (in query evaluation)
than the plain relational representation.