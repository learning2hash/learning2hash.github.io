---
layout: publication
title: 'Set2box: Similarity Preserving Representation Learning Of Sets'
authors: Geon Lee, Chanyoung Park, Kijung Shin
conference: "Arxiv"
year: 2022
citations: 0
bibkey: lee2022similarity
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2210.03282'}
tags: ['Hashing Methods', 'Applications', 'Efficient Learning', 'Quantization and Compression', 'Tools and Libraries', 'Hashing Fundamentals', 'Quantization']
---
Sets have been used for modeling various types of objects (e.g., a document
as the set of keywords in it and a customer as the set of the items that she
has purchased). Measuring similarity (e.g., Jaccard Index) between sets has
been a key building block of a wide range of applications, including,
plagiarism detection, recommendation, and graph compression. However, as sets
have grown in numbers and sizes, the computational cost and storage required
for set similarity computation have become substantial, and this has led to the
development of hashing and sketching based solutions. In this work, we propose
Set2Box, a learning-based approach for compressed representations of sets from
which various similarity measures can be estimated accurately in constant time.
The key idea is to represent sets as boxes to precisely capture overlaps of
sets. Additionally, based on the proposed box quantization scheme, we design
Set2Box+, which yields more concise but more accurate box representations of
sets. Through extensive experiments on 8 real-world datasets, we show that,
compared to baseline approaches, Set2Box+ is (a) Accurate: achieving up to
40.8X smaller estimation error while requiring 60% fewer bits to encode sets,
(b) Concise: yielding up to 96.8X more concise representations with similar
estimation error, and (c) Versatile: enabling the estimation of four
set-similarity measures from a single representation of each set.
