---
layout: publication
title: Characterizing Multiple Instance Datasets
authors: Veronika Cheplygina, David M. J. Tax
conference: Lecture Notes in Computer Science
year: 2015
bibkey: cheplygina2015characterizing
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.08186'}]
tags: ["Datasets"]
short_authors: Veronika Cheplygina, David M. J. Tax
---
In many pattern recognition problems, a single feature vector is not
sufficient to describe an object. In multiple instance learning (MIL), objects
are represented by sets (*bags*) of feature vectors (*instances*).
This requires an adaptation of standard supervised classifiers in order to
train and evaluate on these bags of instances. Like for supervised
classification, several benchmark datasets and numerous classifiers are
available for MIL. When performing a comparison of different MIL classifiers,
it is important to understand the differences of the datasets, used in the
comparison. Seemingly different (based on factors such as dimensionality)
datasets may elicit very similar behaviour in classifiers, and vice versa. This
has implications for what kind of conclusions may be drawn from the comparison
results. We aim to give an overview of the variability of available benchmark
datasets and some popular MIL classifiers. We use a dataset dissimilarity
measure, based on the differences between the ROC-curves obtained by different
classifiers, and embed this dataset dissimilarity matrix into a low-dimensional
space. Our results show that conceptually similar datasets can behave very
differently. We therefore recommend examining such dataset characteristics when
making comparisons between existing and new MIL classifiers.
  The datasets are available via Figshare at https://bit.ly/2K9iTja.