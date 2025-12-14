---
layout: publication
title: Sampled Image Tagging And Retrieval Methods On User Generated Content
authors: Karl Ni, Kyle Zaragoza, Charles Foster, Carmen Carrano, Barry Chen, Yonas
  Tesfaye, Alex Gude
conference: Arxiv
year: 2016
bibkey: ni2016sampled
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.06962'}]
tags: [Few-shot & Zero-shot, Neural Hashing, Datasets, Robustness, Scalability]
short_authors: Ni et al.
---
Traditional image tagging and retrieval algorithms have limited value as a
result of being trained with heavily curated datasets. These limitations are
most evident when arbitrary search words are used that do not intersect with
training set labels. Weak labels from user generated content (UGC) found in the
wild (e.g., Google Photos, FlickR, etc.) have an almost unlimited number of
unique words in the metadata tags. Prior work on word embeddings successfully
leveraged unstructured text with large vocabularies, and our proposed method
seeks to apply similar cost functions to open source imagery. Specifically, we
train a deep learning image tagging and retrieval system on large scale, user
generated content (UGC) using sampling methods and joint optimization of word
embeddings. By using the Yahoo! FlickR Creative Commons (YFCC100M) dataset,
such an approach builds robustness to common unstructured data issues that
include but are not limited to irrelevant tags, misspellings, multiple
languages, polysemy, and tag imbalance. As a result, the final proposed
algorithm will not only yield comparable results to state of the art in
conventional image tagging, but will enable new capability to train algorithms
on large, scale unstructured text in the YFCC100M dataset and outperform cited
work in zero-shot capability.