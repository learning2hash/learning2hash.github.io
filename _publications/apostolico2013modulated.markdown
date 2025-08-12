---
layout: publication
title: Modulated String Searching
authors: "Alberto Apostolico, P\xE9ter L. Erd\u0151s, Istv\xE1n Mikl\xF3s, Johannes\
  \ Siemons"
conference: Theoretical Computer Science
year: 2013
bibkey: apostolico2013modulated
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1302.3437'}]
tags: []
short_authors: Apostolico et al.
---
In his 1987 paper entitled "Generalized String Matching", Abrahamson
introduced \{\em pattern matching with character classes\} and provided the first
efficient algorithm to solve it. The best known solution to date is due to
Linhart and Shamir (2009).
  Another broad yet comparatively less studied class of string matching
problems is that of numerical string searching, such as, e.g., the `less-than'
or \(L_1\)-norm string searching. The best known solutions for problems in this
class are based on FFT convolution after some suitable re-encoding.
  The present paper introduces \{\em modulated string searching\} as a unified
framework for string matching problems where the numerical conditions can be
combined with some Boolean/numerical decision conditions on the character
classes. One example problem in this class is the \{\em locally bounded
\(L_1\)-norm\} matching problem on character classes: here the "match" between a
character at some position in the text and a set of characters at some position
in the pattern is assessed based on the smallest \(L_1\) distance between the
text character and one of those pattern characters. The two positions "match"
if the (absolute value of the) difference between the two characters does not
exceed a predefined constant. The pattern has an occurrence in an alignment
with the text if the sum of all such differences does not exceed a second
predefined constant value. This problem requires a pointwise evaluation of the
quality of each match and has no known solution based on the previously
mentioned algorithms.