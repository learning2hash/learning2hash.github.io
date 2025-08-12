---
layout: publication
title: 'PADDLE: Proximal Algorithm For Dual Dictionaries Learning'
authors: Curzio Basso, Matteo Santoro, Alessandro Verri, Silvia Villa
conference: Lecture Notes in Computer Science
year: 2011
bibkey: basso2010paddle
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1011.3728'}]
tags: []
short_authors: Basso et al.
---
Recently, considerable research efforts have been devoted to the design of
methods to learn from data overcomplete dictionaries for sparse coding.
However, learned dictionaries require the solution of an optimization problem
for coding new data. In order to overcome this drawback, we propose an
algorithm aimed at learning both a dictionary and its dual: a linear mapping
directly performing the coding. By leveraging on proximal methods, our
algorithm jointly minimizes the reconstruction error of the dictionary and the
coding error of its dual; the sparsity of the representation is induced by an
\\(\ell_1\\)-based penalty on its coefficients. The results obtained on synthetic
data and real images show that the algorithm is capable of recovering the
expected dictionaries. Furthermore, on a benchmark dataset, we show that the
image features obtained from the dual matrix yield state-of-the-art
classification performance while being much less computational intensive.