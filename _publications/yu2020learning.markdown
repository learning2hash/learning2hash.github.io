---
layout: publication
title: Learning Diverse And Discriminative Representations Via The Principle Of Maximal
  Coding Rate Reduction
authors: Yaodong Yu, Kwan Ho Ryan Chan, Chong You, Chaobing Song, Yi Ma
conference: Arxiv
year: 2020
bibkey: yu2020learning
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.08558'}]
tags: ["Datasets", "Self-Supervised", "Supervised", "Unsupervised"]
short_authors: Yu et al.
---
To learn intrinsic low-dimensional structures from high-dimensional data that
most discriminate between classes, we propose the principle of Maximal Coding
Rate Reduction (\(\text\{MCR\}^2\)), an information-theoretic measure that
maximizes the coding rate difference between the whole dataset and the sum of
each individual class. We clarify its relationships with most existing
frameworks such as cross-entropy, information bottleneck, information gain,
contractive and contrastive learning, and provide theoretical guarantees for
learning diverse and discriminative features. The coding rate can be accurately
computed from finite samples of degenerate subspace-like distributions and can
learn intrinsic representations in supervised, self-supervised, and
unsupervised settings in a unified manner. Empirically, the representations
learned using this principle alone are significantly more robust to label
corruptions in classification than those using cross-entropy, and can lead to
state-of-the-art results in clustering mixed data from self-learned invariant
features.