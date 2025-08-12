---
layout: publication
title: 'Searching By Code: A New Searchbysnippet Dataset And Snipper Retrieval Model
  For Searching By Code Snippets'
authors: Ivan Sedykh, Dmitry Abulkhanov, Nikita Sorokin, Sergey Nikolenko, Valentin
  Malykh
conference: Arxiv
year: 2023
bibkey: sedykh2023searching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.11625'}]
tags: ["Datasets", "Evaluation"]
short_authors: Sedykh et al.
---
Code search is an important and well-studied task, but it usually means
searching for code by a text query. We argue that using a code snippet (and
possibly an error traceback) as a query while looking for bugfixing
instructions and code samples is a natural use case not covered by prior art.
Moreover, existing datasets use code comments rather than full-text
descriptions as text, making them unsuitable for this use case. We present a
new SearchBySnippet dataset implementing the search-by-code use case based on
StackOverflow data; we show that on SearchBySnippet, existing architectures
fall short of a simple BM25 baseline even after fine-tuning. We present a new
single encoder model SnippeR that outperforms several strong baselines on
SearchBySnippet with a result of 0.451 Recall@10; we propose the
SearchBySnippet dataset and SnippeR as a new important benchmark for code
search evaluation.