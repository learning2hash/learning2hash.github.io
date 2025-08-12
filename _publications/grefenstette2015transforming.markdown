---
layout: publication
title: Transforming Wikipedia Into An Ontology-based Information Retrieval Search
  Engine For Local Experts Using A Third-party Taxonomy
authors: Gregory Grefenstette, Karima Rafes
conference: Arxiv
year: 2015
bibkey: grefenstette2015transforming
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.01259'}]
tags: ["Text Retrieval"]
short_authors: Gregory Grefenstette, Karima Rafes
---
Wikipedia is widely used for finding general information about a wide variety
of topics. Its vocation is not to provide local information. For example, it
provides plot, cast, and production information about a given movie, but not
showing times in your local movie theatre. Here we describe how we can connect
local information to Wikipedia, without altering its content. The case study we
present involves finding local scientific experts. Using a third-party
taxonomy, independent from Wikipedia's category hierarchy, we index information
connected to our local experts, present in their activity reports, and we
re-index Wikipedia content using the same taxonomy. The connections between
Wikipedia pages and local expert reports are stored in a relational database,
accessible through as public SPARQL endpoint. A Wikipedia gadget (or plugin)
activated by the interested user, accesses the endpoint as each Wikipedia page
is accessed. An additional tab on the Wikipedia page allows the user to open up
a list of teams of local experts associated with the subject matter in the
Wikipedia page. The technique, though presented here as a way to identify local
experts, is generic, in that any third party taxonomy, can be used in this to
connect Wikipedia to any non-Wikipedia data source.