---
layout: publication
title: Quantum Search In A Dictionary Based On Fingerprinting-hashing
authors: Farid Ablayev, Nailya Salikhova, Marat Ablayev
conference: Arxiv
year: 2024
citations: 0
bibkey: ablayev2024quantum
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.11422'}]
tags: [Hashing Methods, ANN Search]
---
In this work, we present a quantum query algorithm for searching a word of
length \\(m\\) in an unsorted dictionary of size \\(n\\). The algorithm uses
\\(O(\sqrt\{n\})\\) queries (Grover operators), like previously known algorithms.
  What is new is that the algorithm is based on the quantum
fingerprinting-hashing technique, which (a) provides a first level of amplitude
amplification before applying the sequence of Grover amplitude amplification
operators and (b) makes the algorithm more efficient in terms of memory use --
it requires \\(O(log n + log m)\\) qubits.
  Note that previously developed algorithms by other researchers without
hashing require \\(O(log n + m)\\) qubits.