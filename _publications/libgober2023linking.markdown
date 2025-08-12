---
layout: publication
title: Linking Datasets On Organizations Using Half A Billion Open-collaborated Records
authors: Brian Libgober, Connor T. Jerzak
conference: Political Science Research and Methods
year: 2024
bibkey: libgober2023linking
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.02533'}]
tags: ["Datasets"]
short_authors: Brian Libgober, Connor T. Jerzak
---
Scholars studying organizations often work with multiple datasets lacking
shared identifiers or covariates. In such situations, researchers usually use
approximate string ("fuzzy") matching methods to combine datasets. String
matching, although useful, faces fundamental challenges. Even where two strings
appear similar to humans, fuzzy matching often struggles because it fails to
adapt to the informativeness of the character combinations. In response, a
number of machine learning methods have been developed to refine string
matching. Yet, the effectiveness of these methods is limited by the size and
diversity of training data. This paper introduces data from a prominent
employment networking site (LinkedIn) as a massive training corpus to address
these limitations. By leveraging information from the LinkedIn corpus regarding
organizational name-to-name links, we incorporate trillions of name pair
examples into various methods to enhance existing matching benchmarks and
performance by explicitly maximizing match probabilities. We also show how
relationships between organization names can be modeled using a network
representation of the LinkedIn data. In illustrative merging tasks involving
lobbying firms, we document improvements when using the LinkedIn corpus in
matching calibration and make all data and methods open source.