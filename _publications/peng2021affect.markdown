---
layout: publication
title: 'Affect-dml: Context-aware One-shot Recognition Of Human Affect Using Deep
  Metric Learning'
authors: Kunyu Peng, Alina Roitberg, David Schneider, Marios Koulakis, Kailun Yang,
  Rainer Stiefelhagen
conference: 2021 16th IEEE International Conference on Automatic Face and Gesture
  Recognition (FG 2021)
year: 2021
bibkey: peng2021affect
citations: 3
additional_links: [{name: Code, url: 'https://github.com/KPeng9510/Affect-DML'}, {
    name: Paper, url: 'https://arxiv.org/abs/2111.15271'}]
tags: [Evaluation, Distance Metric Learning, Datasets]
short_authors: Peng et al.
---
Human affect recognition is a well-established research area with numerous
applications, e.g., in psychological care, but existing methods assume that all
emotions-of-interest are given a priori as annotated training examples.
However, the rising granularity and refinements of the human emotional spectrum
through novel psychological theories and the increased consideration of
emotions in context brings considerable pressure to data collection and
labeling work. In this paper, we conceptualize one-shot recognition of emotions
in context -- a new problem aimed at recognizing human affect states in finer
particle level from a single support sample. To address this challenging task,
we follow the deep metric learning paradigm and introduce a multi-modal emotion
embedding approach which minimizes the distance of the same-emotion embeddings
by leveraging complementary information of human appearance and the semantic
scene context obtained through a semantic segmentation network. All streams of
our context-aware model are optimized jointly using weighted triplet loss and
weighted cross entropy loss. We conduct thorough experiments on both,
categorical and numerical emotion recognition tasks of the Emotic dataset
adapted to our one-shot recognition problem, revealing that categorizing human
affect from a single example is a hard task. Still, all variants of our model
clearly outperform the random baseline, while leveraging the semantic scene
context consistently improves the learnt representations, setting
state-of-the-art results in one-shot emotion recognition. To foster research of
more universal representations of human affect states, we will make our
benchmark and models publicly available to the community under
https://github.com/KPeng9510/Affect-DML.