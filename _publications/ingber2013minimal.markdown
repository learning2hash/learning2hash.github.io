---
layout: publication
title: The Minimal Compression Rate For Similarity Identification
authors: Amir Ingber, Tsachy Weissman
conference: Arxiv
year: 2013
bibkey: ingber2013minimal
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1312.2063'}]
tags: ["Similarity Search"]
short_authors: Amir Ingber, Tsachy Weissman
---
Traditionally, data compression deals with the problem of concisely
representing a data source, e.g. a sequence of letters, for the purpose of
eventual reproduction (either exact or approximate). In this work we are
interested in the case where the goal is to answer similarity queries about the
compressed sequence, i.e. to identify whether or not the original sequence is
similar to a given query sequence. We study the fundamental tradeoff between
the compression rate and the reliability of the queries performed on compressed
data. For i.i.d. sequences, we characterize the minimal compression rate that
allows query answers, that are reliable in the sense of having a vanishing
false-positive probability, when false negatives are not allowed. The result is
partially based on a previous work by Ahlswede et al., and the inherently
typical subset lemma plays a key role in the converse proof. We then
characterize the compression rate achievable by schemes that use lossy source
codes as a building block, and show that such schemes are, in general,
suboptimal. Finally, we tackle the problem of evaluating the minimal
compression rate, by converting the problem to a sequence of convex programs
that can be solved efficiently.