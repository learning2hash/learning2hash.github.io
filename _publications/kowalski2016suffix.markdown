---
layout: publication
title: Suffix Arrays With A Twist
authors: Tomasz Kowalski, Szymon Grabowski, Kimmo Fredriksson, Marcin Raniszewski
conference: Computing and Informatics
year: 2019
bibkey: kowalski2016suffix
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.08176'}]
tags: ["Efficiency"]
short_authors: Kowalski et al.
---
The suffix array is a classic full-text index, combining effectiveness with
simplicity. We discuss three approaches aiming to improve its efficiency even
more: changes to the navigation, data layout and adding extra data. In short,
we show that \\((i)\\) how we search for the right interval boundary impacts
significantly the overall search speed, \\((ii)\\) a B-tree data layout easily wins
over the standard one, \\((iii)\\) the well-known idea of a lookup table for the
prefixes of the suffixes can be refined with using compression, \\((iv)\\) caching
prefixes of the suffixes in a helper array can pose a(nother) practical
space-time tradeoff.