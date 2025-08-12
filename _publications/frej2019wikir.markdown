---
layout: publication
title: 'WIKIR: A Python Toolkit For Building A Large-scale Wikipedia-based English
  Information Retrieval Dataset'
authors: Jibril Frej, Didier Schwab, Jean-Pierre Chevallet
conference: Arxiv
year: 2019
bibkey: frej2019wikir
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.01901'}]
tags: ["Scalability", "Tools & Libraries"]
short_authors: Jibril Frej, Didier Schwab, Jean-Pierre Chevallet
---
Over the past years, deep learning methods allowed for new state-of-the-art
results in ad-hoc information retrieval. However such methods usually require
large amounts of annotated data to be effective. Since most standard ad-hoc
information retrieval datasets publicly available for academic research (e.g.
Robust04, ClueWeb09) have at most 250 annotated queries, the recent deep
learning models for information retrieval perform poorly on these datasets.
These models (e.g. DUET, Conv-KNRM) are trained and evaluated on data collected
from commercial search engines not publicly available for academic research
which is a problem for reproducibility and the advancement of research. In this
paper, we propose WIKIR: an open-source toolkit to automatically build
large-scale English information retrieval datasets based on Wikipedia. WIKIR is
publicly available on GitHub. We also provide wikIR78k and wikIRS78k: two
large-scale publicly available datasets that both contain 78,628 queries and
3,060,191 (query, relevant documents) pairs.