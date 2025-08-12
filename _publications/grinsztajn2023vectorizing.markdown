---
layout: publication
title: 'Vectorizing String Entries For Data Processing On Tables: When Are Larger
  Language Models Better?'
authors: "L\xE9o Grinsztajn, Edouard Oyallon, Myung Jun Kim, Ga\xEBl Varoquaux"
conference: Arxiv
year: 2023
bibkey: grinsztajn2023vectorizing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09634'}]
tags: []
short_authors: Grinsztajn et al.
---
There are increasingly efficient data processing pipelines that work on
vectors of numbers, for instance most machine learning models, or vector
databases for fast similarity search. These require converting the data to
numbers. While this conversion is easy for simple numerical and categorical
entries, databases are strife with text entries, such as names or descriptions.
In the age of large language models, what's the best strategies to vectorize
tables entries, baring in mind that larger models entail more operational
complexity? We study the benefits of language models in 14 analytical tasks on
tables while varying the training size, as well as for a fuzzy join benchmark.
We introduce a simple characterization of a column that reveals two settings:
1) a dirty categories setting, where strings share much similarities across
entries, and conversely 2) a diverse entries setting. For dirty categories,
pretrained language models bring little-to-no benefit compared to simpler
string models. For diverse entries, we show that larger language models improve
data processing. For these we investigate the complexity-performance tradeoffs
and show that they reflect those of classic text embedding: larger models tend
to perform better, but it is useful to fine tune them for embedding purposes.