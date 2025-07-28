---
layout: publication
title: 'Leader: Prefixing A Length For Faster Word Vector Serialization'
authors: Brian Lester
conference: Arxiv
year: 2020
bibkey: lester2020leader
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.13699'}]
tags: ["Tools & Libraries"]
short_authors: Brian Lester
---
Two competing file formats have become the de facto standards for
distributing pre-trained word embeddings. Both are named after the most popular
pre-trained embeddings that are distributed in that format. The GloVe format is
an entirely text based format that suffers from huge file sizes and slow reads,
and the word2vec format is a smaller binary format that mixes a textual
representation of words with a binary representation of the vectors themselves.
Both formats have problems that we solve with a new format we call the Leader
format. We include a word length prefix for faster reads while maintaining the
smaller file size a binary format offers. We also created a minimalist library
to facilitate the reading and writing of various word vector formats, as well
as tools for converting pre-trained embeddings to our new Leader format.