---
layout: publication
title: 'Differentially Private One Permutation Hashing And Bin-wise Consistent Weighted Sampling'
authors: Xiaoyun Li, Ping Li
conference: "Arxiv"
year: 2023
citations: 0
bibkey: li2023differentially
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2306.07674'}
tags: ['Hashing Methods', 'Applications', 'Approximate Nearest Neighbor Search', 'Evaluation Metrics', 'Privacy and Security', 'ANN Search', 'Tools and Libraries', 'Hashing Fundamentals', 'Indexing and Efficiency']
---
Minwise hashing (MinHash) is a standard algorithm widely used in the
industry, for large-scale search and learning applications with the binary
(0/1) Jaccard similarity. One common use of MinHash is for processing massive
n-gram text representations so that practitioners do not have to materialize
the original data (which would be prohibitive). Another popular use of MinHash
is for building hash tables to enable sub-linear time approximate near neighbor
(ANN) search. MinHash has also been used as a tool for building large-scale
machine learning systems. The standard implementation of MinHash requires
applying \\(K\\) random permutations. In comparison, the method of one permutation
hashing (OPH), is an efficient alternative of MinHash which splits the data
vectors into \\(K\\) bins and generates hash values within each bin. OPH is
substantially more efficient and also more convenient to use.
  In this paper, we combine the differential privacy (DP) with OPH (as well as
MinHash), to propose the DP-OPH framework with three variants: DP-OPH-fix,
DP-OPH-re and DP-OPH-rand, depending on which densification strategy is adopted
to deal with empty bins in OPH. A detailed roadmap to the algorithm design is
presented along with the privacy analysis. An analytical comparison of our
proposed DP-OPH methods with the DP minwise hashing (DP-MH) is provided to
justify the advantage of DP-OPH. Experiments on similarity search confirm the
merits of DP-OPH, and guide the choice of the proper variant in different
practical scenarios. Our technique is also extended to bin-wise consistent
weighted sampling (BCWS) to develop a new DP algorithm called DP-BCWS for
non-binary data. Experiments on classification tasks demonstrate that DP-BCWS
is able to achieve excellent utility at around \\(\epsilon = 5\sim 10\\), where
\\(\epsilon\\) is the standard parameter in the language of \\((\epsilon,
\delta)\\)-DP.
