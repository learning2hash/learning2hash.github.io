---
layout: publication
title: Parallel Algorithm For Pattern Matching Problems Under Substring Consistent
  Equivalence Relations
authors: Davaajav Jargalsaikhan, Diptarama Hendrian, Ryo Yoshinaka, Ayumi Shinohara
conference: Arxiv
year: 2022
bibkey: jargalsaikhan2022parallel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.13284'}]
tags: []
short_authors: Jargalsaikhan et al.
---
Given a text and a pattern over an alphabet, the pattern matching problem
searches for all occurrences of the pattern in the text. An equivalence
relation \(\approx\) is called a substring consistent equivalence relation
(SCER), if for two strings \(X\) and \(Y\), \(X \approx Y\) implies \(|X| = |Y|\) and
\(X[i:j] \approx Y[i:j]\) for all \(1 \le i \le j \le |X|\). In this paper, we
propose an efficient parallel algorithm for pattern matching under any SCER
using the"duel-and-sweep" paradigm. For a pattern of length \(m\) and a text of
length \(n\), our algorithm runs in \(O(\xi_m^\mathrm\{t\} log^2 m)\) time and
\(O(\xi_m^\mathrm\{w\} \cdot n log^2 m)\) work, with \(O(\tau_n^\mathrm\{t\} +
\xi_m^\mathrm\{t\} log^2 m)\) time and \(O(\tau_n^\mathrm\{w\} + \xi_m^\mathrm\{w\}
\cdot m log^2 m)\) work preprocessing on the Priority Concurrent Read
Concurrent Write Parallel Random-Access Machines (P-CRCW PRAM).