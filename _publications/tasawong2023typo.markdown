---
layout: publication
title: Typo-robust Representation Learning For Dense Retrieval
authors: Panuthep Tasawong, Wuttikorn Ponwitayarat, Peerat Limkonchotiwat, Can Udomcharoenchaikit,
  Ekapol Chuangsuwanich, Sarana Nutanong
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2023
bibkey: tasawong2023typo
citations: 4
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2306.10348'}]
tags: ["Datasets", "Evaluation"]
short_authors: Tasawong et al.
---
Dense retrieval is a basic building block of information retrieval
applications. One of the main challenges of dense retrieval in real-world
settings is the handling of queries containing misspelled words. A popular
approach for handling misspelled queries is minimizing the representations
discrepancy between misspelled queries and their pristine ones. Unlike the
existing approaches, which only focus on the alignment between misspelled and
pristine queries, our method also improves the contrast between each misspelled
query and its surrounding queries. To assess the effectiveness of our proposed
method, we compare it against the existing competitors using two benchmark
datasets and two base encoders. Our method outperforms the competitors in all
cases with misspelled queries. Our code and models are available at
https://github. com/panuthept/DST-DenseRetrieval.