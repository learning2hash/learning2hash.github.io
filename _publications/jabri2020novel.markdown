---
layout: publication
title: A Novel Approach For Generating SPARQL Queries From RDF Graphs
authors: Emna Jabri
conference: Arxiv
year: 2020
bibkey: jabri2020novel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.02862'}]
tags: []
short_authors: Emna Jabri
---
This work is done as part of a research master's thesis project. The goal is
to generate SPARQL queries based on user-supplied keywords to query RDF graphs.
To do this, we first transformed the input ontology into an RDF graph that
reflects the semantics represented in the ontology. Subsequently, we stored
this RDF graph in the Neo4j graphical database to ensure efficient and
persistent management of RDF data. At the time of the interrogation, we studied
the different possible and desired interpretations of the request originally
made by the user. We have also proposed to carry out a sort of transformation
between the two query languages SPARQL and Cypher, which is specific to Neo4j.
This allows us to implement the architecture of our system over a wide variety
of BD-RDFs providing their query languages, without changing any of the other
components of the system. Finally, we tested and evaluated our tool using
different test bases, and it turned out that our tool is comprehensive,
effective, and powerful enough.