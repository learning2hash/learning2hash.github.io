---
layout: publication
title: MONI Can Find K-mems
authors: Igor Tatarnikov, Ardavan Shahrabi Farahani, Sana Kashgouli, Travis Gagie
conference: Arxiv
year: 2022
bibkey: tatarnikov2022moni
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.05085'}]
tags: ["Efficiency"]
short_authors: Tatarnikov et al.
---
Suppose we are asked to index a text \(T [0..n - 1]\) such that, given a
pattern \(P [0..m - 1]\), we can quickly report the maximal substrings of \(P\)
that each occur in \(T\) at least \(k\) times. We first show how we can add \(O (r
log n)\) bits to Rossi et al.'s recent MONI index, where \(r\) is the number of
runs in the Burrows-Wheeler Transform of \(T\), such that it supports such
queries in \(O (k m log n)\) time. We then show how, if we are given \(k\) at
construction time, we can reduce the query time to \(O (m log n)\).