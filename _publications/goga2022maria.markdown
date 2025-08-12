---
layout: publication
title: 'MARIA: Multiple-alignment \(r\)-index With Aggregation'
authors: "Adri\xE1n Goga, Andrej Bal\xE1\u017E, Alessia Petescia, Travis Gagie"
conference: Arxiv
year: 2022
bibkey: goga2022maria
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.09218'}]
tags: []
short_authors: Goga et al.
---
There now exist compact indexes that can efficiently list all the occurrences
of a pattern in a dataset consisting of thousands of genomes, or even all the
occurrences of all the pattern's maximal exact matches (MEMs) with respect to
the dataset. Unless we are lucky and the pattern is specific to only a few
genomes, however, we could be swamped by hundreds of matches -- or even
hundreds per MEM -- only to discover that most or all of the matches are to
substrings that occupy the same few columns in a multiple alignment. To address
this issue, in this paper we present a simple and compact data index MARIA that
stores a multiple alignment such that, given the position of one match of a
pattern (or a MEM or other substring of a pattern) and its length, we can
quickly list all the distinct columns of the multiple alignment where matches
start.