---
layout: publication
title: 'Algorithms For Parameterized String Matching With Mismatches'
authors: Apurba Saha, Iftekhar Hakim Kaowsar, Mahdi Hasnat Siyam, M. Sohel Rahman
conference: "Arxiv"
year: 2024
citations: 0
bibkey: saha2024algorithms
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2412.00222'}
tags: ['Cross-Modal', 'Supervised', 'Deep', 'Hashing']
---
Two strings are considered to have parameterized matching when there exists a
bijection of the parameterized alphabet onto itself such that it transforms one
string to another. Parameterized matching has application in software
duplication detection, image processing, and computational biology. We consider
the problem for which a pattern \\(p\\), a text \\(t\\) and a mismatch tolerance limit
\\(k\\) is given and the goal is to find all positions in text \\(t\\), for which
pattern \\(p\\), parameterized matches with \\(|p|\\) length substrings of \\(t\\) with at
most \\(k\\) mismatches. Our main result is an algorithm for this problem with
\\(O(\alpha^2 nlog n + n \alpha^2 \sqrt\{\alpha\} log \left( n \alpha \right))\\)
time complexity, where \\(n = |t|\\) and \\(\alpha = |\Sigma|\\) which is improving for
\\(k=\tilde\{Ω\}(|\Sigma|^\{5/3\})\\) the algorithm by Hazay, Lewenstein and
Sokol. We also present a hashing based probabilistic algorithm for this problem
when \\(k = 1\\) with \\(O \left( n log n \right)\\) time complexity, which we believe
is algorithmically beautiful.
