---
layout: publication
title: 'Chunk List: Concurrent Data Structures'
authors: Daniel Szelogowski
conference: Arxiv
year: 2021
bibkey: szelogowski2021chunk
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.00172'}]
tags: []
short_authors: Daniel Szelogowski
---
Chunking data is obviously no new concept; however, I had never found any
data structures that used chunking as the basis of their implementation. I
figured that by using chunking alongside concurrency, I could create an
extremely fast run-time in regards to particular methods as searching and/or
sorting. By using chunking and concurrency to my advantage, I came up with the
chunk list - a dynamic list-based data structure that would separate large
amounts of data into specifically sized chunks, each of which should be able to
be searched at the exact same time by searching each chunk on a separate
thread. As a result of implementing this concept into its own class, I was able
to create something that almost consistently gives around 20x-300x faster
results than a regular ArrayList. However, should speed be a particular issue
even after implementation, users can modify the size of the chunks and
benchmark the speed of using smaller or larger chunks, depending on the amount
of data being stored.