---
layout: publication
title: Bayesian Metric Learning For Uncertainty Quantification In Image Retrieval
authors: Frederik Warburg, Marco Miani, Silas Brack, Soren Hauberg
conference: Arxiv
year: 2023
bibkey: warburg2023bayesian
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.01332'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation]
short_authors: Warburg et al.
---
We propose the first Bayesian encoder for metric learning. Rather than
relying on neural amortization as done in prior works, we learn a distribution
over the network weights with the Laplace Approximation. We actualize this by
first proving that the contrastive loss is a valid log-posterior. We then
propose three methods that ensure a positive definite Hessian. Lastly, we
present a novel decomposition of the Generalized Gauss-Newton approximation.
Empirically, we show that our Laplacian Metric Learner (LAM) estimates
well-calibrated uncertainties, reliably detects out-of-distribution examples,
and yields state-of-the-art predictive performance.