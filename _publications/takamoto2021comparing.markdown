---
layout: publication
title: Comparing Two Counting Methods For Estimating The Probabilities Of Strings
authors: Ayaka Takamoto, Mitsuo Yoshida, Kyoji Umemura
conference: '2021 8th International Conference on Advanced Informatics: Concepts,
  Theory and Applications (ICAICTA)'
year: 2021
bibkey: takamoto2021comparing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.04024'}]
tags: []
short_authors: Ayaka Takamoto, Mitsuo Yoshida, Kyoji Umemura
---
There are two methods for counting the number of occurrences of a string in
another large string. One is to count the number of places where the string is
found. The other is to determine how many pieces of string can be extracted
without overlapping. The difference between the two becomes apparent when the
string is part of a periodic pattern. This research reports that the difference
is significant in estimating the occurrence probability of a pattern.
  In this study, the strings used in the experiments are approximated from
time-series data. The task involves classifying strings by estimating the
probability or computing the information quantity. First, the frequencies of
all substrings of a string are computed. Each counting method may sometimes
produce different frequencies for an identical string. Second, the probability
of the most probable segmentation is selected. The probability of the string is
the product of all probabilities of substrings in the selected segmentation.
The classification results demonstrate that the difference in counting methods
is statistically significant, and that the method without overlapping is
better.