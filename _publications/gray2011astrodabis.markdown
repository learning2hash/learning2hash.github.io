---
layout: publication
title: 'Astrodabis: Annotations And Cross-matches For Remote Catalogues'
authors: Norman Gray, Robert G Mann, Dave Morris, Mark Holliman, Keith Noddle
conference: Arxiv
year: 2011
bibkey: gray2011astrodabis
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1111.6116'}]
tags: []
short_authors: Gray et al.
---
Astronomers are good at sharing data, but poorer at sharing knowledge.
  Almost all astronomical data ends up in open archives, and access to these is
being simplified by the development of the global Virtual Observatory (VO).
This is a great advance, but the fundamental problem remains that these
archives contain only basic observational data, whereas all the astrophysical
interpretation of that data -- which source is a quasar, which a low-mass star,
and which an image artefact -- is contained in journal papers, with very little
linkage back from the literature to the original data archives. It is therefore
currently impossible for an astronomer to pose a query like "give me all
sources in this data archive that have been identified as quasars" and this
limits the effective exploitation of these archives, as the user of an archive
has no direct means of taking advantage of the knowledge derived by its
previous users.
  The AstroDAbis service aims to address this, in a prototype service enabling
astronomers to record annotations and cross-identifications in the AstroDAbis
service, annotating objects in other catalogues. We have deployed two
interfaces to the annotations, namely one astronomy-specific one using the TAP
protocol\}, and a second exploiting generic Linked Open Data (LOD) and RDF
techniques.