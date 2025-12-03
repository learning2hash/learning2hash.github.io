---
layout: publication
title: Sign-full Random Projections
authors: Ping Li
conference: Arxiv
year: 2018
bibkey: li2018sign
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.00533'}]
tags: ["Datasets", "Distance Metric Learning", "Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Ping Li
---
The method of 1-bit ("sign-sign") random projections has been a popular tool
for efficient search and machine learning on large datasets. Given two \(D\)-dim
data vectors \(u\), \(v\in\mathbb\{R\}^D\), one can generate \(x = \sum_\{i=1\}^D u_i
r_i\), and \(y = \sum_\{i=1\}^D v_i r_i\), where \(r_i\sim N(0,1)\) iid. The
"collision probability" is \(\{Pr\}\left(sgn(x)=sgn(y)\right) =
1-\frac\{\cos^\{-1\}\rho\}\{\pi\}\), where \(\rho = \rho(u,v)\) is the cosine
similarity.
  We develop "sign-full" random projections by estimating \(\rho\) from (e.g.,)
the expectation \(E(sgn(x)y)=\sqrt\{\frac\{2\}\{\pi\}\} \rho\), which can be further
substantially improved by normalizing \(y\). For nonnegative data, we recommend
an interesting estimator based on \(E\left(y_- 1_\{x\geq 0\} + y_+ 1_\{x<0\}\right)\)
and its normalized version. The recommended estimator almost matches the
accuracy of the (computationally expensive) maximum likelihood estimator. At
high similarity (\(\rho\rightarrow1\)), the asymptotic variance of recommended
estimator is only \(\frac\{4\}\{3\pi\} \approx 0.4\) of the estimator for sign-sign
projections. At small \(k\) and high similarity, the improvement would be even
much more substantial.