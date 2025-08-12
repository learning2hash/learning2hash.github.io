---
layout: publication
title: Practical KMP/BM Style Pattern-matching On Indeterminate Strings
authors: Hossein Dehghani, Neerja Mhaskar, W. F. Smyth
conference: Arxiv
year: 2022
bibkey: dehghani2022practical
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.08331'}]
tags: []
short_authors: Hossein Dehghani, Neerja Mhaskar, W. F. Smyth
---
In this paper we describe two simple, fast, space-efficient algorithms for
finding all matches of an indeterminate pattern \(p = p[1..m]\) in an
indeterminate string \(x = x[1..n]\), where both \(p\) and \(x\) are defined on a
"small" ordered alphabet \(\Sigma\) \(-\) say, \(\sigma = |\Sigma| \le 9\). Both
algorithms depend on a preprocessing phase that replaces \(\Sigma\) by an integer
alphabet \(\Sigma_I\) of size \(\sigma_I = \sigma\) which (reversibly, in time
linear in string length) maps both \(x\) and \(p\) into equivalent regular strings
\(y\) and \(q\), respectively, on \(\Sigma_I\), whose maximum (indeterminate) letter
can be expressed in a 32-bit word (for \(\sigma \le 4\), thus for DNA sequences,
an 8-bit representation suffices). We first describe an efficient version KMP
Indet of the venerable Knuth-Morris-Pratt algorithm to find all occurrences of
\(q\) in \(y\) (that is, of \(p\) in \(x\)), but, whenever necessary, using the prefix
array, rather than the border array, to control shifts of the transformed
pattern \(q\) along the transformed string \(y\). We go on to describe a similar
efficient version BM Indet of the Boyer- Moore algorithm that turns out to
execute significantly faster than KMP Indet over a wide range of test cases. A
noteworthy feature is that both algorithms require very little additional
space: \(\Theta(m)\) words. We conjecture that a similar approach may yield
practical and efficient indeterminate equivalents to other well-known
pattern-matching algorithms, in particular the several variants of Boyer-Moore.