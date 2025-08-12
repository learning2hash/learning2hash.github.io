---
layout: publication
title: Similarity Search On Computational Notebooks
authors: Misato Horiuchi, Yuya Sasaki, Chuan Xiao, Makoto Onizuka
conference: Arxiv
year: 2022
bibkey: horiuchi2022similarity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.12786'}]
tags: ["Similarity Search"]
short_authors: Horiuchi et al.
---
Computational notebook software such as Jupyter Notebook is popular for data
science tasks. Numerous computational notebooks are available on the Web and
reusable; however, searching for computational notebooks manually is a tedious
task, and so far, there are no tools to search for computational notebooks
effectively and efficiently. In this paper, we propose a similarity search on
computational notebooks and develop a new framework for the similarity search.
Given contents (i.e., source codes, tabular data, libraries, and outputs
formats) in computational notebooks as a query, the similarity search problem
aims to find top-k computational notebooks with the most similar contents. We
define two similarity measures; set-based and graph-based similarities.
Set-based similarity handles each content independently, while graph-based
similarity captures the relationships between contents. Our framework can
effectively prune the candidates of computational notebooks that should not be
in the top-k results. Furthermore, we develop optimization techniques such as
caching and indexing to accelerate the search. Experiments using Kaggle
notebooks show that our method, in particular graph-based similarity, can
achieve high accuracy and high efficiency.