---
layout: publication
title: Theory Of The GMM Kernel
authors: Ping Li, Cun-Hui Zhang
conference: Arxiv
year: 2016
bibkey: li2016theory
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.00550'}]
tags: ["Distance Metric Learning", "Hashing Methods"]
short_authors: Ping Li, Cun-Hui Zhang
---
We develop some theoretical results for a robust similarity measure named
"generalized min-max" (GMM). This similarity has direct applications in machine
learning as a positive definite kernel and can be efficiently computed via
probabilistic hashing. Owing to the discrete nature, the hashed values can also
be used for efficient near neighbor search. We prove the theoretical limit of
GMM and the consistency result, assuming that the data follow an elliptical
distribution, which is a very general family of distributions and includes the
multivariate \(t\)-distribution as a special case. The consistency result holds
as long as the data have bounded first moment (an assumption which essentially
holds for datasets commonly encountered in practice). Furthermore, we establish
the asymptotic normality of GMM. Compared to the "cosine" similarity which is
routinely adopted in current practice in statistics and machine learning, the
consistency of GMM requires much weaker conditions. Interestingly, when the
data follow the \(t\)-distribution with \(\nu\) degrees of freedom, GMM typically
provides a better measure of similarity than "cosine" roughly when \(\nu<8\)
(which is already very close to normal). These theoretical results will help
explain the recent success of GMM in learning tasks.