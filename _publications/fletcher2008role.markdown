---
layout: publication
title: A Role-free Approach To Indexing Large RDF Data Sets In Secondary Memory For
  Efficient SPARQL Evaluation
authors: George H. L. Fletcher, Peter W. Beck
conference: Arxiv
year: 2008
bibkey: fletcher2008role
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0811.1083'}]
tags: []
short_authors: George H. L. Fletcher, Peter W. Beck
---
Massive RDF data sets are becoming commonplace. RDF data is typically
generated in social semantic domains (such as personal information management)
wherein a fixed schema is often not available a priori. We propose a simple
Three-way Triple Tree (TripleT) secondary-memory indexing technique to
facilitate efficient SPARQL query evaluation on such data sets. The novelty of
TripleT is that (1) the index is built over the atoms occurring in the data
set, rather than at a coarser granularity, such as whole triples occurring in
the data set; and (2) the atoms are indexed regardless of the roles (i.e.,
subjects, predicates, or objects) they play in the triples of the data set. We
show through extensive empirical evaluation that TripleT exhibits multiple
orders of magnitude improvement over the state of the art on RDF indexing, in
terms of both storage and query processing costs.