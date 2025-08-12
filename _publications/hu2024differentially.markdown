---
layout: publication
title: On Differentially Private String Distances
authors: Jerry Yao-Chieh Hu, Erzhi Liu, Han Liu, Zhao Song, Lichen Zhang
conference: Arxiv
year: 2024
bibkey: hu2024differentially
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.05750'}]
tags: ["Distance Metric Learning", "Privacy & Security"]
short_authors: Hu et al.
---
Given a database of bit strings \(A_1,\ldots,A_m\in \\{0,1\\}^n\), a fundamental
data structure task is to estimate the distances between a given query \(B\in
\\{0,1\\}^n\) with all the strings in the database. In addition, one might further
want to ensure the integrity of the database by releasing these distance
statistics in a secure manner. In this work, we propose differentially private
(DP) data structures for this type of tasks, with a focus on Hamming and edit
distance. On top of the strong privacy guarantees, our data structures are also
time- and space-efficient. In particular, our data structure is \(\epsilon\)-DP
against any sequence of queries of arbitrary length, and for any query \(B\) such
that the maximum distance to any string in the database is at most \(k\), we
output \(m\) distance estimates. Moreover,
  - For Hamming distance, our data structure answers any query in \(\widetilde
O(mk+n)\) time and each estimate deviates from the true distance by at most
\(\widetilde O(k/e^\{\epsilon/log k\})\);
  - For edit distance, our data structure answers any query in \(\widetilde
O(mk^2+n)\) time and each estimate deviates from the true distance by at most
\(\widetilde O(k/e^\{\epsilon/(log k log n)\})\).
  For moderate \(k\), both data structures support sublinear query operations. We
obtain these results via a novel adaptation of the randomized response
technique as a bit flipping procedure, applied to the sketched strings.