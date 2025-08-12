---
layout: publication
title: Fast And Linear-time String Matching Algorithms Based On The Distances Of \(q\)-gram
  Occurrences
authors: Satoshi Kobayashi, Diptarama Hendrian, Ryo Yoshinaka, Ayumi Shinohara
conference: Arxiv
year: 2020
bibkey: kobayashi2020fast
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.08004'}]
tags: []
short_authors: Kobayashi et al.
---
Given a text \(T\) of length \(n\) and a pattern \(P\) of length \(m\), the string
matching problem is a task to find all occurrences of \(P\) in \(T\). In this
study, we propose an algorithm that solves this problem in \(O((n + m)q)\) time
considering the distance between two adjacent occurrences of the same \(q\)-gram
contained in \(P\). We also propose a theoretical improvement of it which runs in
\(O(n + m)\) time, though it is not necessarily faster in practice. We compare
the execution times of our and existing algorithms on various kinds of real and
artificial datasets such as an English text, a genome sequence and a Fibonacci
string. The experimental results show that our algorithm is as fast as the
state-of-the-art algorithms in many cases, particularly when a pattern
frequently appears in a text.