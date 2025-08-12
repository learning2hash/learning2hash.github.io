---
layout: publication
title: 'Binarsity: A Penalization For One-hot Encoded Features In Linear Supervised
  Learning'
authors: "Mokhtar Z. Alaya, Simon Bussy, St\xE9phane Ga\xEFffas, Agathe Guilloux"
conference: Arxiv
year: 2019
bibkey: alaya2017binarsity
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.08619'}]
tags: ["Supervised"]
short_authors: Alaya et al.
---
This paper deals with the problem of large-scale linear supervised learning
in settings where a large number of continuous features are available. We
propose to combine the well-known trick of one-hot encoding of continuous
features with a new penalization called *binarsity*. In each group of
binary features coming from the one-hot encoding of a single raw continuous
feature, this penalization uses total-variation regularization together with an
extra linear constraint. This induces two interesting properties on the model
weights of the one-hot encoded features: they are piecewise constant, and are
eventually block sparse. Non-asymptotic oracle inequalities for generalized
linear models are proposed. Moreover, under a sparse additive model assumption,
we prove that our procedure matches the state-of-the-art in this setting.
Numerical experiments illustrate the good performances of our approach on
several datasets. It is also noteworthy that our method has a numerical
complexity comparable to standard \\(\ell_1\\) penalization.