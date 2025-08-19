---
layout: publication
title: How Does The Degree Of Novelty Impacts Semi-supervised Representation Learning
  For Novel Class Retrieval?
authors: Quentin Leroy, Olivier Buisson, Alexis Joly
conference: Arxiv
year: 2022
bibkey: leroy2022how
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.08217'}]
tags: [Supervised, Similarity Search, Evaluation, Datasets]
short_authors: Quentin Leroy, Olivier Buisson, Alexis Joly
---
Supervised representation learning with deep networks tends to overfit the
training classes and the generalization to novel classes is a challenging
question. It is common to evaluate a learned embedding on held-out images of
the same training classes. In real applications however, data comes from new
sources and novel classes are likely to arise. We hypothesize that
incorporating unlabelled images of novel classes in the training set in a
semi-supervised fashion would be beneficial for the efficient retrieval of
novel-class images compared to a vanilla supervised representation. To verify
this hypothesis in a comprehensive way, we propose an original evaluation
methodology that varies the degree of novelty of novel classes by partitioning
the dataset category-wise either randomly, or semantically, i.e. by minimizing
the shared semantics between base and novel classes. This evaluation procedure
allows to train a representation blindly to any novel-class labels and evaluate
the frozen representation on the retrieval of base or novel classes. We find
that a vanilla supervised representation falls short on the retrieval of novel
classes even more so when the semantics gap is higher. Semi-supervised
algorithms allow to partially bridge this performance gap but there is still
much room for improvement.