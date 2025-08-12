---
layout: publication
title: Generalized Dictionary Matching Under Substring Consistent Equivalence Relations
authors: Diptarama Hendrian
conference: Lecture Notes in Computer Science
year: 2020
bibkey: hendrian2019generalized
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.07538'}]
tags: []
short_authors: Diptarama Hendrian
---
Given a set of patterns called a dictionary and a text, the dictionary
matching problem is a task to find all occurrence positions of all patterns in
the text. The dictionary matching problem can be solved efficiently by using
the Aho-Corasick algorithm. Recently, Matsuoka et al. [TCS, 2016] proposed a
generalization of pattern matching problem under substring consistent
equivalence relations and presented a generalization of the Knuth-Morris-Pratt
algorithm to solve this problem. An equivalence relation \\(\approx\\) is a
substring consistent equivalence relation (SCER) if for two strings \\(X,Y\\), \\(X
\approx Y\\) implies \\(|X| = |Y|\\) and \\(X[i:j] \approx Y[i:j]\\) for all \\(1 \le i \le
j \le |X|\\). In this paper, we propose a generalization of the dictionary
matching problem and present a generalization of the Aho-Corasick algorithm for
the dictionary matching under SCER. We present an algorithm that constructs
SCER automata and an algorithm that performs dictionary matching under SCER by
using the automata. Moreover, we show the time and space complexity of our
algorithms with respect to the size of input strings.