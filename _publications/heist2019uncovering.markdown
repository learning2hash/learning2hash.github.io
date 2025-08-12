---
layout: publication
title: Uncovering The Semantics Of Wikipedia Categories
authors: Nicolas Heist, Heiko Paulheim
conference: Lecture Notes in Computer Science
year: 2019
bibkey: heist2019uncovering
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.12089'}]
tags: []
short_authors: Nicolas Heist, Heiko Paulheim
---
The Wikipedia category graph serves as the taxonomic backbone for large-scale
knowledge graphs like YAGO or Probase, and has been used extensively for tasks
like entity disambiguation or semantic similarity estimation. Wikipedia's
categories are a rich source of taxonomic as well as non-taxonomic information.
The category 'German science fiction writers', for example, encodes the type of
its resources (Writer), as well as their nationality (German) and genre
(Science Fiction). Several approaches in the literature make use of fractions
of this encoded information without exploiting its full potential. In this
paper, we introduce an approach for the discovery of category axioms that uses
information from the category network, category instances, and their
lexicalisations. With DBpedia as background knowledge, we discover 703k axioms
covering 502k of Wikipedia's categories and populate the DBpedia knowledge
graph with additional 4.4M relation assertions and 3.3M type assertions at more
than 87% and 90% precision, respectively.