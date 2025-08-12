---
layout: publication
title: Minimal Suffix And Rotation Of A Substring In Optimal Time
authors: Tomasz Kociumaka
conference: Arxiv
year: 2016
bibkey: kociumaka2016minimal
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.08051'}]
tags: ["Efficiency"]
short_authors: Tomasz Kociumaka
---
For a text given in advance, the substring minimal suffix queries ask to
determine the lexicographically minimal non-empty suffix of a substring
specified by the location of its occurrence in the text. We develop a data
structure answering such queries optimally: in constant time after linear-time
preprocessing. This improves upon the results of Babenko et al. (CPM 2014),
whose trade-off solution is characterized by \(\Theta(nlog n)\) product of these
time complexities. Next, we extend our queries to support concatenations of
\(O(1)\) substrings, for which the construction and query time is preserved. We
apply these generalized queries to compute lexicographically minimal and
maximal rotations of a given substring in constant time after linear-time
preprocessing.
  Our data structures mainly rely on properties of Lyndon words and Lyndon
factorizations. We combine them with further algorithmic and combinatorial
tools, such as fusion trees and the notion of order isomorphism of strings.