---
layout: publication
title: 'Fairest Neighbors: Tradeoffs Between Metric Queries'
authors: Magnus Lie Hetland, Halvard Hummel
conference: Arxiv
year: 2021
bibkey: hetland2021fairest
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.03621'}]
tags: ["Efficiency", "Vector Indexing"]
short_authors: Magnus Lie Hetland, Halvard Hummel
---
Metric search commonly involves finding objects similar to a given sample
object. We explore a generalization, where the desired result is a fair
tradeoff between multiple query objects. This builds on previous results on
complex queries, such as linear combinations. We instead use measures of
inequality, like ordered weighted averages, and query existing index structures
to find objects that minimize these. We compare our method empirically to
linear scan and a post hoc combination of individual queries, and demonstrate a
considerable speedup.