---
layout: publication
title: On Practical Accuracy Of Edit Distance Approximation Algorithms
authors: Hiroyuki Hanada, Mineichi Kudo, Atsuyoshi Nakamura
conference: Arxiv
year: 2017
bibkey: hanada2017practical
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.06134'}]
tags: ["Evaluation"]
short_authors: Hiroyuki Hanada, Mineichi Kudo, Atsuyoshi Nakamura
---
The edit distance is a basic string similarity measure used in many
applications such as text mining, signal processing, bioinformatics, and so on.
However, the computational cost can be a problem when we repeat many distance
calculations as seen in real-life searching situations. A promising solution to
cope with the problem is to approximate the edit distance by another distance
with a lower computational cost. There are, indeed, many distances have been
proposed for approximating the edit distance. However, their approximation
accuracies are evaluated only theoretically: many of them are evaluated only
with big-oh (asymptotic) notations, and without experimental analysis.
Therefore, it is beneficial to know their actual performance in real
applications. In this study we compared existing six approximation distances in
two approaches: (i) we refined their theoretical approximation accuracy by
calculating up to the constant coefficients, and (ii) we conducted some
experiments, in one artificial and two real-life data sets, to reveal under
which situations they perform best. As a result we obtained the following
results: [Batu 2006] is the best theoretically and [Andoni 2010]
experimentally. Theoretical considerations show that [Batu 2006] is the best if
the string length n is large enough (n >= 300). [Andoni 2010] is experimentally
the best for most data sets and theoretically the second best. [Bar-Yossef
2004], [Charikar 2006] and [Sokolov 2007], despite their middle-level
theoretical performance, are experimentally as good as [Andoni 2010] for pairs
of strings with large alphabet size.