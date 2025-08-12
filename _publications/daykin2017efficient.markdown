---
layout: publication
title: Efficient Pattern Matching In Degenerate Strings With The Burrows-wheeler Transform
authors: "Jacqueline W. Daykin, Richard Groult, Yannick Guesnet, Thierry Lecroq, Arnaud\
  \ Lefebvre, Martine L\xE9onard, Laurent Mouchard, \xC9lise Prieur-gaston, Bruce\
  \ Watson"
conference: Information Processing Letters
year: 2019
bibkey: daykin2017efficient
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01130'}]
tags: ["Efficiency"]
short_authors: Daykin et al.
---
A degenerate or indeterminate string on an alphabet \\(\Sigma\\) is a sequence of
non-empty subsets of \\(\Sigma\\). Given a degenerate string \\(t\\) of length \\(n\\), we
present a new method based on the Burrows--Wheeler transform for searching for
a degenerate pattern of length \\(m\\) in \\(t\\) running in \\(O(mn)\\) time on a constant
size alphabet \\(\Sigma\\). Furthermore, it is a hybrid pattern-matching technique
that works on both regular and degenerate strings. A degenerate string is said
to be conservative if its number of non-solid letters is upper-bounded by a
fixed positive constant \\(q\\); in this case we show that the search complexity
time is \\(O(qm^2)\\). Experimental results show that our method performs well in
practice.