---
layout: publication
title: Optimal Terminal Dimensionality Reduction In Euclidean Space
authors: Shyam Narayanan, Jelani Nelson
conference: Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing
year: 2019
bibkey: narayanan2018optimal
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.09250'}]
tags: []
short_authors: Shyam Narayanan, Jelani Nelson
---
Let \\(\epsilon\in(0,1)\\) and \\(X\subset\mathbb R^d\\) be arbitrary with \\(|X|\\)
having size \\(n>1\\). The Johnson-Lindenstrauss lemma states there exists
\\(f:X\rightarrow\mathbb R^m\\) with \\(m = O(\epsilon^\{-2\}log n)\\) such that $\\(
\forall x\in X\ \forall y\in X, \|x-y\|_2 \le \|f(x)-f(y)\|_2 \le
(1+\epsilon)\|x-y\|_2 . \\)\\( We show that a strictly stronger version of this
statement holds, answering one of the main open questions of [MMMR18]:
"\\)\forall y\in X\\(" in the above statement may be replaced with "\\)\forall
y\in\mathbb R^d\\(", so that \\)f\\( not only preserves distances within \\)X\\(, but
also distances to \\)X\\( from the rest of space. Previously this stronger version
was only known with the worse bound \\)m = O(\epsilon^\{-4\}log n)$. Our proof
is via a tighter analysis of (a specific instantiation of) the embedding recipe
of [MMMR18].