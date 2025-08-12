---
layout: publication
title: Sort Race
authors: Hantao Zhang, Baoluo Meng, Yiwen Liang
conference: 'Software: Practice and Experience'
year: 2022
bibkey: zhang2016sort
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.04471'}]
tags: []
short_authors: Hantao Zhang, Baoluo Meng, Yiwen Liang
---
Sorting is one of the oldest computing problems and is still very important
in the age of big data. Various algorithms and implementation techniques have
been proposed. In this study, we focus on comparison based, internal sorting
algorithms. We created 12 data types of various sizes for experiments and
tested extensively various implementations in a single setting. Using some
effective techniques, we discovered that quicksort is adaptive to nearly sorted
inputs and is still the best overall sorting algorithm. We also identified
which techniques are effective in timsort, one of the most popular and
efficient sorting method based on natural mergesort, and created our version of
mergesort, which runs faster than timsort on nearly sorted instances. Our
implementations of quicksort and mergesort are different from other
implementations reported in all textbooks or research articles, faster than any
version of the C library qsort functions, not only for randomly generated data,
but also for various types of nearly sorted data. This experiment can help the
user to choose the best sorting algorithm for the hard sorting job at hand.
This work provides a platform for anyone to test their own sorting algorithm
against the best in the field.