---
layout: publication
title: Efficient SPARQL Autocompletion Via SPARQL
authors: Hannah Bast, Johannes Kalmbach, Theresa Klumpp, Florian Kramer, Niklas Schnelle
conference: Arxiv
year: 2021
bibkey: bast2021efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.14595'}]
tags: ["Evaluation"]
short_authors: Bast et al.
---
We show how to achieve fast autocompletion for SPARQL queries on very large
knowledge bases. At any position in the body of a SPARQL query, the
autocompletion suggests matching subjects, predicates, or objects. The
suggestions are context-sensitive in the sense that they lead to a non-empty
result and are ranked by their relevance to the part of the query already
typed. The suggestions can be narrowed down by prefix search on the names and
aliases of the desired subject, predicate, or object. All suggestions are
themselves obtained via SPARQL queries, which we call autocompletion queries.
For existing SPARQL engines, these queries are impractically slow on large
knowledge bases. We present various algorithmic and engineering improvements of
an existing SPARQL engine such that these autocompletion queries are executed
efficiently. We provide an extensive evaluation of a variety of suggestion
methods on three large knowledge bases, including Wikidata (6.9B triples). We
explore the trade-off between the relevance of the suggestions and the
processing time of the autocompletion queries. We compare our results with two
widely used SPARQL engines, Virtuoso and Blazegraph. On Wikidata, we achieve
fully sensitive suggestions with sub-second response times for over 90% of a
large and diverse set of thousands of autocompletion queries. Materials for
full reproducibility, an interactive evaluation web app, and a demo are
available on: https://ad.informatik.uni-freiburg.de/publications .