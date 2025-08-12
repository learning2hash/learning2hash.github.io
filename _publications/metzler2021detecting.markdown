---
layout: publication
title: 'Detecting Potentially Harmful And Protective Suicide-related Content On Twitter:
  A Machine Learning Approach'
authors: Hannah Metzler, Hubert Baginski, Thomas Niederkrotenthaler, David Garcia
conference: Journal of Medical Internet Research
year: 2022
bibkey: metzler2021detecting
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04796'}]
tags: []
short_authors: Metzler et al.
---
Research shows that exposure to suicide-related news media content is
associated with suicide rates, with some content characteristics likely having
harmful and others potentially protective effects. Although good evidence
exists for a few selected characteristics, systematic large scale
investigations are missing in general, and in particular for social media data.
We apply machine learning methods to classify large quantities of Twitter data
according to a novel annotation scheme that distinguishes 12 categories of
suicide-related tweets. We then trained a benchmark of machine learning models
including a majority classifier, an approach based on word frequency (TF-IDF
with a linear SVM) and two state-of-the-art deep learning models (BERT, XLNet).
The two deep learning models achieved the best performance in two
classification tasks: In the first task, we classified six main content
categories, including personal stories about either suicidal ideation and
attempts or coping, calls for action intending to spread either problem
awareness or prevention-related information, reporting of suicide cases, and
other tweets irrelevant to these categories. The deep learning models reached
accuracy scores above 73% on average across the six categories, and F1-scores
in between 0.70 and 0.85 for all but the suicidal ideation and attempts
category (0.51-0.55). In the second task, separating tweets referring to actual
suicide from off-topic tweets, they correctly labeled around 88% of tweets,
with BERT achieving F1-scores of 0.93 and 0.74 for the two categories,
respectively. These classification performances are comparable to the
state-of-the-art on similar tasks. By making data labeling more efficient, this
work has enabled large-scale investigations on harmful and protective
associations of social media content with suicide rates and help-seeking
behavior.