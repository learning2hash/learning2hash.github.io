---
layout: publication
title: Searching In One Billion Vectors Re-rank With Source Coding
authors: Jégou Hervé Inria - Irisa, Tavenard Romain Inria - Irisa, Douze Matthijs Inria Rhône-alpes / Ljk Laboratoire Jean Kuntzmann, Sed, Amsaleg Laurent Inria - Irisa
conference: "Arxiv"
year: 2011
bibkey: jégou2011searching
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1102.3828"}
tags: ['ARXIV', 'Quantisation']
---
<p>Recent indexing techniques inspired by source coding have been shown
successful to index billions of high-dimensional vectors in memory. In
this paper, we propose an approach that re-ranks the neighbor hypotheses
obtained by these compressed-domain indexing methods. In contrast to the
usual post-verification scheme, which performs exact distance
calculation on the short-list of hypotheses, the estimated distances are
refined based on short quantization codes, to avoid reading the full
vectors from disk. We have released a new public dataset of one billion
128-dimensional vectors and proposed an experimental setup to evaluate
high dimensional indexing algorithms on a realistic scale. Experiments
show that our method accurately and efficiently re-ranks the neighbor
hypotheses using little memory compared to the full vectors
representation.</p>
