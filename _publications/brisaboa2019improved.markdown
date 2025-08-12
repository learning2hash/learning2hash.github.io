---
layout: publication
title: Improved Compressed String Dictionaries
authors: Nieves R. Brisaboa, Ana Cerdeira-Pena, Guillermo de Bernardo, Gonzalo Navarro
conference: Proceedings of the 28th ACM International Conference on Information and
  Knowledge Management
year: 2019
bibkey: brisaboa2019improved
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08372'}]
tags: ["CIKM", "Efficiency"]
short_authors: Brisaboa et al.
---
We introduce a new family of compressed data structures to efficiently store
and query large string dictionaries in main memory. Our main technique is a
combination of hierarchical Front-coding with ideas from longest-common-prefix
computation in suffix arrays. Our data structures yield relevant space-time
tradeoffs in real-world dictionaries. We focus on two domains where string
dictionaries are extensively used and efficient compression is required: URL
collections, a key element in Web graphs and applications such as Web mining;
and collections of URIs and literals, the basic components of RDF datasets. Our
experiments show that our data structures achieve better compression than the
state-of-the-art alternatives while providing very competitive query times.