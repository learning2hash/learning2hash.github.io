---
layout: publication
title: Re-assessing The "classify And Count" Quantification Method
authors: Alejandro Moreo, Fabrizio Sebastiani
conference: Lecture Notes in Computer Science
year: 2021
bibkey: moreo2020re
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.02552'}]
tags: []
short_authors: Alejandro Moreo, Fabrizio Sebastiani
---
Learning to quantify (a.k.a.\ quantification) is a task concerned with
training unbiased estimators of class prevalence via supervised learning. This
task originated with the observation that "Classify and Count" (CC), the
trivial method of obtaining class prevalence estimates, is often a biased
estimator, and thus delivers suboptimal quantification accuracy; following this
observation, several methods for learning to quantify have been proposed that
have been shown to outperform CC. In this work we contend that previous works
have failed to use properly optimised versions of CC. We thus reassess the real
merits of CC (and its variants), and argue that, while still inferior to some
cutting-edge methods, they deliver near-state-of-the-art accuracy once (a)
hyperparameter optimisation is performed, and (b) this optimisation is
performed by using a true quantification loss instead of a standard
classification-based loss. Experiments on three publicly available binary
sentiment classification datasets support these conclusions.