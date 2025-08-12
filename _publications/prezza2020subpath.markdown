---
layout: publication
title: 'Subpath Queries On Compressed Graphs: A Survey'
authors: Nicola Prezza
conference: Algorithms
year: 2021
bibkey: prezza2020subpath
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.10008'}]
tags: ["Survey Paper"]
short_authors: Nicola Prezza
---
Text indexing is a classical algorithmic problem that has been studied for
over four decades: given a text \\(T\\), pre-process it off-line so that, later, we
can quickly count and locate the occurrences of any string (the query pattern)
in \\(T\\) in time proportional to the query's length. The earliest optimal-time
solution to the problem, the suffix tree, dates back to 1973 and requires up to
two orders of magnitude more space than the plain text just to be stored. In
the year 2000, two breakthrough works showed that efficient queries can be
achieved without this space overhead: a fast index be stored in a space
proportional to the text's entropy. These contributions had an enormous impact
in bioinformatics: nowadays, virtually any DNA aligner employs compressed
indexes. Recent trends considered more powerful compression schemes (dictionary
compressors) and generalizations of the problem to labeled graphs: after all,
texts can be viewed as labeled directed paths. In turn, since finite state
automata can be considered as a particular case of labeled graphs, these
findings created a bridge between the fields of compressed indexing and regular
language theory, ultimately allowing to index regular languages and promising
to shed new light on problems such as regular expression matching. This survey
is a gentle introduction to the main landmarks of the fascinating journey that
took us from suffix trees to today's compressed indexes for labeled graphs and
regular languages.