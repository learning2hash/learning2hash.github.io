---
layout: publication
title: Ranked Document Retrieval In (almost) No Space
authors: Nieves R. Brisaboa, Ana Cerdeira-Pena, Gonzalo Navarro, Oscar Pedreira
conference: Lecture Notes in Computer Science
year: 2012
bibkey: brisaboa2012ranked
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1207.5425'}]
tags: ["Text Retrieval"]
short_authors: Brisaboa et al.
---
Ranked document retrieval is a fundamental task in search engines. Such
queries are solved with inverted indexes that require additional 45%-80% of the
compressed text space, and take tens to hundreds of microseconds per query. In
this paper we show how ranked document retrieval queries can be solved within
tens of milliseconds using essentially no extra space over an in-memory
compressed representation of the document collection. More precisely, we
enhance wavelet trees on bytecodes (WTBCs), a data structure that rearranges
the bytes of the compressed collection, so that they support ranked conjunctive
and disjunctive queries, using just 6%-18% of the compressed text space.