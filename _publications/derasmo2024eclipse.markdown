---
layout: publication
title: 'ECLIPSE: Contrastive Dimension Importance Estimation With Pseudo-irrelevance
  Feedback For Dense Retrieval'
authors: Giulio D'Erasmo, Giovanni Trappolini, Nicola Tonellotto, Fabrizio Silvestri
conference: Arxiv
year: 2024
bibkey: derasmo2024eclipse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.14967'}]
tags: ["Evaluation"]
short_authors: D'Erasmo et al.
---
Recent advances in Information Retrieval have leveraged high-dimensional
embedding spaces to improve the retrieval of relevant documents. Moreover, the
Manifold Clustering Hypothesis suggests that despite these high-dimensional
representations, documents relevant to a query reside on a lower-dimensional,
query-dependent manifold. While this hypothesis has inspired new retrieval
methods, existing approaches still face challenges in effectively separating
non-relevant information from relevant signals. We propose a novel methodology
that addresses these limitations by leveraging information from both relevant
and non-relevant documents. Our method, ECLIPSE, computes a centroid based on
irrelevant documents as a reference to estimate noisy dimensions present in
relevant ones, enhancing retrieval performance. Extensive experiments on three
in-domain and one out-of-domain benchmarks demonstrate an average improvement
of up to 19.50% (resp. 22.35%) in mAP(AP) and 11.42% (resp. 13.10%) in nDCG@10
w.r.t. the DIME-based baseline (resp. the baseline using all dimensions). Our
results pave the way for more robust, pseudo-irrelevance-based retrieval
systems in future IR research.