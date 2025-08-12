---
layout: publication
title: Translating Place-related Questions To Geosparql Queries
authors: Ehsan Hamzei, Martin Tomko, Stephan Winter
conference: Proceedings of the ACM Web Conference 2022
year: 2022
bibkey: hamzei2022translating
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.03067'}]
tags: []
short_authors: Ehsan Hamzei, Martin Tomko, Stephan Winter
---
Many place-related questions can only be answered by complex spatial
reasoning, a task poorly supported by factoid question retrieval. Such
reasoning using combinations of spatial and non-spatial criteria pertinent to
place-related questions is increasingly possible on linked data knowledge
bases. Yet, to enable question answering based on linked knowledge bases,
natural language questions must first be re-formulated as formal queries. Here,
we first present an enhanced version of YAGO2geo, the geospatially-enabled
variant of the YAGO2 knowledge base, by linking and adding more than one
million places from OpenStreetMap data to YAGO2. We then propose a novel
approach to translate the place-related questions into logical representations,
theoretically grounded in the core concepts of spatial information. Next, we
use a dynamic template-based approach to generate fully executable GeoSPARQL
queries from the logical representations. We test our approach using the
Geospatial Gold Standard dataset and report substantial improvements over
existing methods.