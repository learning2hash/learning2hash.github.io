---
layout: publication
title: Semantics Of Negative Sequential Patterns
authors: Thomas Guyet, Philippe Besnard
conference: Frontiers in Artificial Intelligence and Applications
year: 2020
bibkey: guyet2020semantics
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06920'}]
tags: []
short_authors: Thomas Guyet, Philippe Besnard
---
In the field of pattern mining, a negative sequential pattern is specified by
means of a sequence consisting of events to occur and of other events, called
negative events, to be absent. For instance, containment of the pattern
\(\langle a\ \neg b\ c\rangle\) arises with an occurrence of a and a subsequent
occurrence of c but no occurrence of b in between. This article is to shed
light on the ambiguity of such a seemingly intuitive notation and we identify
eight possible semantics for the containment relation between a pattern and a
sequence. These semantics are illustrated and formally studied, in particular
we propose dominance and equivalence relations between them. Also we prove that
support is anti-monotonic for some of these semantics. Some of the results are
discussed with the aim of developing algorithms to extract efficiently frequent
negative patterns.