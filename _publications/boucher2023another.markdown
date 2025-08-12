---
layout: publication
title: Another Virtue Of Wavelet Forests?
authors: Christina Boucher, Travis Gagie, Aaron Hong, Yansong Li, Norbert Zeh
conference: 2024 Data Compression Conference (DCC)
year: 2024
bibkey: boucher2023another
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.07809'}]
tags: []
short_authors: Boucher et al.
---
A wavelet forest for a text \\(T [1..n]\\) over an alphabet \\(\sigma\\) takes \\(n H_0
(T) + o (n log \sigma)\\) bits of space and supports access and rank on \\(T\\) in
\\(O (log \sigma)\\) time. K\"arkk\"ainen and Puglisi (2011) implicitly introduced
wavelet forests and showed that when \\(T\\) is the Burrows-Wheeler Transform (BWT)
of a string \\(S\\), then a wavelet forest for \\(T\\) occupies space bounded in terms
of higher-order empirical entropies of \\(S\\) even when the forest is implemented
with uncompressed bitvectors. In this paper we show experimentally that wavelet
forests also have better access locality than wavelet trees and are thus
interesting even when higher-order compression is not effective on \\(S\\), or when
\\(T\\) is not a BWT at all.