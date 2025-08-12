---
layout: publication
title: 'Swift Linked Data Miner: Mining OWL 2 EL Class Expressions Directly From Online
  RDF Datasets'
authors: "Jedrzej Potoniec, Piotr Jakubowski, Agnieszka \u0141awrynowicz"
conference: Journal of Web Semantics
year: 2017
bibkey: potoniec2017swift
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.07114'}]
tags: ["Datasets"]
short_authors: "Jedrzej Potoniec, Piotr Jakubowski, Agnieszka \u0141awrynowicz"
---
In this study, we present Swift Linked Data Miner, an interruptible algorithm
that can directly mine an online Linked Data source (e.g., a SPARQL endpoint)
for OWL 2 EL class expressions to extend an ontology with new SubClassOf:
axioms. The algorithm works by downloading only a small part of the Linked Data
source at a time, building a smart index in the memory and swiftly iterating
over the index to mine axioms. We propose a transformation function from mined
axioms to RDF Data Shapes. We show, by means of a crowdsourcing experiment,
that most of the axioms mined by Swift Linked Data Miner are correct and can be
added to an ontology. We provide a ready to use Prot\'eg\'e plugin implementing
the algorithm, to support ontology engineers in their daily modeling work.