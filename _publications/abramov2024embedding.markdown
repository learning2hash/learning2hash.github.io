---
layout: publication
title: Embedding-based Search In Jetbrains Ides
authors: Evgeny Abramov, Nikolai Palchikov
conference: Arxiv
year: 2024
bibkey: abramov2024embedding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14975'}]
tags: ["Similarity Search"]
short_authors: Evgeny Abramov, Nikolai Palchikov
---
Most modern Integrated Development Environments (IDEs) and code editors have
a feature to search across available functionality and items in an open
project. In JetBrains IDEs, this feature is called Search Everywhere: it allows
users to search for files, actions, classes, symbols, settings, and anything
from VCS history from a single entry point. However, it works with the
candidates obtained by algorithms that don't account for semantics, e.g.,
synonyms, complex word permutations, part of the speech modifications, and
typos. In this work, we describe the machine learning approach we implemented
to improve the discoverability of search items. We also share the obstacles
encountered during this process and how we overcame them.