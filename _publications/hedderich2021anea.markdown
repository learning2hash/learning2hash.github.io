---
layout: publication
title: 'ANEA: Distant Supervision For Low-resource Named Entity Recognition'
authors: Michael A. Hedderich, Lukas Lange, Dietrich Klakow
conference: Arxiv
year: 2021
bibkey: hedderich2021anea
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.13129'}]
tags: []
short_authors: Michael A. Hedderich, Lukas Lange, Dietrich Klakow
---
Distant supervision allows obtaining labeled training corpora for
low-resource settings where only limited hand-annotated data exists. However,
to be used effectively, the distant supervision must be easy to gather. In this
work, we present ANEA, a tool to automatically annotate named entities in texts
based on entity lists. It spans the whole pipeline from obtaining the lists to
analyzing the errors of the distant supervision. A tuning step allows the user
to improve the automatic annotation with their linguistic insights without
labelling or checking all tokens manually. In six low-resource scenarios, we
show that the F1-score can be increased by on average 18 points through
distantly supervised data obtained by ANEA.