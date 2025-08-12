---
layout: publication
title: 'Card-660: Cambridge Rare Word Dataset - A Reliable Benchmark For Infrequent
  Word Representation Models'
authors: Mohammad Taher Pilehvar, Dimitri Kartsaklis, Victor Prokhorov, Nigel Collier
conference: Proceedings of the 2018 Conference on Empirical Methods in Natural Language
  Processing
year: 2018
bibkey: pilehvar2018card
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.09308'}]
tags: ["Datasets", "EMNLP", "Tools & Libraries"]
short_authors: Pilehvar et al.
---
Rare word representation has recently enjoyed a surge of interest, owing to
the crucial role that effective handling of infrequent words can play in
accurate semantic understanding. However, there is a paucity of reliable
benchmarks for evaluation and comparison of these techniques. We show in this
paper that the only existing benchmark (the Stanford Rare Word dataset) suffers
from low-confidence annotations and limited vocabulary; hence, it does not
constitute a solid comparison framework. In order to fill this evaluation gap,
we propose CAmbridge Rare word Dataset (Card-660), an expert-annotated word
similarity dataset which provides a highly reliable, yet challenging, benchmark
for rare word representation techniques. Through a set of experiments we show
that even the best mainstream word embeddings, with millions of words in their
vocabularies, are unable to achieve performances higher than 0.43 (Pearson
correlation) on the dataset, compared to a human-level upperbound of 0.90. We
release the dataset and the annotation materials at
https://pilehvar.github.io/card-660/.