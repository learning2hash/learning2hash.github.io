---
layout: publication
title: Efficient Computation Of Positional Population Counts Using SIMD Instructions
authors: "Marcus D. R. Klarqvist, Wojciech Mu\u0142a, Daniel Lemire"
conference: 'Concurrency and Computation: Practice and Experience'
year: 2021
bibkey: klarqvist2019efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.02696'}]
tags: []
short_authors: "Marcus D. R. Klarqvist, Wojciech Mu\u0142a, Daniel Lemire"
---
In several fields such as statistics, machine learning, and bioinformatics,
categorical variables are frequently represented as one-hot encoded vectors.
For example, given 8 distinct values, we map each value to a byte where only a
single bit has been set. We are motivated to quickly compute statistics over
such encodings. Given a stream of k-bit words, we seek to compute k distinct
sums corresponding to bit values at indexes 0, 1, 2, ..., k-1. If the k-bit
words are one-hot encoded then the sums correspond to a frequency histogram.
This multiple-sum problem is a generalization of the population-count problem
where we seek the sum of all bit values. Accordingly, we refer to the
multiple-sum problem as a positional population-count. Using SIMD (Single
Instruction, Multiple Data) instructions from recent Intel processors, we
describe algorithms for computing the 16-bit position population count using
less than half of a CPU cycle per 16-bit word. Our best approach uses up to 400
times fewer instructions and is up to 50 times faster than baseline code using
only regular (non-SIMD) instructions, for sufficiently large inputs.