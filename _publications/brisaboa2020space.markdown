---
layout: publication
title: Space/time-efficient RDF Stores Based On Circular Suffix Sorting
authors: "Nieves R. Brisaboa, Ana Cerdeira-pena, Guillermo de Bernardo, Antonio Fari\xF1\
  a, Gonzalo Navarro"
conference: The Journal of Supercomputing
year: 2022
bibkey: brisaboa2020space
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.10045'}]
tags: ["Efficiency"]
short_authors: Brisaboa et al.
---
In recent years, RDF has gained popularity as a format for the standardized
publication and exchange of information in the Web of Data. In this paper we
introduce RDFCSA, a data structure that is able to self-index an RDF dataset in
small space and supports efficient querying. RDFCSA regards the triples of the
RDF store as short circular strings and applies suffix sorting on those
strings, so that triple-pattern queries reduce to prefix searching on the
string set. The RDF store is then represented compactly using a Compressed
Suffix Array (CSA), a proved technology in text indexing that efficiently
supports prefix searches.
  Our experiments show that RDFCSA provides a compact RDF representation, using
less than 60% of the space required by the raw data, and yields fast and
consistent query times when answering triple-pattern queries (a few
microseconds per result). We also support join queries, a key component of most
SPARQL queries. RDFCSA is shown to provide an excellent space/time tradeoff,
typically using much less space than alternatives that compete in time.