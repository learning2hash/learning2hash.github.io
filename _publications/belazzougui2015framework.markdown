---
layout: publication
title: A Framework For Space-efficient String Kernels
authors: Djamal Belazzougui, Fabio Cunial
conference: Algorithmica
year: 2017
bibkey: belazzougui2015framework
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.06370'}]
tags: []
short_authors: Djamal Belazzougui, Fabio Cunial
---
String kernels are typically used to compare genome-scale sequences whose
length makes alignment impractical, yet their computation is based on data
structures that are either space-inefficient, or incur large slowdowns. We show
that a number of exact string kernels, like the \\(k\\)-mer kernel, the substrings
kernels, a number of length-weighted kernels, the minimal absent words kernel,
and kernels with Markovian corrections, can all be computed in \\(O(nd)\\) time and
in \\(o(n)\\) bits of space in addition to the input, using just a
\\(\mathtt\{rangeDistinct\}\\) data structure on the Burrows-Wheeler transform of the
input strings, which takes \\(O(d)\\) time per element in its output. The same
bounds hold for a number of measures of compositional complexity based on
multiple value of \\(k\\), like the \\(k\\)-mer profile and the \\(k\\)-th order empirical
entropy, and for calibrating the value of \\(k\\) using the data.