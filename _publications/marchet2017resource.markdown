---
layout: publication
title: A Resource-frugal Probabilistic Dictionary And Applications In Bioinformatics
authors: Camille Marchet, Lolita Lecompte, Antoine Limasset, Lucie Bittner, Pierre
  Peterlongo
conference: Discrete Applied Mathematics
year: 2018
bibkey: marchet2017resource
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.00667'}]
tags: ["Efficiency", "Hashing Methods", "Memory Efficiency"]
short_authors: Marchet et al.
---
Indexing massive data sets is extremely expensive for large scale problems.
In many fields, huge amounts of data are currently generated, however
extracting meaningful information from voluminous data sets, such as computing
similarity between elements, is far from being trivial. It remains nonetheless
a fundamental need. This work proposes a probabilistic data structure based on
a minimal perfect hash function for indexing large sets of keys. Our structure
out-compete the hash table for construction, query times and for memory usage,
in the case of the indexation of a static set. To illustrate the impact of
algorithms performances, we provide two applications based on similarity
computation between collections of sequences, and for which this calculation is
an expensive but required operation. In particular, we show a practical case in
which other bioinformatics tools fail to scale up the tested data set or
provide lower recall quality results.