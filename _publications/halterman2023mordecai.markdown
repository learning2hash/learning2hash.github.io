---
layout: publication
title: 'Mordecai 3: A Neural Geoparser And Event Geocoder'
authors: Andrew Halterman
conference: Arxiv
year: 2023
bibkey: halterman2023mordecai
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.13675'}]
tags: ["Tools & Libraries"]
short_authors: Andrew Halterman
---
Mordecai3 is a new end-to-end text geoparser and event geolocation system.
The system performs toponym resolution using a new neural ranking model to
resolve a place name extracted from a document to its entry in the Geonames
gazetteer. It also performs event geocoding, the process of linking events
reported in text with the place names where they are reported to occur, using
an off-the-shelf question-answering model. The toponym resolution model is
trained on a diverse set of existing training data, along with several thousand
newly annotated examples. The paper describes the model, its training process,
and performance comparisons with existing geoparsers. The system is available
as an open source Python library, Mordecai 3, and replaces an earlier
geoparser, Mordecai v2, one of the most widely used text geoparsers (Halterman
2017).