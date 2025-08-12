---
layout: publication
title: Faster Population Counts Using AVX2 Instructions
authors: "Wojciech Mu\u0142a, Nathan Kurz, Daniel Lemire"
conference: The Computer Journal
year: 2017
bibkey: "mu\u0142a2016faster"
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.07612'}]
tags: ["Efficiency"]
short_authors: "Wojciech Mu\u0142a, Nathan Kurz, Daniel Lemire"
---
Counting the number of ones in a binary stream is a common operation in
database, information-retrieval, cryptographic and machine-learning
applications. Most processors have dedicated instructions to count the number
of ones in a word (e.g., popcnt on x64 processors). Maybe surprisingly, we show
that a vectorized approach using SIMD instructions can be twice as fast as
using the dedicated instructions on recent Intel processors. The benefits can
be even greater for applications such as similarity measures (e.g., the Jaccard
index) that require additional Boolean operations. Our approach has been
adopted by LLVM: it is used by its popular C compiler (clang).