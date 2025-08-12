---
layout: publication
title: 'Fw-shapley: Real-time Estimation Of Weighted Shapley Values'
authors: Pranoy Panda, Siddharth Tandon, Vineeth N Balasubramanian
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: panda2024fw
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.06602'}]
tags: ["Efficiency", "ICASSP"]
short_authors: Pranoy Panda, Siddharth Tandon, Vineeth N Balasubramanian
---
Fair credit assignment is essential in various machine learning (ML)
applications, and Shapley values have emerged as a valuable tool for this
purpose. However, in critical ML applications such as data valuation and
feature attribution, the uniform weighting of Shapley values across subset
cardinalities leads to unintuitive credit assignments. To address this,
weighted Shapley values were proposed as a generalization, allowing different
weights for subsets with different cardinalities. Despite their advantages,
similar to Shapley values, Weighted Shapley values suffer from exponential
compute costs, making them impractical for high-dimensional datasets. To tackle
this issue, we present two key contributions. Firstly, we provide a weighted
least squares characterization of weighted Shapley values. Next, using this
characterization, we propose Fast Weighted Shapley (FW-Shapley), an amortized
framework for efficiently computing weighted Shapley values using a learned
estimator. We further show that our estimator's training procedure is
theoretically valid even though we do not use ground truth Weighted Shapley
values during training. On the feature attribution task, we outperform the
learned estimator FastSHAP by \(27%\) (on average) in terms of Inclusion AUC.
For data valuation, we are much faster (14 times) while being comparable to the
state-of-the-art KNN Shapley.