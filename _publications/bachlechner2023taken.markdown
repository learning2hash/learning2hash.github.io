---
layout: publication
title: 'Taken By Surprise: Contrast Effect For Similarity Scores'
authors: Thomas C. Bachlechner, Mario Martone, Marjorie Schillo
conference: Arxiv
year: 2023
bibkey: bachlechner2023taken
citations: 0
additional_links: [{name: Code, url: 'https://github.com/MeetElise/surprise-similarity'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.09765'}]
tags: ["Distance Metric Learning"]
short_authors: Thomas C. Bachlechner, Mario Martone, Marjorie Schillo
---
Accurately evaluating the similarity of object vector embeddings is of
critical importance for natural language processing, information retrieval and
classification tasks. Popular similarity scores (e.g cosine similarity) are
based on pairs of embedding vectors and disregard the distribution of the
ensemble from which objects are drawn. Human perception of object similarity
significantly depends on the context in which the objects appear. In this work
we propose the \(\textit\{surprise score\}\), an ensemble-normalized similarity
metric that encapsulates the contrast effect of human perception and
significantly improves the classification performance on zero- and few-shot
document classification tasks. This score quantifies the surprise to find a
given similarity between two elements relative to the pairwise ensemble
similarities. We evaluate this metric on zero/few shot classification and
clustering tasks and typically find 10-15 % better performance compared to raw
cosine similarity. Our code is available at
https://github.com/MeetElise/surprise-similarity.