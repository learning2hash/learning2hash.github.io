---
layout: publication
title: 'Tricking The Hashing Trick: A Tight Lower Bound On The Robustness Of Countsketch
  To Adaptive Inputs'
authors: "Edith Cohen, Jelani Nelson, Tam\xE1s Sarl\xF3s, Uri Stemmer"
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: cohen2023tricking
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.00956'}]
tags: [AAAI, Hashing Methods, Robustness]
short_authors: Cohen et al.
---
CountSketch and Feature Hashing (the "hashing trick") are popular randomized
dimensionality reduction methods that support recovery of \(ℓ₂\)-heavy
hitters (keys \(i\) where \(v_i^2 > \epsilon \|\boldsymbol\{v\}\|_2^2\)) and
approximate inner products. When the inputs are \{\em not adaptive\} (do not
depend on prior outputs), classic estimators applied to a sketch of size
\(O(\ell/\epsilon)\) are accurate for a number of queries that is exponential in
\(\ell\). When inputs are adaptive, however, an adversarial input can be
constructed after \(O(\ell)\) queries with the classic estimator and the best
known robust estimator only supports \(\tilde\{O\}(\ell^2)\) queries. In this work
we show that this quadratic dependence is in a sense inherent: We design an
attack that after \(O(\ell^2)\) queries produces an adversarial input vector
whose sketch is highly biased. Our attack uses "natural" non-adaptive inputs
(only the final adversarial input is chosen adaptively) and universally applies
with any correct estimator, including one that is unknown to the attacker. In
that, we expose inherent vulnerability of this fundamental method.