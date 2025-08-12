---
layout: publication
title: Top-k String Auto-completion With Synonyms
authors: Pengfei Xu, Jiaheng Lu
conference: Lecture Notes in Computer Science
year: 2017
bibkey: xu2016top
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.03751'}]
tags: []
short_authors: Pengfei Xu, Jiaheng Lu
---
Auto-completion is one of the most prominent features of modern information
systems. The existing solutions of auto-completion provide the suggestions
based on the beginning of the currently input character sequence (i.e. prefix).
However, in many real applications, one entity often has synonyms or
abbreviations. For example, "DBMS" is an abbreviation of "Database Management
Systems". In this paper, we study a novel type of auto-completion by using
synonyms and abbreviations. We propose three trie-based algorithms to solve the
top-k auto-completion with synonyms; each one with different space and time
complexity trade-offs. Experiments on large-scale datasets show that it is
possible to support effective and efficient synonym-based retrieval of
completions of a million strings with thousands of synonyms rules at about a
microsecond per-completion, while taking small space overhead (i.e. 160-200
bytes per string). The source code of our experiments can be download at:
http://udbms.cs.helsinki.fi/?projects/autocompletion/download .