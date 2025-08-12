---
layout: publication
title: 'An Index For Regular Expression Queries: Design And Implementation'
authors: Dominic Tsang, Sanjay Chawla
conference: Arxiv
year: 2011
bibkey: tsang2011index
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1108.1228'}]
tags: ["Efficiency"]
short_authors: Dominic Tsang, Sanjay Chawla
---
The like regular expression predicate has been part of the SQL standard since
at least 1989. However, despite its popularity and wide usage, database vendors
provide only limited indexing support for regular expression queries which
almost always require a full table scan.
  In this paper we propose a rigorous and robust approach for providing
indexing support for regular expression queries. Our approach consists of
formulating the indexing problem as a combinatorial optimization problem. We
begin with a database, abstracted as a collection of strings. From this data
set we generate a query workload. The input to the optimization problem is the
database and the workload. The output is a set of multigrams (substrings) which
can be used as keys to records which satisfy the query workload. The multigrams
can then be integrated with the data structure (like B+ trees) to provide
indexing support for the queries. We provide a deterministic and a randomized
approximation algorithm (with provable guarantees) to solve the optimization
problem. Extensive experiments on synthetic data sets demonstrate that our
approach is accurate and efficient.
  We also present a case study on PROSITE patterns - which are complex regular
expression signatures for classes of proteins. Again, we are able to
demonstrate the utility of our indexing approach in terms of accuracy and
efficiency. Thus, perhaps for the first time, there is a robust and practical
indexing mechanism for an important class of database queries.