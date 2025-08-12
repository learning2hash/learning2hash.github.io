---
layout: publication
title: Automatic Classification Of Object Code Using Machine Learning
authors: John Clemens
conference: Digital Investigation
year: 2015
bibkey: clemens2015automatic
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.02146'}]
tags: ["Datasets"]
short_authors: John Clemens
---
Recent research has repeatedly shown that machine learning techniques can be
applied to either whole files or file fragments to classify them for analysis.
We build upon these techniques to show that for samples of un-labeled compiled
computer object code, one can apply the same type of analysis to classify
important aspects of the code, such as its target architecture and endianess.
We show that using simple byte-value histograms we retain enough information
about the opcodes within a sample to classify the target architecture with high
accuracy, and then discuss heuristic-based features that exploit information
within the operands to determine endianess. We introduce a dataset with over
16000 code samples from 20 architectures and experimentally show that by using
our features, classifiers can achieve very high accuracy with relatively small
sample sizes.