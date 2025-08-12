---
layout: publication
title: Hybrid Indexes For Repetitive Datasets
authors: H. Ferrada, T. Gagie, T. Hirvola, S. J. Puglisi
conference: 'Philosophical Transactions of the Royal Society A: Mathematical, Physical
  and Engineering Sciences'
year: 2014
bibkey: ferrada2013hybrid
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1306.4037'}]
tags: ["Datasets", "Hybrid ANN Methods"]
short_authors: Ferrada et al.
---
Advances in DNA sequencing mean databases of thousands of human genomes will
soon be commonplace. In this paper we introduce a simple technique for reducing
the size of conventional indexes on such highly repetitive texts. Given upper
bounds on pattern lengths and edit distances, we preprocess the text with LZ77
to obtain a filtered text, for which we store a conventional index. Later,
given a query, we find all matches in the filtered text, then use their
positions and the structure of the LZ77 parse to find all matches in the
original text. Our experiments show this also significantly reduces query
times.