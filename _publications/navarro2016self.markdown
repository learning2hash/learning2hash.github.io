---
layout: publication
title: A Self-index On Block Trees
authors: Gonzalo Navarro
conference: Lecture Notes in Computer Science
year: 2017
bibkey: navarro2016self
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.06617'}]
tags: ["Tree Based ANN"]
short_authors: Gonzalo Navarro
---
The Block Tree is a recently proposed data structure that reaches compression
close to Lempel-Ziv while supporting efficient direct access to text
substrings. In this paper we show how a self-index can be built on top of a
Block Tree so that it provides efficient pattern searches while using space
proportional to that of the original data structure. More precisely, if a
Lempel-Ziv parse cuts a text of length \\(n\\) into \\(z\\) non-overlapping phrases,
then our index uses \\(O(zlog(n/z))\\) words and finds the \\(occ\\) occurrences of a
pattern of length \\(m\\) in time \\(O(mlog n+occlog^\epsilon n)\\) for any constant
\\(\epsilon>0\\).