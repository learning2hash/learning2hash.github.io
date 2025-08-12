---
layout: publication
title: 'String2string: A Modern Python Library For String-to-string Algorithms'
authors: Mirac Suzgun, Stuart M. Shieber, Dan Jurafsky
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 3: System Demonstrations)'
year: 2024
bibkey: suzgun2023string2string
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.14395'}]
tags: ["Tools & Libraries"]
short_authors: Mirac Suzgun, Stuart M. Shieber, Dan Jurafsky
---
We introduce string2string, an open-source library that offers a
comprehensive suite of efficient algorithms for a broad range of
string-to-string problems. It includes traditional algorithmic solutions as
well as recent advanced neural approaches to tackle various problems in string
alignment, distance measurement, lexical and semantic search, and similarity
analysis -- along with several helpful visualization tools and metrics to
facilitate the interpretation and analysis of these methods. Notable algorithms
featured in the library include the Smith-Waterman algorithm for pairwise local
alignment, the Hirschberg algorithm for global alignment, the Wagner-Fisher
algorithm for edit distance, BARTScore and BERTScore for similarity analysis,
the Knuth-Morris-Pratt algorithm for lexical search, and Faiss for semantic
search. Besides, it wraps existing efficient and widely-used implementations of
certain frameworks and metrics, such as sacreBLEU and ROUGE, whenever it is
appropriate and suitable. Overall, the library aims to provide extensive
coverage and increased flexibility in comparison to existing libraries for
strings. It can be used for many downstream applications, tasks, and problems
in natural-language processing, bioinformatics, and computational social
sciences. It is implemented in Python, easily installable via pip, and
accessible through a simple API. Source code, documentation, and tutorials are
all available on our GitHub page: https://github.com/stanfordnlp/string2string.