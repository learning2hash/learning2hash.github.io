---
layout: publication
title: Wavelet Decomposition Of Software Entropy Reveals Symptoms Of Malicious Code
authors: Michael Wojnowicz, Glenn Chisholm, Matt Wolff, Xuan Zhao
conference: Journal of Innovation in Digital Ecosystems
year: 2016
bibkey: wojnowicz2016wavelet
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.04950'}]
tags: []
short_authors: Wojnowicz et al.
---
Sophisticated malware authors can sneak hidden malicious code into portable
executable files, and this code can be hard to detect, especially if encrypted
or compressed. However, when an executable file switches between code regimes
(e.g. native, encrypted, compressed, text, and padding), there are
corresponding shifts in the file's representation as an entropy signal. In this
paper, we develop a method for automatically quantifying the extent to which
patterned variations in a file's entropy signal make it "suspicious." In
Experiment 1, we use wavelet transforms to define a Suspiciously Structured
Entropic Change Score (SSECS), a scalar feature that quantifies the
suspiciousness of a file based on its distribution of entropic energy across
multiple levels of spatial resolution. Based on this single feature, it was
possible to raise predictive accuracy on a malware detection task from 50.0% to
68.7%, even though the single feature was applied to a heterogeneous corpus of
malware discovered "in the wild." In Experiment 2, we describe how
wavelet-based decompositions of software entropy can be applied to a parasitic
malware detection task involving large numbers of samples and features. By
extracting only string and entropy features (with wavelet decompositions) from
software samples, we are able to obtain almost 99% detection of parasitic
malware with fewer than 1% false positives on good files. Moreover, the
addition of wavelet-based features uniformly improved detection performance
across plausible false positive rates, both in a strings-only model (e.g., from
80.90% to 82.97%) and a strings-plus-entropy model (e.g. from 92.10% to 94.74%,
and from 98.63% to 98.90%). Overall, wavelet decomposition of software entropy
can be useful for machine learning models for detecting malware based on
extracting millions of features from executable files.