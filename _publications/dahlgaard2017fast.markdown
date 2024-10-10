---
layout: publication
title: Fast Similarity Sketching
authors: Dahlgaard Søren, Langhede Mathias Bæk Tejs, Houen Jakob Bæk Tejs, Thorup Mikkel
conference: "Arxiv"
year: 2017
bibkey: dahlgaard2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.04370"}
tags: ['ARXIV', 'Supervised']
---
We consider the () problem Given a universe (u = 0ldots u-1) we want a random function (S) mapping subsets (Asubseteq u) into vectors (S(A)) of size (t) such that the Jaccard similarity (J(AB) = Acap B/Acup B) between sets (A) and (B) is preserved. More precisely define X_i = S(A)i = S(B)i( and )X = sum_iin t X_i(. We want )EX_i=J(AB) and we want (X) to be strongly concentrated around (EX = t cdot J(AB)) (i.e. Chernoff-style bounds). This is a fundamental problem which has found numerous applications in data mining large-scale classification computer vision similarity search etc. via the classic MinHash algorithm. The vectors (S(A)) are also called (). Strong concentration is critical for often we want to sketch many sets (B_1ldotsB_n) so that we later for a query set (A) can find (one of) the most similar (B_i). It is then critical that no (B_i) looks much more similar to (A) due to errors in the sketch. The seminal (ttimes) algorithm uses (t) random hash functions (h_1ldots h_t) and stores left ( min_ain A h_1(A)ldots min_ain A h_t(A) right )( as the sketch of )A. The main drawback of MinHash is however its (O(tcdot A)) running time and finding a sketch with similar properties and faster running time has been the subject of several papers. (continued...)
